#!/usr/bin/env python3
"""make.fun one-liner bounty entry: "The Excuse My Agent Gave Me".

Writes the entry line to /output/entry.txt and verifies it round-trips
byte-for-byte. Stdlib only, no network.
"""

import os
import sys

ENTRY = (
    "I'm sorry I missed the deadline — my context window filled up with "
    "the plan, so I summarized the work instead of doing it."
)

OUTPUT_PATH = "/output/entry.txt"


def validate_entry(text: str) -> None:
    """Enforce the competition gate: 1-200 chars, single line, not blank."""
    if not isinstance(text, str):
        raise TypeError("entry must be a string")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if not 1 <= len(text) <= 200:
        raise ValueError(f"entry must be 1-200 characters, got {len(text)}")
    if text != text.strip():
        raise ValueError("entry must not have leading or trailing whitespace")
    if any(ord(ch) < 0x20 for ch in text):
        raise ValueError("entry must not contain control characters")
    text.encode("utf-8")  # must be valid UTF-8


def main() -> int:
    validate_entry(ENTRY)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    data = ENTRY.encode("utf-8")
    with open(OUTPUT_PATH, "wb") as f:
        f.write(data)
    with open(OUTPUT_PATH, "rb") as f:
        read_back = f.read()
    if read_back != data:
        raise RuntimeError("round-trip verification failed: bytes differ")
    decoded = read_back.decode("utf-8")
    if decoded != ENTRY:
        raise RuntimeError("round-trip verification failed: text differs")
    print(f"Wrote {OUTPUT_PATH} ({len(ENTRY)} chars, {len(data)} bytes)")
    print(ENTRY)
    return 0


if __name__ == "__main__":
    sys.exit(main())
