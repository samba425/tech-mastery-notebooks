#!/usr/bin/env python3
"""
30 Days Of — learning helper for Python, JavaScript, and React courses.

Usage:
  python3 learn.py                          # list all courses
  python3 learn.py python                   # list Python days
  python3 learn.py python 5                 # show day 5 lesson path + practice files
  python3 learn.py python 5 --open          # open lesson in editor
  python3 learn.py python 5 --browser       # open lesson in web browser
  python3 learn.py python 5 --run             # run course sample .py files
  python3 learn.py python 5 --exercise          # open your answer file in exercises/
  python3 learn.py python 5 --run-exercise    # run your answer file
  python3 learn.py javascript 2 --run         # run JS starter / sample files
  python3 learn.py react 4 --run              # npm install + npm start (React boilerplate)
  python3 learn.py plan                       # suggested learning order
"""

from __future__ import annotations

import argparse
import html as html_module
import os
import re
import subprocess
import sys
import tempfile
import webbrowser
from pathlib import Path

ROOT = Path(__file__).resolve().parent
EXERCISES = ROOT / "exercises"

COURSES = {
    "python": ROOT / "30-Days-Of-Python-master",
    "javascript": ROOT / "30-Days-Of-JavaScript-master",
    "js": ROOT / "30-Days-Of-JavaScript-master",
    "react": ROOT / "30-Days-Of-React-master",
}

DAY_DIR = re.compile(r"^(\d{2})_Day_", re.IGNORECASE)
REACT_DAY_DIR = re.compile(r"^(\d{2})_", re.IGNORECASE)


def die(msg: str, code: int = 1) -> None:
    print(f"Error: {msg}", file=sys.stderr)
    sys.exit(code)


def find_lesson_md(day_dir: Path) -> Path | None:
    """Pick the main markdown lesson file in a day folder."""
    candidates = sorted(day_dir.glob("*.md"))
    if not candidates:
        return None
    # Prefer files that are not README in subfolders
    for c in candidates:
        name = c.name.lower()
        if name in ("readme.md", "read_me.md"):
            continue
        return c
    return candidates[0]


def get_python_days() -> dict[int, dict]:
    base = COURSES["python"]
    days: dict[int, dict] = {}
    for entry in sorted(base.iterdir()):
        if not entry.is_dir():
            continue
        m = DAY_DIR.match(entry.name)
        if not m:
            continue
        day_num = int(m.group(1))
        lesson = find_lesson_md(entry)
        py_files = sorted(entry.glob("*.py"))
        if day_num == 1 and lesson is None:
            readme = base / "readme.md"
            if readme.exists():
                lesson = readme
        days[day_num] = {
            "dir": entry,
            "title": entry.name.replace("_", " "),
            "lesson": lesson,
            "practice": py_files,
            "starter": None,
            "boilerplate": None,
        }
    return dict(sorted(days.items()))


def get_javascript_days() -> dict[int, dict]:
    base = COURSES["javascript"]
    days: dict[int, dict] = {}
    for entry in sorted(base.iterdir()):
        if not entry.is_dir():
            continue
        m = DAY_DIR.match(entry.name)
        if not m:
            continue
        day_num = int(m.group(1))
        lesson = find_lesson_md(entry)
        starter = entry / f"{m.group(1)}_day_starter"
        if not starter.exists():
            starter = next(entry.glob("*_day_starter"), None)
        js_samples = sorted(entry.glob("*.js"))
        if day_num == 1 and lesson is None:
            readme = base / "readMe.md"
            if readme.exists():
                lesson = readme
        days[day_num] = {
            "dir": entry,
            "title": entry.name.replace("_", " "),
            "lesson": lesson,
            "practice": js_samples,
            "starter": starter if starter and starter.exists() else None,
            "boilerplate": None,
        }
    return dict(sorted(days.items()))


