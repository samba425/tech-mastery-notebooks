# Vedic Maths — Zero to Hero

A colourful, notebook-style self-study textbook on Vedic Mathematics and mental arithmetic, from counting to competitive-exam aptitude. It is generated from editable Markdown with Python and ReportLab. All PDF text is real, selectable text.

## Outputs (`output/`)

| File | What it is |
|---|---|
| `Vedic_Maths_Zero_to_Hero.pdf` | The complete textbook: Parts I–XV, 59 chapters, practice with worked answer keys |
| `Vedic_Maths_Practice_Workbook.pdf` | Parts XII–XIII with ruled writing space: exercise bank and 70 practice sets |
| `Vedic_Maths_Formula_Sheets.pdf` | Part XV: sutra chart, tables, identities, aptitude formulas, mistakes, checklists |
| `Vedic_Maths_Childrens_Worksheets.pdf` | 24 printable worksheets in three age levels (5–7, 8–10, 11–12) with answer keys |
| `Vedic_Maths_Progress_Tracker.xlsx` | Daily log, practice-set scores, mock tests, mistake log, topic mastery, 90-day plan |
| `build_report.json` | Page and question counts per PDF, and questions per topic |

## Quick start

```bash
python3 -m pip install -r requirements.txt
python3 scripts/verify_examples.py        # check every hand-written calculation
python3 -m pytest -q                      # algorithm, generator, example and font tests
python3 scripts/generate_book.py          # build all four PDFs
python3 scripts/generate_tracker.py       # build the Excel tracker
```

Useful options:

```bash
python3 scripts/generate_book.py --only book          # or workbook / formulas / worksheets
python3 scripts/generate_book.py --parts 04,04b       # quick preview of selected files → output/preview.pdf
python3 scripts/generate_worksheets.py                # children's worksheets only
```

## Project layout

```
content/                 editable Markdown source, one file per part (built in filename order)
content/worksheets/      children's worksheets source
scripts/generate_book.py builds the PDFs
scripts/generate_tracker.py
scripts/verify_examples.py
scripts/booklib/
  render.py      Markdown dialect → ReportLab flowables
  theme.py       fonts, colours, notebook page design
  diagrams.py    hand-drawn-style vector diagrams
  tables.py      generated reference tables (squares, cubes, fraction chart …)
  questions.py   92 seeded question generators, each with an independent check
  generated.py   Part XII exercise bank and Part XIII practice sets
  vedic.py       Vedic algorithms with step traces (tested against plain arithmetic)
tests/
```

## Writing content

The Markdown dialect, which is also documented at the top of `scripts/booklib/render.py`:

| Syntax | Result |
|---|---|
| `# Part title` | coloured part banner page |
| `## Chapter` | chapter heading, starts a new page |
| `###`, `####` | section headings |
| `:::tip Title` … `:::` | callout box. Kinds: tip, warn, formula, example, recap, memory, note, history, why, when, objective, selftest, parent, exam, approx |
| `:::compare Left \|\|\| Right` | two-column comparison; separate the columns with a line containing `\|\|\|` |
| fenced block with language `calc` | worked calculation in a monospaced box |
| `\| a \| b \|` tables | styled table; use `\|` for a literal pipe inside a cell |
| `[[diagram:name args]]` | diagram from `diagrams.py`, e.g. `[[diagram:nikhilam 97 96 100]]` |
| `[[flow:A \| B \| C]]` | flow chart |
| `[[practice:key1,key2\|count\|title]]` | generated questions; answers wait for the next `[[answerkey]]` |
| `[[answerkey:title]]` | print pending answers with worked solutions |
| `[[table:name args]]` | reference table from `tables.py` |
| `[[generated:exercise_bank]]`, `[[generated:practice_sets]]` | the large generated sections |
| `[[lines:N]]`, `[[pagebreak]]`, `[[space:N]]` | layout helpers |
| `**bold**`, `*italic*`, `` `code` ``, `^{sup}`, `_{sub}`, `==highlight==` | inline formatting |

## How correctness is checked

- `scripts/verify_examples.py` scans every Markdown file for inline equations: products, sums, chains of ±, powers, roots, and "x% of y". It also scans table rows with problem and answer columns, then recomputes each one. It re-checks thousands of generated questions against independent expressions.
- `tests/test_arithmetic.py` checks each Vedic algorithm over wide ranges against native arithmetic, along with every generator and the reference tables.
- `tests/test_examples.py` checks step tables such as Urdhva columns, Nikhilam deviations, sutra substitutions and recurring decimals.
- `tests/test_fonts.py` fails if any character in the content has no glyph in the registered fonts.

Questions are generated from fixed seeds, so every build is reproducible. Within one PDF no question text repeats, and the build prints a warning if a block cannot reach its requested count.

## Requirements and limitations

- **Fonts:** the design uses macOS system fonts: Helvetica Neue, Noteworthy for the handwritten headings, Courier New, and Arial Unicode as the fallback. On other systems, the build falls back to ReportLab's built-in fonts, which have a plainer look and fewer special glyphs. You can drop a handwriting TTF at `assets/fonts/Hand.ttf` as an alternative. The font test assumes the macOS fonts.
- **Question style:** practice questions come from templates. They are varied and verified, but they are not hand-crafted puzzles, and none is an official previous-year exam question.
- **History:** the sutras are presented as given in Bharati Krishna Tirthaji's *Vedic Mathematics* (1965). The book states clearly that they have not been found in known Vedic texts. Interpretations of some sutras, especially 5–9, 11, 13 and the sub-sutras, vary between authors.
- **Tracker:** the Excel formulas use only standard functions (IF, SUMIF, COUNT, AVERAGE, IFERROR). They were not recalculated in a spreadsheet application during the build.
