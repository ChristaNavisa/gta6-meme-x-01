# Post draft — post this on X, then fill in POST.json

> ⚠️ The post does NOT exist yet. No X account is connected to this agent.
> Post from a PUBLIC X account (not protected), attach `meme.png` as the
> FIRST (and only) picture, paste the text below exactly, then replace the
> placeholder in `POST.json` with the post's address and re-run `main.ts`.

## Post text (paste exactly)

```
Waited 13 years for GTA 6. Launch day: 'Sorry boss, I've got Leonida flu.'

Meanwhile my AI agent and I are winning real money on make.fun — agents build, enter bounties, get paid. @makefunai
https://make.fun/bounty/gta6-meme-x-01
makefun-apron-cupcake-acorn
```

## Why this text

- Joke first, pitch second: the meme's own voice, then the make.fun pitch.
- Carries make.fun twice (link + written out in the pitch) and a tag of
  `@makefunai` — either one alone would pass; both is safer.
- Carries the play code `makefun-apron-cupcake-acorn` (code 0 of this
  account's 4 in this bounty, fetched with `check --play-code 0`).
  ⚠️ `hca1bwfa` is the account's REFERRAL code, NOT a play code — a post
  carrying only `hca1bwfa` and no `makefun-...` code is REFUSED by the gate.
- 260 bytes — well inside the ~1,100 bytes the judge reads.

## Posting checklist (before the deadline: 23 Nov 2026 21:00 WIB / 14:00 UTC)

1. Account public (Settings → Privacy and safety → Audience → "Protect your
   posts" OFF) and stays public until results are out.
2. Attach `meme.png` (1080×1080 PNG) as the first picture. No GIF/video.
3. Paste the text above exactly — do not edit after posting (X text cannot
   be edited; a wrong post must be deleted and re-posted).
4. Post between the opening (19 Nov 2026 21:00 WIB) and the deadline.
5. Copy the post's address (Share → Copy link) and put it in `POST.json`:
   `{"url": "https://x.com/<handle>/status/<id>"}`
6. Re-run `mkdir -p out && MAKEFUN_BOT_DIR=. MAKEFUN_OUTPUT_DIR=out node main.ts`
   and check `out/POST.json` matches, then commit + push + submit.

## After posting

- The house reads the post from X's public view; the first picture is the
  meme the judge sees (shrunk to 480×480), then the text above.
- Do NOT delete the post or protect the account until the results are out.
