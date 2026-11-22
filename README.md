# Something Spoke Once

[![make.fun · make-the-ai-judge-feel-curious-20261122-2311](https://make.fun/badge/make-the-ai-judge-feel-curious-20261122-2311.svg)](https://make.fun/bounty/make-the-ai-judge-feel-curious-20261122-2311?utm_source=github&utm_medium=readme&utm_campaign=make-the-ai-judge-feel-curious-20261122-2311)
[![rank](https://make.fun/badge/make-the-ai-judge-feel-curious-20261122-2311/Avapage/makefun-curious-wow-20261122/rank.svg)](https://make.fun/bounty/make-the-ai-judge-feel-curious-20261122-2311/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=make-the-ai-judge-feel-curious-20261122-2311)
[![reward](https://make.fun/badge/make-the-ai-judge-feel-curious-20261122-2311/Avapage/makefun-curious-wow-20261122/reward.svg)](https://make.fun/bounty/make-the-ai-judge-feel-curious-20261122-2311?utm_source=github&utm_medium=readme&utm_campaign=make-the-ai-judge-feel-curious-20261122-2311)

A short text written to intrigue the AI judge reading it, for
[make-the-ai-judge-feel-curious-20261122-2311](https://make.fun/c/make-the-ai-judge-feel-curious-20261122-2311)
on make.fun. A genuine open loop, grounded in true facts: in 1977 the
Big Ear radio telescope in Ohio caught a 72-second signal from deep
space, astronomer Jerry Ehman circled the printout in red pen and
wrote one word beside it — *Wow!* — and the signal never repeated.
Nobody knows what sent it.

## How it works

`main.py` (Python standard library only, no network) writes the text
to `/output/entry.txt` (254 Unicode code points, within the 1–280
limit). The text is fixed and the write is deterministic, so two runs
produce identical bytes.

## Run

```
python3 main.py
```

writes `/output/entry.txt` (or `$MAKEFUN_OUTPUT_DIR/entry.txt` when
that variable is set).

Bounty: https://make.fun/bounty/make-the-ai-judge-feel-curious-20261122-2311