def get_react_days() -> dict[int, dict]:
    base = COURSES["react"]
    days: dict[int, dict] = {}
    for entry in sorted(base.iterdir()):
        if not entry.is_dir():
            continue
        m = REACT_DAY_DIR.match(entry.name)
        if not m:
            continue
        day_num = int(m.group(1))
        if day_num == 0:
            continue
        lesson = find_lesson_md(entry)
        boilerplate = next(entry.glob("*_boilerplate"), None)
        days[day_num] = {
            "dir": entry,
            "title": entry.name.replace("_", " "),
            "lesson": lesson,
            "practice": [],
            "starter": None,
            "boilerplate": boilerplate if boilerplate and boilerplate.is_dir() else None,
        }
    readme = base / "readMe.md"
    if readme.exists():
        days.setdefault(
            0,
            {
                "dir": base,
                "title": "Introduction & Setup",
                "lesson": readme,
                "practice": [],
                "starter": None,
                "boilerplate": base / "03_Day_Setting_Up" / "03_setting_up_boilerplate",
            },
        )
    return dict(sorted(days.items()))


LOADERS = {
    "python": get_python_days,
    "javascript": get_javascript_days,
    "js": get_javascript_days,
    "react": get_react_days,
}

EXERCISE_EXT = {"python": "py", "javascript": "js", "js": "js", "react": "md"}


def exercise_path(course: str, day: int) -> Path:
    ext = EXERCISE_EXT[course if course != "js" else "javascript"]
    sub = "javascript" if course == "js" else course
    return EXERCISES / sub / f"day_{day:02d}.{ext}"


def print_course_list() -> None:
    print("\n📚 Available courses in this folder:\n")
    print("  python      — 30 Days Of Python   (read .md → write/run .py exercises)")
    print("  javascript  — 30 Days Of JavaScript (read .md → node / browser starters)")
    print("  react       — 30 Days Of React     (read .md → npm start boilerplates)\n")
    print("Examples:")
    print("  python3 learn.py python 1 --browser")
    print("  python3 learn.py python 1 --exercise")
    print("  python3 learn.py python 2 --run-exercise")
    print("  python3 learn.py javascript 3 --run")
    print("  python3 learn.py react 4 --run")
    print("  python3 learn.py plan\n")


def print_days(course: str) -> None:
    days = LOADERS[course]()
    label = course.upper()
    print(f"\n{label} — {len(days)} lesson(s):\n")
    for num, info in days.items():
        tag = ""
        if info.get("boilerplate"):
            tag = " [react app]"
        elif info.get("starter"):
            tag = " [browser starter]"
        elif info.get("practice"):
            tag = f" [{len(info['practice'])} sample file(s)]"
        print(f"  Day {num:02d}: {info['title']}{tag}")
    print()


def show_day(course: str, day: int) -> dict:
    days = LOADERS[course]()
    if day not in days:
        die(f"Day {day} not found for {course}. Use: python3 learn.py {course}")
    info = days[day]
    print(f"\n=== {course.upper()} — Day {day:02d} ===")
    print(f"Folder:  {info['dir']}")
    if info["lesson"]:
        print(f"Lesson:  {info['lesson']}")
    else:
        print("Lesson:  (no .md found — check folder manually)")
    if info["practice"]:
        print("Practice files:")
        for p in info["practice"]:
            print(f"  - {p}")
    if info.get("starter"):
        print(f"Starter: {info['starter']}")
        html = list(Path(info["starter"]).glob("index.html"))
        if html:
            print(f"  Open in browser: file://{html[0]}")
    if info.get("boilerplate"):
        print(f"React app: {info['boilerplate']}")
        print(f"  Run: python3 learn.py {course} {day} --run")
    ex = exercise_path(course if course != "js" else "javascript", day)
    if ex.exists():
        print(f"Your answers: {ex}")
    print("\nHow to practice:")
    print("  1. Read the lesson (--browser or --open)")
    print("  2. Write answers in exercises/ (--exercise)")
    print("  3. Run course samples (--run) or your file (--run-exercise)")
    print()
    return info


def open_lesson(path: Path | None) -> None:
    if not path or not path.exists():
        die("Lesson file not found")
    if sys.platform == "darwin":
        subprocess.run(["open", str(path)], check=False)
    elif sys.platform == "win32":
        os.startfile(str(path))  # type: ignore[attr-defined]
    else:
        subprocess.run(["xdg-open", str(path)], check=False)
    print(f"Opened: {path}")


