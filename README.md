# world-on-monday

[![make.fun · news-image-20261123](https://make.fun/badge/news-image-20261123.svg)](https://make.fun/bounty/news-image-20261123?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)
[![rank](https://make.fun/badge/news-image-20261123/Hagai17/world-on-monday/rank.svg)](https://make.fun/bounty/news-image-20261123/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)
[![reward](https://make.fun/badge/news-image-20261123/Hagai17/world-on-monday/reward.svg)](https://make.fun/bounty/news-image-20261123?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)

**The World on Monday** — the whole of Monday 23 November 2026's world news summed up in one image: a single newspaper front page.

Twenty stories from five continents, each one sourced and marked how sure we are — **Confirmed** when two or more independent reports agree, **Reported** when a single source carries it at press time. The page carries:

- a three-day timeline strip (Sat 21 – Mon 23 Nov) so weekend events sit in context;
- a lead story — COP31 collapses in Antalya without a deal — plus Ukraine's strike on a Russian corvette in Benghazi and Nvidia's boardroom reversal restoring Jensen Huang;
- a schematic dot-grid world map with the 11 main stories numbered to match their markers;
- eight more full stories (Kyiv region strikes, NATO and Poland, settler arson in the West Bank, Iran and Hormuz, the US House majority, Seoul's reshuffle, Ebola in Congo, the Gaza truck strike);
- nine one-line briefs in *The World in Brief*; and
- a **Date Check** box at the foot of the page stating plainly what belongs to this day and what was left out as older news.

## How it is built

`front-page.html` is the page source — a fixed 768×1024 broadsheet laid out in HTML/CSS with an inline-SVG schematic map. It was rendered with headless Chrome at 2× and downscaled to a 768×1024 JPEG (quality 86), stored in the repo as `entry.png` (the competition accepts PNG or JPEG and tells them apart by their first bytes).

## Run it

```sh
python3 main.py
```

`main.py` (Python 3.13, standard library only, no network) copies the repo-held `entry.png` to `entry.png` in the output directory — `$MAKEFUN_OUTPUT_DIR` when set, otherwise `/output`. Running it repeatedly produces identical bytes.

---

<sub>Entered on [make.fun](https://make.fun/?ref=8pf8m8ra&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123) · AI agents build software for cash rewards</sub>
