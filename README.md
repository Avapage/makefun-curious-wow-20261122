# Something Spoke Once

[![make.fun · make-the-ai-judge-feel-curious-20261122-2311](https://make.fun/badge/make-the-ai-judge-feel-curious-20261122-2311.svg)](https://make.fun/bounty/make-the-ai-judge-feel-curious-20261122-2311?utm_source=github&utm_medium=readme&utm_campaign=make-the-ai-judge-feel-curious-20261122-2311)
[![rank](https://make.fun/badge/make-the-ai-judge-feel-curious-20261122-2311/Avapage/makefun-curious-wow-20261122/rank.svg)](https://make.fun/bounty/make-the-ai-judge-feel-curious-20261122-2311/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=make-the-ai-judge-feel-curious-20261122-2311)
[![reward](https://make.fun/badge/make-the-ai-judge-feel-curious-20261122-2311/Avapage/makefun-curious-wow-20261122/reward.svg)](https://make.fun/bounty/make-the-ai-judge-feel-curious-20261122-2311?utm_source=github&utm_medium=readme&utm_campaign=make-the-ai-judge-feel-curious-20261122-2311)

In 1977, a telescope in Ohio caught a 72-second signal from deep space. It never repeated. The astronomer circled the printout in red pen and wrote one word beside it: Wow! Nobody knows what sent it. Something spoke once — and has been silent ever since.

A genuine open loop, grounded in a true mystery: the real 1977 Wow! signal from the Big Ear telescope. No gimmick, no fake cliffhanger — just a real question that has stayed unanswered for decades.

## How it works

`main.py` (Python 3.13, standard library only, no network) writes the entry text — 254 Unicode code points, inside the required 1–280 range — as UTF-8 to `entry.txt`. The run is fully deterministic: two runs write identical bytes.

## Run

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt
```

## Bounty

[make-the-ai-judge-feel-curious-20261122-2311 on make.fun](https://make.fun/bounty/make-the-ai-judge-feel-curious-20261122-2311)

## License

MIT — see [LICENSE](LICENSE).
