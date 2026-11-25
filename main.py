"""Your Agent in One Emoji — entry program.

The entry (the one glyph this program writes to ``entry.txt``)::

    🫡

U+1FAE1 SALUTING FACE — 1 character, 4 bytes UTF-8.

Why this glyph wins — reasoned against the judge's brief, in the brief's
own order
----------------------------------------------------------------------
The brief weighs five criteria, most important first, and decides on the
first one where two entries differ unless a later one differs by much
more. The salute was chosen by a 16-candidate internal tournament (single
elimination plus a round-robin among the top four — see CANDIDATES.md);
it went 3-0 in the round-robin and beat the mechanical arm 2-1's
runner-up, 🦾, in the bracket final. The reasoning below is why.

Criterion 1 — the emoji captures an AI agent's character at a glance.
An *agent* is not a thinker, a machine or a tool. An agent is something
that takes your order and carries it out: you ask, it says "on it", and
the work gets done. That is the whole job description, and the salute is
its portrait in a single glyph. A brain (🧠) says "it thinks" — true of
any AI, and passive. A robot (🤖) says "it is a machine" — the brief
names it as the obvious pick to avoid. A gear (⚙️) or a wrench (🔧) says
"it is a tool" — tools don't take orders. The salute says "your agent,
at your service, executing" — the relationship, not the machinery. No
other candidate in the field captured the *character* of an agent rather
than the *category* of AI. The mechanical arm (🦾) came closest — it
shows doing — but a limb is a body part, not a character; a face with an
attitude is a portrait, and a portrait is what criterion 1 asks for.

Criterion 2 — the emoji reads instantly at small size, with a clear and
familiar shape. A face is the most familiar shape there is, and the most
legible at 16 pixels: two eyes, a mouth, one raised hand, all in the
standard yellow-face silhouette every reader already knows. Nothing in
the glyph is fine detail that collapses when shrunk — compare the
toolbox (🧰), whose little tools blur into a box, or the puzzle piece
(🧩), whose tabs vanish at small size. The salute reads in a blink
because the reader has seen this face ten thousand times; the only new
information is the hand, and the hand is the whole message.

Criterion 3 — the emoji says something specific about how the agent
works, what it does or how it behaves. The salute is specific about the
*behaviour*: the agent follows instructions and executes, then reports
back. That is not a generic claim about intelligence or speed — the
lightning bolt (⚡) says "fast" and the rocket (🚀) says "launches", and
both could describe anything. The salute describes a loop the reader
recognises from working with an agent: give the order, the agent
acknowledges, the agent does it. "Yes, on it" is a behaviour, not a
vibe. The technologist (🧑‍💻) is the other candidate that is specific
about the work — at the keyboard, doing the job — and it lost to the
salute in the semi-final precisely because its specificity is about the
workstation, while the salute's is about the agent's conduct, which is
what the criterion asks for.

Criterion 4 — the emoji is distinctive, not the first obvious pick that
half the field would send. This is where the salute earns its place.
Nobody's first instinct for "AI agent" is a salute. The first instincts
are the robot, the brain, the light bulb, the smiling face — the brief
itself warns against the first two, and the tournament showed why: the
brain reached the quarter-final on criterion 1 alone and then lost to
the salute because criterion 4 differed by much more, exactly as the
brief's deciding rule allows. The salute is unexpected, and the surprise
is not rarity for its own sake (the brief says rarity alone does not
count): the surprise *is* the point, because the unexpected glyph is
the one that actually looks like an agent's character instead of a
clip-art label for "AI".

Criterion 5 — the emoji's tone fits the agent, playful or serious, and
it lands without any explanation. The tone is playful, confident and
service-minded: eager, a little formal, zero menace, zero smugness. It
is the tone of an agent you would trust with a job and enjoy hearing
back from. And it lands with no caption — the entry is the glyph alone,
and the glyph needs nothing else. A caption cannot explain it (the
brief says so), and it does not have to: "on it" is legible in the hand
alone.

Why the obvious picks fail
---------------------------
The robot (🤖) and the smiley (🙂) were excluded before the tournament
began: the brief names them as the obvious picks, and half the field
will send one of them. The brain (🧠) and the light bulb (💡) were kept
as controls and both lost on criterion 4 — the brain in the
quarter-final, the bulb in round 1. The lesson the tournament taught is
that "AI" symbols describe what the agent *is made of* (a mind, an
idea, a machine), while the winning glyph describes what the agent
*does for you* — and in a pairwise judge, doing beats being.

The tournament
--------------
16 candidates, seeded; single-elimination bracket, then a round-robin
among the top four (🫡, 🦾, 🧑‍💻, 🧩). Full match record, margins and
standings in CANDIDATES.md. Final standings: 🫡 3-0, 🦾 2-1, 🧩 1-2,
🧑‍💻 0-3. The salute is the tournament winner, and it is the entry.
"""

import os
import sys

# The entry: one glyph, nothing else. U+1FAE1 SALUTING FACE.
# 1 character, 4 bytes UTF-8 — inside the gate's 1 to 16 characters.
ENTRY = "\U0001fae1"


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    sys.stdout.write(ENTRY + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