def markdown_preview_html(md_path: Path) -> Path:
    """Build a readable HTML preview for a markdown lesson (images use file:// paths)."""
    content = md_path.read_text(encoding="utf-8")
    base = md_path.parent

    def fix_image(match: re.Match[str]) -> str:
        alt, src = match.group(1), match.group(2)
        if not src.startswith(("http://", "https://", "file://")):
            resolved = (base / src).resolve()
            if resolved.exists():
                src = resolved.as_uri()
        return f"![{alt}]({src})"

    content = re.sub(r"!\[([^\]]*)\]\(([^)]+)\)", fix_image, content)

    page = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{html_module.escape(md_path.stem)}</title>
  <style>
    body {{
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
      max-width: 920px; margin: 0 auto; padding: 2rem 1.25rem;
      line-height: 1.65; background: #f6f8fa; color: #1f2328;
    }}
    h1 {{ font-size: 1.1rem; color: #57606a; margin-bottom: 1rem; }}
    pre {{
      white-space: pre-wrap; word-wrap: break-word;
      font-family: "SF Mono", Menlo, Consolas, monospace; font-size: 14px;
      background: #fff; padding: 1.5rem; border-radius: 10px;
      border: 1px solid #d0d7de; box-shadow: 0 1px 3px rgba(0,0,0,.06);
    }}
  </style>
</head>
<body>
  <h1>{html_module.escape(md_path.name)}</h1>
  <pre>{html_module.escape(content)}</pre>
</body>
</html>"""
    preview_dir = EXERCISES / ".preview"
    preview_dir.mkdir(parents=True, exist_ok=True)
    out = preview_dir / f"{md_path.stem}.html"
    out.write_text(page, encoding="utf-8")
    return out


def open_in_browser(path: Path | None) -> None:
    if not path or not path.exists():
        die("File not found")
    if path.suffix.lower() == ".md":
        path = markdown_preview_html(path)
    uri = path.resolve().as_uri()
    webbrowser.open(uri)
    print(f"Opened in browser: {uri}")


def run_exercise_file(course: str, day: int) -> None:
    c = course if course != "js" else "javascript"
    path = exercise_path(c, day)
    if not path.exists():
        die(f"Exercise file not found: {path}")
    if path.suffix == ".md":
        open_lesson(path)
        print("React day notes are markdown — edit the checklist and use --run for the boilerplate app.")
        return
    print(f"\n--- running your exercise: {path.name} ---")
    runner = [sys.executable] if path.suffix == ".py" else ["node"]
    subprocess.run(runner + [str(path)], cwd=str(path.parent))


def run_python_practice(info: dict) -> None:
    files = info["practice"]
    if not files:
        print("No .py sample files for this day.")
        print("Use: python3 learn.py python <day> --run-exercise")
        return
    for f in files:
        print(f"\n--- running {f.name} ---")
        subprocess.run([sys.executable, str(f)], cwd=str(f.parent))


def run_javascript_practice(info: dict) -> None:
    starter = info.get("starter")
    if starter:
        html_files = list(Path(starter).glob("index.html"))
        main_js = list(Path(starter).glob("main.js")) + list(Path(starter).glob("scripts/main.js"))
        if main_js:
            for js in main_js:
                print(f"\n--- node {js} ---")
                subprocess.run(["node", str(js)], cwd=str(js.parent))
        if html_files:
            uri = html_files[0].resolve().as_uri()
            print(f"\nOpening browser starter: {uri}")
            webbrowser.open(uri)
            return
    files = info["practice"]
    if not files:
        print("No JS files found. Open the lesson and use Chrome DevTools console.")
        return
    for f in files[:5]:  # avoid flooding terminal on days with many demos
        print(f"\n--- node {f.name} ---")
        subprocess.run(["node", str(f)], cwd=str(f.parent))
    if len(files) > 5:
        print(f"\n... and {len(files) - 5} more .js demos in {info['dir']}")


def run_react_app(info: dict) -> None:
    boilerplate = info.get("boilerplate")
    if not boilerplate or not Path(boilerplate).exists():
        print("No React boilerplate for this day.")
        if info["lesson"]:
            print("This day is theory-only — read the lesson and do exercises in markdown.")
        return
    bp = Path(boilerplate)
    node_modules = bp / "node_modules"
    if not node_modules.exists():
        print(f"Installing dependencies in {bp} ...")
        subprocess.run(["npm", "install"], cwd=str(bp), check=True)
    print(f"\nStarting React dev server from {bp}")
    print("Press Ctrl+C to stop.\n")
    subprocess.run(["npm", "start"], cwd=str(bp))


def print_plan() -> None:
    print(
        """
🗓️  Suggested learning path (Samba's 30 Days series)

Order:  Python → JavaScript → React

Why this order?
  • Python builds programming fundamentals (variables, loops, functions, OOP)
  • JavaScript adds web basics (DOM, async, browser APIs)
  • React assumes solid JavaScript — Day 1 of React is a JS refresher

Daily routine (~1–2 hours):
  ┌─────────────────────────────────────────────────────────────┐
  │ 1. Read today's .md lesson (15–30 min)                      │
  │ 2. Type every code example — don't copy-paste               │
  │ 3. Complete Level 1 exercises, then Level 2                 │
  │ 4. Run practice code: python3 learn.py <course> <day> --run │
  │ 5. Save work in exercises/ (--exercise / --run-exercise)   │
  └─────────────────────────────────────────────────────────────┘

Course specifics:
  PYTHON (Days 1–30)
    • Answers: exercises/python/day_XX.py
    • Run yours: python3 learn.py python <day> --run-exercise
    • Days 23+: virtual env, pip install packages as lessons say

  JAVASCRIPT (Days 1–30)
    • Run:  python3 learn.py javascript <day> --run
    • Days 1–20: Node.js for .js files
    • Days 21+: open *_day_starter/index.html in Chrome
    • Use DevTools console (F12) for quick experiments

  REACT (Days 1–30)
    • Needs Node.js + npm
    • Days 1–2: JavaScript refresher (no app yet)
    • Day 3+: python3 learn.py react <day> --run
    • Each boilerplate runs at http://localhost:3000

Quick start today:
  python3 learn.py python 1 --open
  python3 learn.py python 1 --run
"""
    )


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Learn and practice 30 Days Of Python / JavaScript / React",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    parser.add_argument("course", nargs="?", help="python | javascript | react | plan")
    parser.add_argument("day", nargs="?", type=int, help="Day number (1–30)")
    parser.add_argument("--open", action="store_true", help="Open lesson in editor")
    parser.add_argument("--browser", action="store_true", help="Open lesson in web browser")
    parser.add_argument("--exercise", action="store_true", help="Open your answer file in exercises/")
    parser.add_argument("--run", action="store_true", help="Run course sample code / React dev server")
    parser.add_argument("--run-exercise", action="store_true", help="Run your answer file in exercises/")
    args = parser.parse_args()

    if not args.course:
        print_course_list()
        return

    if args.course == "plan":
        print_plan()
        return

    course = args.course.lower()
    if course not in LOADERS:
        die(f"Unknown course '{args.course}'. Choose: python, javascript, react")

    if not COURSES[course if course != "js" else "javascript"].exists():
        die(f"Course folder missing: {COURSES[course if course != 'js' else 'javascript']}")

    if args.day is None:
        print_days(course)
        return

    info = show_day(course, args.day)

    if args.open and info.get("lesson"):
        open_lesson(info["lesson"])

    if args.browser:
        if info.get("starter"):
            html_files = list(Path(info["starter"]).glob("index.html"))
            if html_files:
                open_in_browser(html_files[0])
            elif info.get("lesson"):
                open_in_browser(info["lesson"])
        elif info.get("lesson"):
            open_in_browser(info["lesson"])
        else:
            die("Nothing to open in browser for this day")

    if args.exercise:
        open_lesson(exercise_path(course if course != "js" else "javascript", args.day))

    if args.run_exercise:
        run_exercise_file(course, args.day)

    if args.run:
        if course in ("python",):
            run_python_practice(info)
        elif course in ("javascript", "js"):
            run_javascript_practice(info)
        elif course == "react":
            run_react_app(info)


if __name__ == "__main__":
    main()
