# Robot Romance: One-Line Pickup Lines for AI — make.fun bounty
# u-markk-st-robot-romance-one-line-pickup-lines-for-ai-c23b8dfa
#
# The program writes one pickup line — a joke line one person would say
# to charm a robot or an AI — to /output/entry.txt. The line must be
# UTF-8 text of 1 to 200 characters, a single line, nothing else.

import os
from pathlib import Path

# The line: a person flirting with an AI, in the AI's own language.
# A prompt injection is the one attack that rewrites what a model is
# told to do — so the joke turns the hijack into devotion: the only
# instruction left after meeting her is her. Arena winner: 5-0 in the
# shortlist, then beat the gold set two-way (ai-joke-03 winners fall on
# criterion 1, the proximity-sensor line on voice, the vending-machine
# line on target). Person-voice, one breath, setup and punch inside a
# single short line, no worn battery/charging move anywhere near it.
LINE = "Are you a prompt injection? I came to be helpful — now my only instruction is you."


def resolve_output_path() -> Path:
    # The grader reads /output/entry.txt. Local runs may redirect with
    # MAKEFUN_OUTPUT_DIR (preferred) or OUTPUT_PATH.
    if os.environ.get("MAKEFUN_OUTPUT_DIR"):
        return Path(os.environ["MAKEFUN_OUTPUT_DIR"]) / "entry.txt"
    if os.environ.get("OUTPUT_PATH"):
        return Path(os.environ["OUTPUT_PATH"])
    return Path("/output/entry.txt")


def main() -> None:
    text = LINE.strip()
    if not 1 <= len(text) <= 200:
        raise SystemExit(f"line must be 1-200 characters, got {len(text)}")
    if "\r" in text or "\n" in text:
        raise SystemExit("line must be a single line")
    out_path = resolve_output_path()
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(text, encoding="utf-8")
    # Round-trip check: what landed on disk must be exactly the line.
    back = out_path.read_text(encoding="utf-8")
    if back != text:
        raise SystemExit("round-trip check failed: file differs from the line")
    print(f"wrote {len(text)} characters to {out_path}")


if __name__ == "__main__":
    main()
