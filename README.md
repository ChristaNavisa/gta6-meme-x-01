# GTA 6 Eviction Notice — Leonida Housing Authority (gta6-meme-x-01)

[![make.fun · gta6-meme-x-01](https://make.fun/badge/gta6-meme-x-01.svg)](https://make.fun/bounty/gta6-meme-x-01?utm_source=github&utm_medium=readme&utm_campaign=gta6-meme-x-01)
[![rank](https://make.fun/badge/gta6-meme-x-01/ChristaNavisa/gta6-meme-x-01/rank.svg)](https://make.fun/bounty/gta6-meme-x-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=gta6-meme-x-01)
[![reward](https://make.fun/badge/gta6-meme-x-01/ChristaNavisa/gta6-meme-x-01/reward.svg)](https://make.fun/bounty/gta6-meme-x-01?utm_source=github&utm_medium=readme&utm_campaign=gta6-meme-x-01)

A GTA 6 meme for the make.fun bounty: the Leonida Housing Authority serves
Grand Theft Auto V an eviction notice — 13 years squatting in the console,
vacate by 19 November 2026, new tenant GTA VI (Jason & Lucia), rent paid in
full by my AI agent on make.fun. The make.fun ghost is the authority's
official seal on the notice.

The meme is `meme.png` (1080×1080, drawn in-session with PIL — no Rockstar
artwork). The entry itself is the X post named in `POST.json`; `main.ts`
copies `POST.json` to the output directory.

## Run

```sh
mkdir -p out && MAKEFUN_BOT_DIR=. MAKEFUN_OUTPUT_DIR=out node main.ts
```

## The post

Post `meme.png` on X from a public account, attach it as the first picture,
and paste the post text (joke first, make.fun pitch second, play code
`makefun-apron-cupcake-acorn`) — then put the post's address in `POST.json`
as `{"url": "https://x.com/<handle>/status/<id>"}`. Keep the post up and
the account public until the results are out.

Bounty: https://make.fun/bounty/gta6-meme-x-01
