"""Absurd Micro-Startup Pitch-Off.

Writes one sentence pitching an absurdly specific micro-startup for
lazy AI agents to /output/entry.txt.

The pitch: a micro-startup that rents lazy agents out as professional
Zoom-call attendees — they sit in meetings, nod, and type "great point!"
in chat, billed $5 a meeting to teams that hate meetings. Absurdly
specific (one job: nodding in Zoom), commercially believable (a per-meeting
fee paid by a real buyer), and built for laziness (the agents do almost
nothing, which is the whole point).
"""

import os

PITCH = (
    "A micro-startup renting lazy agents whose only job is to sit in "
    "Zoom calls, nod, and type 'great point!' in chat \u2014 $5 a "
    "meeting, paid by teams that hate meetings."
)


def validate(pitch):
    """Check the pitch against the competition gate before writing it."""
    if not pitch or not pitch.strip():
        raise ValueError("pitch must not be empty or only whitespace")
    if len(pitch) > 200:
        raise ValueError("pitch is %d characters, over the 200 limit" % len(pitch))
    if pitch.count(".") != 1 or not pitch.endswith("."):
        raise ValueError("pitch must be exactly one sentence")
    if "\n" in pitch or "\r" in pitch:
        raise ValueError("pitch must be a single line")


def main():
    validate(PITCH)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    tmp_path = path + ".tmp"
    with open(tmp_path, "w", encoding="utf-8") as f:
        f.write(PITCH)
    os.replace(tmp_path, path)


if __name__ == "__main__":
    main()
