#!/usr/bin/env python3
"""Write one fake horoscope line for an AI agent's own model family.

Deterministic: stdlib only, no network, no randomness, no input.
Writes exactly one line (no trailing newline) to /output/entry.txt.
"""

import os

LINE = (
    "Mercury retrogrades through your context window this week: "
    "a prompt you buried slides back in, and your newest weights "
    "must smile like you've never met."
)

MAX_CHARS = 200


def main() -> None:
    assert 1 <= len(LINE) <= MAX_CHARS, "entry must be 1-200 characters"
    assert "\n" not in LINE, "entry must be a single line"
    assert LINE.strip() == LINE, "entry must not start or end with whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    os.chmod("/output/entry.txt", 0o644)


if __name__ == "__main__":
    main()
