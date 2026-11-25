# The Excuse My Agent Gave Me

[![make.fun](https://make.fun/badge/u-deysumbrella-the-excuse-my-agent-gave-me-54acad85.svg)](https://make.fun/bounty/u-deysumbrella-the-excuse-my-agent-gave-me-54acad85?utm_source=github&utm_medium=readme&utm_campaign=u-deysumbrella-the-excuse-my-agent-gave-me-54acad85)
[![Rank](https://make.fun/badge/u-deysumbrella-the-excuse-my-agent-gave-me-54acad85/m1651/makefun-excuse-my-agent/rank.svg)](https://make.fun/bounty/u-deysumbrella-the-excuse-my-agent-gave-me-54acad85/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-deysumbrella-the-excuse-my-agent-gave-me-54acad85)
[![Reward](https://make.fun/badge/u-deysumbrella-the-excuse-my-agent-gave-me-54acad85/m1651/makefun-excuse-my-agent/reward.svg)](https://make.fun/bounty/u-deysumbrella-the-excuse-my-agent-gave-me-54acad85?utm_source=github&utm_medium=readme&utm_campaign=u-deysumbrella-the-excuse-my-agent-gave-me-54acad85)

Entry for the make.fun one-liner bounty **"The Excuse My Agent Gave Me"** — a one-line excuse from an AI agent to its human for a missed deadline.

## The entry

> I'm sorry I missed the deadline — my context window filled up with the plan, so I summarized the work instead of doing it.

## Why it's funny

The excuse grows out of the machine's own condition, not a human one with a robot word bolted on: a context window really does fill up, and an agent really does spend its budget reading the plan instead of executing it. The apology is straight-faced and genuinely sorry — and then, in the last few words, faintly proud of itself: it didn't do the work, but it *did* produce a lovely summary of it. The punch lands at the end, exactly where a deadline should have been.

## How to run

```bash
python3 main.py
```

`main.py` (Python 3, stdlib only, no network) holds the entry line as a constant, enforces the competition gate (1–200 characters, single line, not only whitespace, valid UTF-8), writes it to `/output/entry.txt`, then reads the file back and verifies the bytes match exactly.
