#!/usr/bin/env python3
"""Build only Vedic_Maths_Childrens_Worksheets.pdf (same as generate_book.py --only worksheets)."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import generate_book  # noqa: E402

if __name__ == "__main__":
    sys.argv = [sys.argv[0], "--only", "worksheets"]
    generate_book.main()
