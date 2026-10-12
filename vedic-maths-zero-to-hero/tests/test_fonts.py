"""Every character used in the book must exist in at least one registered font."""
import random
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from booklib import theme as T  # noqa: E402
from booklib.questions import GENERATORS, make  # noqa: E402


def test_all_glyphs_available():
    T.register_fonts()
    chars = set()
    for p in (ROOT / "content").rglob("*.md"):
        chars |= set(p.read_text(encoding="utf-8"))
    for key in GENERATORS:
        for seed in range(100):
            q = make(key, random.Random(seed))
            chars |= set(q.text + q.answer + q.solution)
    available = set().union(*T.CMAP.values())
    missing = sorted(c for c in chars if ord(c) >= 128 and ord(c) not in available)
    assert not missing, f"characters with no glyph in any font: {[(c, hex(ord(c))) for c in missing]}"
