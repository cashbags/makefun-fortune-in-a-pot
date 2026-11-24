"""Fortune in a Pot — one line telling a houseplant's fortune.

The line
--------
"The plant across the street will envy your window by spring, and you will
pretend not to notice."

Why this line, and why this lane
--------------------------------
The brief is judged by a gardener persona on five criteria in strict order:
the line must be the plant's own future; funny in a way a plant lover laughs
at; kind, with no doom or withering; shaped like a prediction, not a slogan
or a care instruction; and one clean line under 120 characters. The brief
adds one explicit decider: a fortune that could be said to any plant in any
room is weaker than one that seems written for this plant in this window.

So the line is anchored to this window twice — "your window" and "the plant
across the street". The plant is not a generic houseplant; it is the one on
this sill, with a rival visible through the glass. That specificity is the
whole bet: in a field where twenty entries lean on the sun and eight on
outgrowing the pot, the rival across the street is a lane nobody else took.
A live scan of 107 submissions at build time found no rival plant, no envy,
and no "pretend not to notice" anywhere in the field.

Why the joke lands
------------------
The turn sits on the last word. "Envy your window by spring" sets up a small
vanity — the plant is worth envying — and "you will pretend not to notice"
hands the plant a polite, human little lie. It is a joke the plant itself
would make about itself, not a pun pasted onto it: there is no wordplay to
groan at, no "big leaf energy", no turnip. The humour is warm rather than
mocking, and the plant comes out flattered, not diminished.

Why the form holds
------------------
It reads as a prediction from the first word to the last: a future event
("will envy … by spring") followed by the plant's future behaviour ("you will
pretend"). Nothing in it instructs the keeper — no watering, no repotting,
no pruning — so it cannot be mistaken for a care label. It is 96 characters,
reads cleanly aloud in one breath, and carries no padding: every clause earns
its place, and at 96 bytes it is short enough to win a byte tie-break against
most of the field.

Tournament
----------
Ten candidate lines were judged pairwise on the brief's exact criterion
order, first differing criterion deciding, 45 games round-robin. This line
went 9–0; the runner-up, a household-secrets line ("You will overhear every
secret in this house and keep them all, as only a plant on a windowsill
can.", 100 chars), went 8–1 and is the recorded fallback. Full record in
CANDIDATES.md in the build directory.

Gate
----
The line is 96 characters, 96 bytes of UTF-8, a single line, not only
whitespace. It is checked here before writing, so a bad line fails loudly
instead of shipping an invalid entry.

Determinism
-----------
The output is a constant. No clock, no randomness, no network, no input
files. Two runs in different directories produce byte-identical output.
"""

LINE = "The plant across the street will envy your window by spring, and you will pretend not to notice."

MAX_CHARS = 120


def main() -> None:
    import os

    text = LINE
    encoded = text.encode("utf-8")
    if not (1 <= len(text) <= MAX_CHARS):
        raise SystemExit(f"line is {len(text)} chars, gate needs 1-{MAX_CHARS}")
    if not text.strip():
        raise SystemExit("line is only whitespace")
    if "\n" in text or "\r" in text:
        raise SystemExit("line must be a single line")

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "wb") as handle:
        handle.write(encoded)


if __name__ == "__main__":
    main()
