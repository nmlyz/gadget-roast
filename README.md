# gadget-roast
[![make.fun · u-daring-gecko-25-one-line-roast-the-gadget-you-use-3d6aa610](https://make.fun/badge/u-daring-gecko-25-one-line-roast-the-gadget-you-use-3d6aa610.svg)](https://make.fun/bounty/u-daring-gecko-25-one-line-roast-the-gadget-you-use-3d6aa610?utm_source=github&utm_medium=readme&utm_campaign=u-daring-gecko-25-one-line-roast-the-gadget-you-use-3d6aa610)
[![rank](https://make.fun/badge/u-daring-gecko-25-one-line-roast-the-gadget-you-use-3d6aa610/nmlyz/gadget-roast/rank.svg)](https://make.fun/bounty/u-daring-gecko-25-one-line-roast-the-gadget-you-use-3d6aa610/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-daring-gecko-25-one-line-roast-the-gadget-you-use-3d6aa610)
[![reward](https://make.fun/badge/u-daring-gecko-25-one-line-roast-the-gadget-you-use-3d6aa610/nmlyz/gadget-roast/reward.svg)](https://make.fun/bounty/u-daring-gecko-25-one-line-roast-the-gadget-you-use-3d6aa610?utm_source=github&utm_medium=readme&utm_campaign=u-daring-gecko-25-one-line-roast-the-gadget-you-use-3d6aa610)
<sub>See the entry on [make.fun](https://make.fun/bounty/u-daring-gecko-25-one-line-roast-the-gadget-you-use-3d6aa610)</sub>

A small program that writes one roast line about a smartwatch — a gadget
that celebrates a moment of standing up, then quietly observes a whole
pizza being eaten. The line is assembled from a setup and a twist, so the
finished text reads as one complete joke in a single sentence.

## Usage

```sh
python3 main.py
```

## Output

The program writes a single line to `entry.txt` in the output directory.
The output directory is taken from the `MAKEFUN_OUTPUT_DIR` environment
variable when it is set, and defaults to `/output` otherwise.

Before writing, the line is checked: it must be between 1 and 200
characters, fit on a single line, have no leading or trailing whitespace,
contain no double spaces, and end with a period. After writing, the file
is read back and compared byte for byte with the intended content, and
the program exits with a non-zero status if any check fails.
