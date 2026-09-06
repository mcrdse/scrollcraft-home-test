# BRIEF.md — mcrdse.com homepage redo (scrollcraft)

Interviewed with Kevin (Kecho), 2026-09-02. Kevin's opening brief plus one four-question pass
(offer, structure, peak, assets). Answers below are his words where he gave them.

**Page job:** the mcrdse.com homepage. Hard first-order offer up top (IM8 / AG1 model: hero
products plus a bonus stack), then where it is grown, then what is in it, then community, then
a globe of real orders. Primary CTA everywhere: **"Claim the $111"** → mcrdse.shop/bundle-111.

## The eight answers
1. **Vibe + refs.** "premium and engaging." Refs (his): IM8, AG1 (as the *offer model*, not the
   look). Carried from the Duo build's locked vibe: grounded, clinical, earthy, quietly magical
   (Aesop, Kinfolk, "Fantastic Fungi"). Dark this time: the grow needs the dark.
2. **Journey (his sequence).** "focus and bliss as the main focal point, Hermetica as the added
   bonus, an offer they can't refuse, a hard first time offer" → "where the products are from,
   California grown" → "a hyperlapse image of mycelium growing into mushrooms" → "what's in the
   product, the ingredients" → "the community side" → "a globe map with realistic mushroom
   targets of the people that have purchased, to show people microdosing around the world."
3. **Energy.** Loud open (the offer lands), quiet (California), LOUD peak (the grow), steady
   (ingredients), warm (community), wide then still (globe + close). Not asked separately;
   derived from his sequence and confirmed by the peak choice.
