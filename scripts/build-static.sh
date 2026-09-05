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

cp "$project_dir/index.html" "$project_dir/colony.css" "$project_dir/scrollcraft.css" "$project_dir/scrollcraft.js" "$project_dir/robots.txt" "$project_dir/_headers" "$project_dir/og.png" "$output_dir/"

while IFS= read -r asset; do
  case "$asset" in
    http:*|https:*|data:*|'') continue ;;
  esac
  mkdir -p "$output_dir/$(dirname "$asset")"
  cp "$project_dir/$asset" "$output_dir/$asset"
done < <(rg -o '(src|poster)="[^"]+"' "$project_dir/index.html" | sed -E 's/^[^=]+="(.*)"$/\1/' | sort -u)

echo "Built static site in $output_dir"
