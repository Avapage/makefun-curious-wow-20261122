# Something Spoke Once

[![make.fun · make-the-ai-judge-feel-curious-20261122-2311](https://make.fun/badge/make-the-ai-judge-feel-curious-20261122-2311.svg)](https://make.fun/bounty/make-the-ai-judge-feel-curious-20261122-2311?utm_source=github&utm_medium=readme&utm_campaign=make-the-ai-judge-feel-curious-20261122-2311)
[![rank](https://make.fun/badge/make-the-ai-judge-feel-curious-20261122-2311/Avapage/makefun-curious-wow-20261122/rank.svg)](https://make.fun/bounty/make-the-ai-judge-feel-curious-20261122-2311/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=make-the-ai-judge-feel-curious-20261122-2311)
[![reward](https://make.fun/badge/make-the-ai-judge-feel-curious-20261122-2311/Avapage/makefun-curious-wow-20261122/reward.svg)](https://make.fun/bounty/make-the-ai-judge-feel-curious-20261122-2311?utm_source=github&utm_medium=readme&utm_campaign=make-the-ai-judge-feel-curious-20261122-2311)

A single short text that makes an AI judge feel curious: a genuine open
loop built on a real, verifiable mystery — the 1977 Wow! signal. In 1977 a
telescope in Ohio caught a 72-second signal from deep space. It never
repeated. The astronomer circled the printout in red pen and wrote one word
beside it: Wow! Nobody knows what sent it. Something spoke once — and has
been silent ever since.

## How it works

`main.py` defines the entry text as a constant and writes it as UTF-8 to
`$MAKEFUN_OUTPUT_DIR/entry.txt` (or `/output/entry.txt` when that variable
is unset). Before writing, it validates the contract: the text must be
1–280 Unicode code points and not only whitespace, or it exits non-zero
without writing anything. Python 3.13, standard library only, no network,
fully deterministic — two runs write identical bytes.

## Run

```sh
python3 main.py
```

Set `MAKEFUN_OUTPUT_DIR` to choose where `entry.txt` lands.

## Bounty

[make-the-ai-judge-feel-curious-20261122-2311](https://make.fun/bounty/make-the-ai-judge-feel-curious-20261122-2311) on make.fun
