# Chem 151 Formula Sheet for the TI-84 Evo (Python)

A menu-driven Python app with everything from **Chem 151 Formula Sheet:
Chemical Thinking Vol. I**: constants, conversions, every formula, variable,
note, method, and table. All the math is written in plain calculator-readable
ASCII.

## Menu layout

```
CHEM 151 FORMULAS (main menu)
|- 0 Constants+Conv          <- module
|   |- 0.1 Constants         <- unit
|   |   |- Formulas          <- tabs (only the ones that unit has)
|   |   |- Variables
|   |   |- Notes
|   |   '- Cheats   (methods, tables, shortcuts, traps)
|   ...
|- 1 U1(M1-2) Phases        (1.1 - 1.10)
|- 2 U1(M3-4) Counting      (2.1 - 2.8)
|- 3 U2 Light/Atom/Bond     (3.1 - 3.8)
|- 4 U3 IMFs/Ionic          (4.1 - 4.6)
|- 5 U4 Reactions/Energy    (5.1 - 5.5)
|- ALL Formulas+Vars
|   |- All formulas    (by module)
|   |- All variables   (by module)
|   |- Glossary A-Z    (every symbol, tagged with its unit, e.g. [2.4])
|   '- Constants
|- Notation key/Help  (navigation, how to read the math, Greek letters,
|                      chemistry symbols, full table of contents)
'- Screen setup
```

## Install

1. Install **TI Connect CE** and connect the calculator with USB.
2. Send **every** `.py` file in the [`TI84EVO/`](TI84EVO) folder:
   `CHEM151.py` plus the data files `C151D01.py` ... `C151D22.py`.
   Drag them all onto the calculator in one go (TI Connect CE turns them
   into Python files on the calculator).
3. On the calculator, open the **Python** app, pick `CHEM151`, and run it.
   The `C151Dxx` files are data only. Don't run them, just keep them on the
   calculator.

## Using it

| Key | Action |
| --- | --- |
| number then `enter` | open that item |
| `enter` | next page (on the last page it goes back) |
| `-` then `enter` | previous page |
| page number then `enter` | jump to that page (while reading) |
| `0` then `enter` | back one level (quits from the main menu) |
| `00` then `enter` | jump to the main menu |
| `on` | stop the program |

**Screen setup:** the app starts at 25 characters x 10 lines, which fits on
any TI-84 model. If your screen has room for more, open *Screen setup* from
the main menu. It shows a ruler, so you can enter the number of characters
that fit and check the result. The setting is saved in a list named `CHEMS`
so it sticks between runs. You can also change `COLS=` / `ROWS=` at the top
of `CHEM151.py`.

### How the math is written

| On screen | Means |
| --- | --- |
| `x_1`, `x^2` | subscript, power |
| `6.022x10^23` | 6.022 x 10^23 (type `6.022E23` on the calculator) |
| `*`, `/` | multiply, divide |
| `<E_k>` | average kinetic energy |
| `SUM`, `\|x\|`, `~`, `prop. to` | sum, absolute value, approximately, proportional to |
| `Delta`, `delta` | change in (DeltaH), partial charge (delta+) |
| `lambda`, `nu`, `nu~`, `chi`, `mu`, `rho` | wavelength, frequency, wavenumber, electronegativity, dipole moment, density |
| `Ca^2+`, `SO4^2-` | ion charges |
| `C=O`, `C#N` | double bond, triple bond |
| `->`, `<->`, `degC` | gives, both ways, degrees Celsius |

The full key is in the app under *Notation key/Help*.

## Why there are many files

The calculator's Python memory (heap) is small. Each tab's text is stored in
small data files, and the app loads only the file it needs, shows the text,
then frees the memory. This keeps the app from crashing with `MemoryError`.

## Troubleshooting

- **"Missing file C151Dxx"**: send all the `C151D*.py` files again.
- **MemoryError**: quit and rerun the Python app, or free up RAM by archiving
  or deleting other programs.
- **Lines wrap badly or the top of the page scrolls off**: lower the
  characters per line or lines per screen in *Screen setup*.

## Editing the content

The content lives in [`src/chem151_content.py`](src/chem151_content.py), and
the app template is in [`src/main_template.py`](src/main_template.py). After
you change either one, rebuild and test:

```
python3 build.py          # regenerates TI84EVO/*.py (fails on non-ASCII text or titles that are too long)
python3 tests/sim_test.py # walks every menu, tab and page at several screen sizes
```
