#!/usr/bin/env python3
"""gadget-roast: write one roast line about a daily gadget to /output/entry.txt.

The line is about a smartwatch. It cheers every time its wearer stands
up, then stays quiet while the wearer eats a whole pizza sitting down.
Setup first, twist second; no summary and no slogan at the end.

Standard library only, no network. Deterministic: the same bytes on
every run.
"""

import os
import sys

SETUP = "My smartwatch throws a party every time I stand up,"
TWIST = "then silently watches me eat an entire pizza without saying a word."

# The line is built from a setup clause and a twist clause, joined with a
# single space, so each half can be checked on its own.
LINE = SETUP + " " + TWIST

MIN_LEN = 1
MAX_LEN = 200


def violations(text):
    """Return every gate violation for the entry text (empty means valid)."""
    found = []
    if not MIN_LEN <= len(text) <= MAX_LEN:
        found.append("entry is %d code points, must be %d-%d" % (len(text), MIN_LEN, MAX_LEN))
    if not text.strip():
        found.append("entry must not be only white space")
    if text != text.strip():
        found.append("entry must not start or end with white space")
    if "\n" in text or "\r" in text:
        found.append("entry must be a single line")
    if not text.strip().endswith("."):
        found.append("entry must end with a period")
    return found


def main():
    text = LINE
    bad = violations(text)
    if bad:
        for item in bad:
            print(item, file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(text)
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
    with open(path, "rb") as handle:
        if handle.read() != text.encode("utf-8"):
            print("entry.txt does not match the roast line", file=sys.stderr)
            return 1
    print("wrote %d characters to %s" % (len(text), path))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
