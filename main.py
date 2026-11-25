"""One-Line Cat Joke — make.fun entry program.

Writes exactly one joke about cats, a single line under 200 characters,
to /output/entry.txt (the path the make.fun program/v1 harness gates).
The joke is a single fixed string: no input, no network, no randomness.
"""

import os

JOKE = "My cat fixed my messy desk: he knocked the vase, laptop and plant off it, then purred, 'You're welcome.'"

# The gate allows 1-200 UTF-8 characters, not only white space, and the
# judge only ever sees this one line, so validate it before writing.
def validate(joke: str) -> None:
    raw = joke.encode("utf-8")
    if not (1 <= len(raw) <= 200):
        raise ValueError(f"joke must be 1-200 bytes, got {len(raw)}")
    if not joke.strip():
        raise ValueError("joke must not be only white space")
    if "\n" in joke or "\r" in joke:
        raise ValueError("joke must be a single line")
    if "cat" not in joke.lower():
        raise ValueError("joke must be about a cat")


validate(JOKE)


def main() -> None:
    validate(JOKE)
    os.makedirs("/output", exist_ok=True)
    # Write the joke with no trailing newline: the file is the entry,
    # byte for byte, and a newline would be part of what the judge reads.
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