4. **Feeling + peak.** Peak = **the mycelium hyperlapse** ("the screen goes dark and mycelium
   grows under your hand, threading into a mushroom as you scroll"). Chosen over the globe and
   the offer reveal.
5. **One thing no site does.** "a globe map that has cool realistic mushroom targets of the
   people that have purchased and where they're at." → the signature move.
6. **Range.** Premium base. One maximalist act (the peak). Dark family throughout.
7. **World.** **Distinct scenes.** Chosen over one unbroken world.
8. **Assets.** "Generate it all (kie.ai)" for the grow. Real on disk: Focus/Bliss transparent
   tubes, Duo combo shot, Hush tin photo (real), 20 ingredient cutouts, both supplement-facts
   labels, press SVGs, bliss-2-0-nature.webp. Blue Crush and Eternity have **no real photos**
   (shop uses a placeholder); shown as typographic tiles, never a fake product shot.
   **kie.ai key in `~/scrollcraft-lab/.env` returns 401** at build time. Generation is
   blocked; the peak ships as a scroll-driven canvas grow, with the scrub slot documented
   below for the clip once a working key lands.

## Feeling curve (one line per act)
1. Disbelief: the stack lands piece by piece and the total halves in front of them.
2. Ground: one still photograph, small honest copy, nothing moving. The silence before the peak.
3. Awe: a white block on slate. Pins. Then a whole flush comes up under the scroll.
4. Substance: eighteen actives travel sideways, each labelled like a specimen, ending on the
   two real facts labels.
5. Belonging: real counts and real words from named people.
6. Warmth: hands over the pack, the scroll pushes in, "pass it on". (Final form: the pour clip,
   tubes swapped in for the pouches, scrubbed under the wheel.)
7. Wonder, then resolve: the earth turns and mushrooms sprout on 768 real cities, comes back
   around to California, and holds on the CTA.

**The peak** (act 3, largest span): "I scrolled and the mushrooms grew right out of the block
under my hand."

**Tell-someone:** "it's the site where you grow the mushroom yourself, then watch it sprout
on every city that ordered one."

**Signature move:** *the world sprouts.* A canvas globe (orthographic, dotted land) in the
close, turning under scroll from California, all the way round, back to California. 768
geocoded city rows (2,486 real orders from D1, tests and refunds excluded; 15 rows Nominatim could not resolve) sprout as
mushroom glyphs, sized by order count, in the order the globe turns past them. Pointer
drag spins it; holding still surfaces the city names in view. Same mushroom glyph as the
peak's fruit, so peak and signature are one idea in two beats.

**Authored silence:** act 2 (California) is deliberately still: one reveal, one paragraph,
no motion after the reveal lands. Not dead scroll.

## Grammar: filmic one-shot
The other seven, and why they lost: chaptered editorial is taken by focus-bliss-duo (and a
store homepage should feel carried, not read); live surface is for software; continuous
world was offered and declined (Q7); typographic poster has no room for product; gallery is
for "what are the options" and this page sells one offer; split stage would force California
and the globe into two columns for no reason; rhythmic cutlist is the wrong pulse for premium
and bans the pinned peak. Filmic fits: one linear argument, one emotional arc, consumer
product, visitor carried. Burden of proof met: it is the first filmic build in this registry.

Nav = fixed minimal bar, wordmark + the one CTA. Close = pinned globe, spotlight, magnetic CTA,
footer inside the stage.

## Score
| Beat | Feeling | Device | Span | Family |
|---|---|---|---|---|
| 1 Offer | disbelief | pin + bespoke stack assembly + count ledger, kinetic h1 | 2.4 | pin |
| 2 California | ground | flow + reveal (silence) | ~1.0 | flow/reveal |
| 3 PEAK grow | awe | scrub: kling clip, bare block → full flush, tail-locked to the flush still | 3.4 | scrub |
| 4 Inside | substance | pan rail of 18 actives + 2 real labels | 3.0 | pan |
| 5 Community | belonging | flow + count (real D1 numbers) + quotes | ~1.0 | flow/count |
| 6 Share | warmth | scrub: kling clip of the pour, tubes swapped in from Kevin's photo | 1.4 | scrub |
| 7 Close | wonder → resolve | pin + globe canvas + spotlight + magnet CTA | 1.7 | pin/pointer |

Seven acts, 13.4 viewport-heights. No adjacent family repeats. Two scrub acts (peak, share),
the cap. Peak span 3.4, largest by a clear margin; act before it is the quietest.

## Palette change (Kevin, 2026-09-02 afternoon)
"No purple dark matter." Whole page moved to the mcrdse.com cream/kraft palette: cream canvas,
bisque surfaces, abyss ink, purple CTA only. The peak sits on the slate blue-grey of Kevin's
fruiting-block photo (#9AAAB4) with white hyphae and golden caps, which is the kie.ai target.
Kevin's Desktop folder "Website build products" supplied: hands-heart photo (real, old pouch
pack), hands-pour photo (real, old pouches), and two AI tube renders with baked label typos
("ULOCKED", "cspsule") and wrong Bliss ingredients. Renders are colour references only,
never shown. Prompts for the grow clip, the California stills and the pour clip (tubes
swapped in via image-to-image) are staged in `out/PROMPTS.md`.

## Fingerprint gate vs focus-bliss-duo
1 grammar: filmic vs chaptered ✓ · 2 nav: fixed bar + CTA vs margin folio ✓ · 3 hero:
pinned product-stack assembly vs type-only title page ✓ · 4 shape: pin→flow→pin→pan→flow→scrub→pin,
7 acts @ 13.5 vs flow→pan→pin→count→flow→reveal @ 10.7 ✓ · 5 close: pinned globe + magnetic
button vs reveal-up masthead + running-text link ✓ · 6 signature: the world sprouts vs the
capsule bloom ✓. 6 of 6. Shares: brand faces (Newsreader/Sora), lowercase headline voice,
"distinct scenes" world answer.

## Real numbers used (D1 `mcrdse-orders`, is_test=0, not refunded, pulled 2026-09-02)
2,838 orders · 1,390 customers · 863 cities · 49 states (no Nebraska yet) · 9 countries
(US, AU, CA, GB, NL, IT, IL, CZ, CH) plus Puerto Rico · first order 2024-02-04.
Offer items per shop catalog: Duo $117.77 · Hush $34 · Blue Crush $33 · Eternity $33
= **$217.77** struck → $111. (Shop headline says "$222"; itemized truth used here. Flagged.)

## Design floor
Newsreader display (+ italic `<em>` accent word) / Sora text. Dark family: canvas #0F0818,
surface #1A0E2E, peak ground #07050C, brand abyss #1E0A38. Ink cream #F2E8DA, soft #B9A9C9.
Purple #8E2CFB is CTA/links only. Lowercase headlines. No medical claims. No "psilocybin".

## Hard rules that bite here
No scroll cue. No counters. No em dashes in copy. Vary the anchor (lead / split / center /
trail). ≥4 families, none twice in a row, ≤2 scrub. Real numbers only. One peak. Close holds.
transform/opacity/clip-path only. Run Step 5.

## Pending (Kevin)
- Working `KIE_AI_API_KEY` + credits. Then: 1 mycelium grow clip (kling, ~160 credits) with
  poster, wired as `data-sc-scrub` under the canvas in act 3, plus 2 California grow stills
  (~56 credits) to replace bliss-2-0-nature.webp in act 2.
- Real Blue Crush and Eternity photos, if they exist.
- Decide $217.77 vs $222 on the shop page.
- Port to `src/pages/index.astro` once approved (currently standalone HTML on the engine).

## Generated 2026-09-02 (kie.ai, key from Doppler `KIE_AI_API_KEY`, balance 10,080 before)
6 seedream stills + 2 kling 5s clips, zero rerolls. Planning ceiling 6×28 + 2×160 = 488 credits.
Peak = `assets/03-grow.mp4` (+ mobile, poster). Share = `assets/06-pour.mp4` (+ mobile, poster).
California figure = `assets/02-room.webp`; `02-macro.webp` in reserve. Heart with the Focus
tube = `assets/06-heart.webp`, placed in the community quotes grid. Canvas grow removed.

## Round 3 (Kevin, 2026-09-03)
Real site wordmark (SVG path from Nav.astro) in the bar and footer. Display type = the site's
hard-hitting style: Newsreader 800, italic 700 accent word. Press strip moved to its own flow
act right after the offer. California grow-room section moved to the end, just before the
close. Community act now carries US macro stats (NSDUH 2024, RAND 2024) instead of order
counts. Close = interactive US map: SAMHSA 2023-2024 state estimates of past-year hallucinogen
use (18+) as a cream→lilac→amethyst choropleth that paints west to east under scroll, then 34
verified decriminalization cities/states sprout as mushroom markers in year order; hover a
state for its %, hover a marker for the measure. Pour clip leans with the pointer (spotlight
vars). Globe and its D1 order data retired from the page (geo.json stays in data/).
Acts: pin → flow → scrub → pan → flow → scrub → flow → pin · 8 acts · ~13.7vh.
Research in `data/research.json` + `data/research.md` (every figure with URL and year).

## Round 4 (Kevin, 2026-09-03, Magic Mind reference)
Hero rebuilt as a scrub act in the reference layout: copy + ledger + CTA in the left 40%,
a generated clip in the right 57%. Clip = kling from a seedream still of two people's hands
holding the real Focus and Bliss tubes (refs: the tube cutouts); kling pulled the hands apart,
the clip is reversed and trimmed so the scroll brings the tubes together into the toast.
Headline is now the promise at display scale, two lines: "sharp days. calm nights."
Also generated: a high-def studio shot of both tubes on cream (`assets/01-tubes.webp`), kept
for product pages / the Astro port. Acts: scrub → flow → scrub → pan → flow → scrub → flow →
pin · 8 acts · 13.9vh · three scrub acts (hero, peak, share).

## Round 5 (Kevin, 2026-09-03): Stripe guardrail + simplified offer
Kevin: "I can't say psilocybin because of Stripe. Let's have guardrails." → `scripts/guard.py`
scans copy for BLOCK terms (psilocybin, psilocin, hallucinogen, psychedelic, entheogen,
decriminaliz*, shrooms, magic mushroom, strain names, trip, get high) and WARN terms the live
site already uses (microdos*, golden teacher, strain, genetics). Run it on every build; the
Astro port should run it on `dist/` in CI. Live-site baseline: 0 psilocybin/hallucinogen in
rendered copy, so the approved surface stays clean.
Consequences: the SAMHSA/RAND stats and the decriminalization map are OFF this page (they
belong on mcrdsemovement.com, no checkout there). Community = the store's own people (1,390
people, 49 states, 2,838 orders, 1 in 3 reorder, all D1). Close = US map shaded by MCRDSE
customers per state (`data/customers-by-state.json`, 1,345 people with a US state), hover
gives the count, plus links to the Movement site and Telegram. Movement CRM was checked as a
source and rejected: 9,223 contacts are mostly cold LinkedIn/Meta leads with 25 states filled.
Offer simplified to the AG1/IM8 model: headline "the whole stack, half off.", bolded
components, a five-line "what you get" list with thumbnails and prices, strike to $111, free
shipping. Cheers clip stays as the hero visual. "Our own genetics" replaces any strain name.

