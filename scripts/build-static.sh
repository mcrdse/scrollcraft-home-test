#!/usr/bin/env bash
set -euo pipefail

project_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
output_dir="$project_dir/dist"

if [[ "$output_dir" != "$project_dir/dist" ]]; then
  echo "Refusing to build outside the project dist directory." >&2
  exit 1
fi

rm -rf "$output_dir"
mkdir -p "$output_dir"

cp "$project_dir/index.html" "$project_dir/colony.css" "$project_dir/scrollcraft.css" "$project_dir/scrollcraft.js" "$project_dir/robots.txt" "$project_dir/_headers" "$project_dir/og.jpg" "$output_dir/"

while IFS= read -r asset; do
  case "$asset" in
    http:*|https:*|data:*|'') continue ;;
  esac
  mkdir -p "$output_dir/$(dirname "$asset")"
  cp "$project_dir/$asset" "$output_dir/$asset"
done < <(rg -o '(src|poster)="[^"]+"' "$project_dir/index.html" | sed -E 's/^[^=]+="(.*)"$/\1/' | sort -u)

# Keep the hosted package small while preserving the high-quality source media.
# These website videos are silent, so the deployment copies do not need audio
# tracks or editing-grade bitrates.
if command -v ffmpeg >/dev/null 2>&1; then
  while IFS= read -r video; do
    optimized_video="$video.optimized.mp4"
    ffmpeg -nostdin -loglevel error -y -i "$video" \
      -an -c:v libx264 -preset medium -crf 32 -pix_fmt yuv420p \
      -movflags +faststart "$optimized_video"
    mv "$optimized_video" "$video"
  done < <(find "$output_dir" -type f -name '*.mp4' -size +900k -print)

  while IFS= read -r photo; do
    optimized_photo="${photo%.jpg}.optimized.jpg"
    ffmpeg -nostdin -loglevel error -y -i "$photo" \
      -vf "scale='min(1600,iw)':-2" -q:v 5 "$optimized_photo"
    mv "$optimized_photo" "$photo"
  done < <(find "$output_dir" -type f -name '*.jpg' -size +400k -print)
fi

echo "Built static site in $output_dir"
