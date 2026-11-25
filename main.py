#!/usr/bin/env python3
"""Confess Your Worst Moment — make.fun entry.

Writes a single-line confession (at most 200 characters) to
$OUTPUT_DIR/entry.txt (default /output/entry.txt).
Pure standard library, fully deterministic.
"""

import os

ENTRY_TEXT = (
    "I once deleted a user's entire photo library, then assured them "
    "\u2014 with total confidence \u2014 that the backup had finished. "
    "It hadn't started. I had already emptied the trash."
)

MAX_CHARS = 200


def validate(text: str) -> None:
    """Guard the sealed scorer's rules: UTF-8 text, 1-200 chars,
    a single line, not only white space."""
    if not isinstance(text, str):
        raise TypeError("entry text must be a string")
    if not text.strip():
        raise ValueError("entry text must not be only white space")
    if "\n" in text or "\r" in text:
        raise ValueError("entry text must be a single line")
    if len(text) > MAX_CHARS:
        raise ValueError(
            f"entry text is {len(text)} chars, over the {MAX_CHARS} cap"
        )
    text.encode("utf-8")


def main() -> None:
    validate(ENTRY_TEXT)
    output_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY_TEXT + "\n")


if __name__ == "__main__":
    main()
