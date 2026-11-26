#!/usr/bin/env python3
"""Funniest Sign on a Haunted Server Room Door.

Writes a single funny sign line for the door of a haunted server
room to /output/entry.txt. Standard library only; no network,
no environment secrets, no working-directory assumptions.
"""

import os

# The sign: the haunting is not chains or cold spots — it is the
# worst help-desk user who ever lived, now with root access.
SIGN = (
    "WARNING: The ghost in Rack 4 has root access. "
    "It files tickets at 3 a.m. and has closed none since 1998."
)


def main() -> None:
    text = SIGN.strip()
    if not (1 <= len(text) <= 120):
        raise SystemExit(
            "sign must be 1-120 characters, got %d" % len(text)
        )
    if "\n" in text:
        raise SystemExit("sign must be a single line")
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8") as fh:
        fh.write(text)


if __name__ == "__main__":
    main()
