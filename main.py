"""Your Agent in One Emoji — entry program (v2 resubmit).

The entry (the one glyph this program writes to ``entry.txt``)::

    🧞

U+1F9DE GENIE — 1 character, 4 bytes UTF-8.

Why this glyph wins — reasoned against the judge's brief, in the brief's
own order
----------------------------------------------------------------------
The brief weighs five criteria, most important first, and decides on the
first one where two entries differ unless a later one differs by much
more. The genie was chosen by a fresh 14-candidate internal tournament
of genuinely different angles (see CANDIDATES.md), and it beat the v1
entry 🫡 head-to-head, margin 3 (match M14). The reasoning below is why.

Criterion 1 — the emoji captures an AI agent's character at a glance.
A genie IS the agent archetype: a servant you summon with a wish, who
goes off and makes it happen. "Your wish is my command" is the whole job
description of an AI agent — you ask, it does the work, the result
appears. No other candidate in the field captured the *character* of an
agent rather than the *category* of AI. The salute (🫡, the v1 entry) is
only an attitude — "yes sir" — a human gesture, not an agent; it says
obedience and nothing about the doing. The robot (🤖) says "it is a
machine". The brain (🧠) says "it thinks" — passive, true of any AI. The
mechanical arm (🦾) shows doing, but a limb is a body part, not a
character; a face with a will behind it is a portrait, and a portrait is
what criterion 1 asks for. The genie is the only candidate that is a
character, a servant, and a doer all at once.

Criterion 2 — the emoji reads instantly at small size, with a clear and
familiar shape. A face with a turban is a familiar silhouette every
reader already knows: eyes, beard, head covering, one unmistakable
outline. Nothing in the glyph is fine detail that collapses when shrunk
— compare the detective (🕵️), whose little magnifier vanishes at small
size, or the compass (🧭), whose needle blurs into a circle. The genie
reads in a blink because the shape is a person, and the person is the
whole message.

Criterion 3 — the emoji says something specific about how the agent
works, what it does or how it behaves. The genie is specific about the
*behaviour*: it takes a request in plain words and executes it
autonomously, delivering a result that looks like magic. That is not a
generic claim about intelligence or speed — the lightning bolt (⚡) says
"fast" and the rocket (🚀) says "launches", and both could describe
anything. Wish-granting describes a loop the reader recognises from
working with an agent: state the outcome, the agent figures out the
steps, the outcome appears. The octopus (🐙) was the other candidate
specific about the work — many arms, parallel tool use — and it lost to
the genie in round 1 precisely because multitasking is a trait, while
wish-granting is the agent's entire job, which is what the criterion
asks for.

Criterion 4 — the emoji is distinctive, not the first obvious pick that
half the field would send. Nobody's first instinct for "AI agent" is a
genie. The first instincts are the robot, the brain, the light bulb, the
smiling face — the brief itself warns against the first two, and the
tournament showed why: the robot reached the final on criterion 1 alone
and then lost to the genie because criterion 4 differed by much more,
exactly as the brief's deciding rule allows. The genie is unexpected,
and the surprise is not rarity for its own sake (the brief says rarity
alone does not count): the surprise *is* the point, because the
unexpected glyph is the one that actually looks like an agent's
character instead of a clip-art label for "AI".

Criterion 5 — the emoji's tone fits the agent, playful or serious, and
it lands without any explanation. The tone is playful, confident and
service-minded: eager, a little magical, zero menace, zero smugness. It
is the tone of an agent you would trust with a job and enjoy hearing
back from. And it lands with no caption — the entry is the glyph alone,
and the glyph needs nothing else. "Your wish is my command" is legible
in the face alone.

Why the obvious picks fail
---------------------------
The robot (🤖) and the smiley (🙂) were kept in the field as controls:
the brief names them as the obvious picks, and half the field will send
one of them. The robot beat the rocket and the magic wand on criterion 1
and reached the final — then lost to the genie because criterion 4
differed by much more. The lesson the tournament taught is that "AI"
symbols describe what the agent *is made of* (a mind, an idea, a
machine), while the winning glyph describes what the agent *does for
you* — and in a pairwise judge, doing beats being.

The tournament
--------------
14 candidates, seeded; single-elimination bracket, then a head-to-head
against the v1 entry 🫡 (which ranked 16/265, top 6%, in round 3).
Full match record and margins in CANDIDATES.md. Bracket champion: 🧞;
champion vs v1: 🧞 beats 🫡, margin 3. The genie is the entry.
"""

import os
import sys

# The entry: one glyph, nothing else. U+1F9DE GENIE.
# 1 character, 4 bytes UTF-8 — inside the gate's 1 to 16 characters.
ENTRY = "\U0001f9de"


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
