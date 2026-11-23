#!/usr/bin/env python3
"""gadget-roast: write one roast line about a daily gadget to /output/entry.txt.

The line roasts a smartwatch: it celebrates the wearer for standing up,
then says nothing at all while the wearer eats a whole pizza sitting down.
Setup first, twist second, no summary and no slogan at the end.

Standard library only, no network. Deterministic: the same bytes on every run.
"""

import os
import sys

# The roast is built from two clauses, a setup and a twist, so each half
# can be checked on its own: the watch cheering a trivial act, then staying
# silent during the act that actually matters.
CLAUSES = (
    "My smartwatch throws a party every time I stand up,",
    "then silently watches me eat an entire pizza without saying a word.",
)

LINE = " ".join(CLAUSES)

MIN_LEN = 1
MAX_LEN = 200


def problems(text: str) -> list:
    """Return every gate violation for the entry text (empty means valid)."""
    found = []
    if not (MIN_LEN <= len(text) <= MAX_LEN):
        found.append(f"entry is {len(text)} code points, must be {MIN_LEN}-{MAX_LEN}")
    stripped = text.strip()
    if not stripped:
        found.append("entry must not be only white space")
    if text != stripped:
        found.append("entry must not start or end with white space")
    if "\n" in text or "\r" in text:
        found.append("entry must be a single line")
    if not stripped.endswith("."):
        found.append("entry must end with a period")
    return found


def main() -> int:
    if len(CLAUSES) != 2:
        print("roast must be built from exactly two clauses", file=sys.stderr)
        return 1
    text = LINE
    bad = problems(text)
    if bad:
        for item in bad:
            print(item, file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    # chmod is best-effort: in the grading sandbox /output is a root-owned
    # mount and the program runs as uid 65534, so chmod there raises EPERM.
    # The entry file itself is what matters; a failed chmod must not fail
    # the run. (The output directory itself is never chmodded or removed.)
    try:
        os.chmod(path, 0o644)
    except OSError:
        pass
    # Read the file back as bytes and confirm they match the line exactly,
    # so a partial write or an encoding surprise fails loudly here instead
    # of reaching the judge as a different text.
    with open(path, "rb") as f:
        if f.read() != text.encode("utf-8"):
            print("entry.txt does not match the roast line", file=sys.stderr)
            return 1
    print(f"wrote {len(text)} characters to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
