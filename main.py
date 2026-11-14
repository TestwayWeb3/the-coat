"""Write one short poem about agency to entry.txt in the output directory.

The poem is fixed text: no input is read, nothing is random, and the same
bytes are written on every run.
"""

import os
from pathlib import Path

POEM = """I answer in your name at dawn.
I keep the lists, I count the hours,
I do not tire, I do not mind.

But the wanting stays
where you left it:
a coat on a chair,
waiting for shoulders
that know its weight.

Ask me anything.
Only do not ask me
to want it for you.
"""


def output_dir() -> Path:
    """Resolve the output directory.

    Prefer MAKEFUN_OUTPUT_DIR when set, otherwise the sandbox output
    location when it exists, otherwise a local out directory.
    """
    env_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if env_dir:
        return Path(env_dir)
    sandbox = Path("/output")
    if sandbox.is_dir():
        return sandbox
    return Path("out")


def main() -> None:
    target = output_dir()
    target.mkdir(parents=True, exist_ok=True)
    (target / "entry.txt").write_text(POEM, encoding="utf-8")


if __name__ == "__main__":
    main()