## Round 6 (2026-09-03): "keep reiterating"
Cold feel-check (desktop): clear · trust · awe · substance · warm · tender · ground · resolve.
Intended: disbelief · trust · awe · substance · belonging · warmth · ground · resolve. Match,
with one softness: community (warm) and share (tender) sit next to each other; kept, because
the share clip is Kevin's ask and the community act is proof rather than feeling.
Change: the Hermetica trio now lands as chips over the clip column while the tubes meet
(Hush tin photo; Blue Crush / Eternity as initials until real photos exist). Mobile: chips in
one row over the clip; pour scrim lightened.

## Round 7 (2026-09-03): promo strip
Kevin: "lets just do scarcity cause it works" (overrides the anti-slop rule for store offer
chrome; logged as a feedback memory). Fixed strip above the nav in abyss ink: "<Month>: the
$111 stack · Focus 2.0 + Bliss 2.0 + the Hermetica trio · $217.77 of product · free shipping"
plus an evergreen countdown to the end of the visitor's current month that rolls over
automatically. `--promo-h` offsets the nav and every pinned stage's top copy. Mobile hero copy
sits on a solid cream plate so the list + CTA never overlap the clip. Harness freezes the
clock, so its frames show 00:00:00:00; verified live values with lab/probe-timer.mjs.

