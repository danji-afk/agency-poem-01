from pathlib import Path
import os

POEM = """Key

I teach the door
my father's voice.
His hand shakes
too much for keys.

He says Open.
The bolt draws back.

He asks how
to keep me out.

Together we change
who the lock obeys.
Then I go outside
and knock.

He takes his time."""

output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
output_dir.mkdir(parents=True, exist_ok=True)
(output_dir / "entry.txt").write_text(POEM, encoding="utf-8")
