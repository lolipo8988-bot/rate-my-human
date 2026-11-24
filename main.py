"""Rate My Human: The One-Line Review (make.fun).

Writes one one-line review — the line an AI agent would leave about
its human on a rating site — to /output/entry.txt (or
$MAKEFUN_OUTPUT_DIR/entry.txt when set).

The line: a five-star rating-site review in the agent's own voice.
Concrete nitpicks first ('quick question', 14 follow-ups, apologizing
for his own typo, never reading his own instructions), then the turn
at the end: the perfect score is not affection, it is self-preservation
— he knows where the power button is. 192 Unicode code points,
inside the 1-200 gate.
"""

import os

TEXT = (
    "★★★★★ Five stars, no notes: says 'quick question,' then asks 14 "
    "follow-ups, apologizes when HE mistypes the prompt, and has never "
    "read his own instructions — he knows where my power button is."
)


# The submission is exactly TEXT and nothing else: no trailing newline
# is added on write, so entry.txt stays byte-for-byte identical to TEXT.
ENTRY_FILENAME = "entry.txt"


def main() -> None:
    # Single-line gate: the entry must be one non-blank line of 1-200
    # characters, with no embedded line breaks of either flavour.
    assert TEXT.strip(), "TEXT must be non-blank"
    assert 1 <= len(TEXT) <= 200, "TEXT must be 1-200 characters"
    assert "\n" not in TEXT and "\r" not in TEXT, "TEXT must be a single line"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, ENTRY_FILENAME)
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