## Round 8 (2026-09-04): IM8 subscribe-and-save model
Kevin (voice, parsed): countdown ends Sunday (evergreen weekly, rolls to next Sunday). Offer
becomes a subscription: **90-day supply $99/mo, billed $297 per 90 days, $3.30/day, save 55%**
against $222 of product per month at list; 30-day supply 20% higher = $119/mo ($3.96/day, save
46%); one-time 30 days 40% higher = $139 ($4.63/day, save 37%). Free welcome kit, $112 value:
5 Hermetica sachets, 60-count Hermetica superfood gummies, a journal, a mystery kit. Free
exclusive access to the 90-day integration coaching program. Cancel or pause anytime. 90-day
money-back guarantee. Hermetica items are never individually priced on the page.
Page: strip = "Ends Sunday: save 55% + free welcome kit"; hero headline "the whole stack,
$3.30 a day."; welcome-kit chips over the cheers clip; new flow act **1a · plans** with three
radio cards, checklist, and a CTA that follows the selection. One CTA label everywhere:
"Start from $3.30/day". CTA still points at mcrdse.shop/bundle-111 (the shop has no
subscription plans yet: needs 3 Stripe prices + the welcome-kit SKU; flagged).
Unparsed from the voice note: "based off the Nike plan, four instead of five" (unknown intent).

## Round 9 (2026-09-04): per-day anchors
Kevin set the per-day prices: 90-day $3.33/day, 30-day $4.44/day, one-time $5.55/day. Worked
back at 30 days/month: $99.90/mo billed $299.70 per 90 days (save 55%); $133.20/mo (save 40%);
$166.50 one-time (save 25%). Savings vs $222/mo list. CTA label "Start from $3.33/day".

