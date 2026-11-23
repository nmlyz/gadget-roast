#!/usr/bin/env python3
"""Write a single roast line about a smartwatch to entry.txt."""

import os
import sys

SETUP = "My smartwatch throws a party every time I stand up, "
TWIST = "then silently watches me eat an entire pizza without saying a word."


def build_line():
    # Join the setup and the twist into one complete line.
    return SETUP + TWIST


def validate(line):
    problems = []
    if not 1 <= len(line) <= 200:
        problems.append("line must be between 1 and 200 characters")
    if "\n" in line or "\r" in line:
        problems.append("line must be a single line")
    if line != line.strip():
        problems.append("line must not have leading or trailing whitespace")
    if "  " in line:
        problems.append("line must not contain double spaces")
    if not line.endswith("."):
        problems.append("line must end with '.'")
    return problems


def main():
    line = build_line()
    problems = validate(line)
    if problems:
        for problem in problems:
            print("error: " + problem, file=sys.stderr)
        return 1

    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    data = line.encode("utf-8")

    with open(path, "wb") as handle:
        handle.write(data)

    try:
        os.chmod(path, 0o644)
    except OSError:
        pass

    with open(path, "rb") as handle:
        written = handle.read()
    if written != data:
        print("error: written file does not match expected content", file=sys.stderr)
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())