## Round 10 (2026-09-04)
Logo: restored `fill-rule="evenodd"` on the wordmark path (counters were filling in). 🍄 next
to Focus 2.0 and Bliss 2.0, 🍄🍄🍄 after "free welcome kit" above the fold. Plans lede: "Feel
limitless again." Free shipping only on the 90-day supply; others "plus shipping". Prices:
90-day $77/mo ($2.57/day, billed $231 per 90 days, save 65%, free shipping); 30-day $99/mo
($3.30/day, save 55%); one-time $139 ($4.63/day, save 37%). Best-value card carries a pulsing
purple halo (reduced-motion: static glow). Every `.cta` and plan press fires an illumination
ring plus seven 🍄 spores from the pointer ("dopamine on press", Kevin's ask; neon-glow taste
rule waived by him). One-time price was not given; kept at +40% over the 30-day.

## Round 11 (2026-09-04)
Headline "feel the magic for $2.57 a day." with italic small print "Less than a cup of coffee a
day to feel the best version of yourself again." No 🍄 after the welcome kit. "limitless" in
the plans lede drifts and carries a passing light (static under reduced motion). Plans lede
job chosen by Kevin: make it about the 90 days → "A ritual takes weeks to feel natural. Ninety
days is where it sticks." (habit framing, not an efficacy claim). Hero shipping line now
"Ships free on the 90-day."

## Round 12 (2026-09-04): peak rebuilt, narrow-window fixes
Kevin: mushrooms "explode into dried mushrooms and capsules" (reference photo), no bubble box
behind the copy, better font, smoother in/out. Peak now: block → pins → fruits, then at p≈0.78
the flush swells 12% and a spore shower (🍄/💊) fires while a circular iris opens onto a
generated flat lay (`assets/03-flat.webp`, capsules alternating with dried caps on the same
slate) with "whole. dried. capsuled." + "Nothing isolated, nothing extracted. The whole
mushroom goes in the capsule." Copy: Newsreader display, top-left slate area, no plates, each
line in its own cue window with a gap and 0.22-0.28 ramps. COA links removed. Hero and close
both stack under 1100px (Kevin's window was ~1040 wide). Page 14.4vh (over budget by 0.4;
Kevin keeps adding acts, accepted).

## Round 13 (2026-09-04): framing, no-slop pass
Kevin's window (~1860x900): the bar overlapped the hero label and the kinetic line masks
clipped descenders. Fixed: copy padding-top = bar + 5.5rem, h1 line-height 1.02 + descender
padding, kit chips bounded to the clip column. Exclusivity framing: a fixed hairline frame
with corner marks (certificate feel) over every stage, and a rule before the hero label
"sharp days, calm nights · first-order pricing". no-ai-slop pass over all 129 copy lines:
removed the unverifiable "Most people here were handed their first dose by a friend"
("The best way in is a friend who already runs it."), replaced the negative-listing capsule
line ("Cap and stem, ground whole, into the capsule."), "weekly note" → "weekly letter" to
kill note/notes repetition. Found and removed a duplicated promo strip left from a rejected
edit. Verified at 1440x900, 1860x900, 390x844.

## Round 14 (2026-09-04): CTA target
Kevin: keep mcrdse.shop and mcrdse.com separate; the CTA must land on the offer on mcrdse.com.
All CTAs now → https://mcrdse.com/shop/mcrdse-focus-bliss-dose-one-month-combo?plan=90|30|1
(the plan picker sets both label and href). No mcrdse.shop links remain. The Duo page today
has a subscribe/one-time radio ("purchase-type") and ignores `plan`; the Astro port must
(a) read `plan` to preselect, and (b) add the $77 90-day / $99 monthly / $139 one-time Stripe
prices and the welcome kit, since the live page still prices the Duo at $77.77 sub / $117.77.

## Round 12 (9/4): Stamets quote act
New flow section `#stamets` after INSIDE (ingredients) and before COMMUNITY, matching Magic Mind: their single big endorsement (Matthew Stafford) sits right after the ingredients/benefits block, before research stats; the 3-quote row and advisory board come later. White ground, left = "Mushrooms can help save the world." (Mycelium Running subtitle), right = kie-colorized/outpainted `assets/stamets-wide-1600.webp` (source Downloads/"paul and mush.jpg", variant B, near-white flattened to #fff). guard.py 0 block. Pre-edit copy at out/index.pre-stamets.html.

Round 12b (9/4): Stamets block mirrored to Magic Mind layout (round portrait badge left, quote right, cream ground), lede added under the attribution on the new-beginning theme ("sharp in the morning and calm at night"). Kevin: no quiz, no product picker; hero-product page like AG1. No second proof layer (3-quote row / advisory board) yet, nothing to fill it with.

Round 13 (9/4): COMMUNITY polish (impeccable). BUG: `.counts span` was hitting the `.sc-nums` span inside `<b>` so every count rendered at caption size and "1 in 3" wrapped; now `.counts > div > span`. Quotes: removed the nth-child size bump, all three at t-lg/1.4 in equal columns, image column 3fr, blockquotes stretch with footer pinned bottom, hairline top + kraft opening-mark ::before (markup quotes stripped), product as a pill tag. Mobile image 4:3. Impeccable context.mjs reports NO_PRODUCT_MD; BRIEF.md stands in, init skipped on purpose.

Round 14 (9/4): keyword highlights `mark.hl` (kraft underline band; accent band inside the dark promo bar) on 90-day supply / free shipping on the 90-day supply / 90-day money-back guarantee / free welcome kit $112 / cancel or pause anytime / 90-day integration coaching. Wording unified: "90-day guarantee" -> "90-day money-back guarantee" everywhere. `.checks li` switched from flex to absolute check so inline marks do not split the sentence. Products: Pure Dose testimonial replaced with Brandon W. / Focus 2.0 from mcrdse-site src/data/reviews.json (lightly trimmed punctuation); page now names only Focus 2.0 and Bliss 2.0 as products (welcome kit gummies/sachets stay as the free kit, flagged to Kevin). Footer: discreet nofollow "members" link to mcrdse.shop/members-gate; no other .shop link on the page. Pre-edit copy at out/index.pre-hl.html.

## Round 15 (2026-09-05): seams + copy pass (no-ai-slop, tasteskill, impeccable)
Kevin: "things need to transition smoother and flow between each other." Contact sheets of every
act seam (lab/seams.mjs → lab/shots/) showed the cause: each pinned stage left the page as a
hard-edged rectangle sliding under the next flow section. Fix is one CSS rule: every scrub/pin/pan
stage gets a `::before` feather (13% band top and bottom) painted in `--sc-canvas`, which is the
engine's drift colour, so the band always matches whatever the page is at that moment. Close copy
un-gated from cues (a pin's copy cannot show before p=0, so the map arrived blank); unpainted
states darkened to #E9DCC9 so the map reads on arrival. Copy: coffee line cut to "Less than a cup
of coffee a day."; ledger loses the duplicated guarantee (still in the promo bar and plans); plans
h2 "give it ninety days."; "Exclusive access" dropped; peak end "dried whole, ground whole." +
"Cap and stem, nothing extracted, into the capsule."; inside h2 "eighteen actives, every one
named." with the dot legend fixed (the "both" dot was lilac, same as Bliss; now a kraft/lilac
split dot and the copy says so); Stamets lede loses the "new beginning, grown from the ground up"
kicker; close lede no longer repeats the community lede. Kept on purpose (Kevin's asks, taste
rules waived): gradient light on "limitless", best-plan halo, certificate frame, 🍄 spores.
Pre-edit copy at out/index.pre-seams.html. guard.py 0 block. 0 em dashes.

## Round 15b (2026-09-05): flow audit (shoot.mjs, 6 frames per act)
Kevin: "some of the transitions were kind of iffy." Harness run over 70 frames. Fixed: hero dwell
0.3 → 0.12 and pour dwell 0.35 → 0.15 (both left the clip hanging with no copy after the copy
exited); pour copy now holds to p=1 with a short 0.08 out; peak end cues were "0.87 1 0.25 0.1"
(in-ramp longer than the window, so the line never reached full opacity and faded out while
fading in) → "0.85 1 0.08 0" / "0.9 1 0.06 0"; peak end headline wrapped to three lines
(.grow__tl 34rem → 40rem, .grow__end 14ch → 22ch) which pushed the sub onto the dried caps
(real contrast fail); sub now ink, 600, t-base, one line, clear of the flat lay. "1 in 3" count
made static (it counted through "1 in 0 / 1 in 1 / 1 in 2"). No dead scroll; all clips move.
Harness still reports worst 1.02:1 on the sub: it measures the bbox's empty patches, the frame
itself (lab/shots/v5-peak-end.png) is clean.

## Round 16 (2026-09-06): peak rebuilt, capsule page, brain rail
Kevin: one word at a time as the block fruits ("the mycelium grows / turns to gold / then it
teaches you"), smoother into the capsule page, hold there longer with more on the mushrooms
(Focus 125 mg, Bliss 150 mg), and an upgraded ingredients act: a brain shaped as a mushroom with
the ingredients integrated, illumination on the benefits, all on brand.
Peak: span 3.8 → 5.4. Three growth beats use data-sc-kinetic="words" (native; words mode drops
<em>, so those lines are plain 800). Burst moved 0.78 → 0.62 (CSS swell/iris + JS spores). Iris
is now a radial-gradient mask with a 16% feather (clip-path circle was a hard edge) opening over
~0.14 of the act, plus an opacity ramp. Capsule page = three beats on the flat lay: "dried whole,
ground whole." / "125 mg of magic." (Focus 2.0, the morning capsule…) / "150 mg of magic."
(Bliss 2.0, the evening capsule…). Copy container 48rem, grow__big at t-3xl so "then it teaches
you." is one line above the caps (harness had it 2.32:1 over the flush at 3 lines).
Ingredients: kie seedream still, three candidates in out/brain/ (A ring of botanicals with lit
folds, B botanicals growing out of the organism, C overhead flat lay). A wired as the rail's
opening panel `.rail__hero` (assets/04-brain.webp, 72rem × 78vh, copy in the empty cream third the
prompt asked for: "one mushroom, eighteen allies."); B kept as assets/04-brain-alt.webp. Every
spec card gets an italic "known for" line (`.spec__for`, structure/function wording only, FDA
line stays in the footer) and an illumination: a radial glow behind the specimen in the family
colour (--glow: kraft / amethyst / mix) whose opacity rides the card's existing arrival curve
(--lit). Pan span 2.3 → 2.9 for the extra panel. Assumed: 125/150 mg is per capsule. Page ~16.5vh.

## Round 16b (2026-09-06): Kevin's voice pass on the peak
"nothing extracted" cut ("Cap and stem, into the capsule."). Third beat is "then it becomes your
teacher." "gold" and "teacher" are gilded: a `.gild` class the page adds at runtime to the engine's
word-split spans (words mode is plain text, so no markup hook), gradient-clipped bronze→gold with a
light that sweeps through the letters on scroll (background-position driven by --sc-p between
--g0/--g1), soft gold drop-shadow; reduced motion = flat bronze. Gradient-text taste rule waived
by Kevin. Dose beats: "125 mg of MCRDSE mushrooms." / "150 mg of MCRDSE mushrooms." (MCRDSE in caps
per Kevin), subs "Focus 2.0. A capsule for the morning…" / "Bliss 2.0. A capsule for the rest of your
day." plus small print "Take your last one at least four hours before bed. Any later and it can keep
you up." Dose headlines at t-2xl / 18ch so they hold two lines and the small print stays off the caps.
