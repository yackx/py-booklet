# py-booklet

**Rearrange the order of a PDF document so that it can be printed as a booklet**

The printed booklet can be folded and stapled to form a small book.

E.g., for a document with 8 pages, this script rearranges the pages as follows:
`8, 1, 2, 7, 6, 3, 4, 5`.

## Installation

```
pip install -r requirements.txt
```

You are advised to create a virtual environment first.

## Usage

```
python booklet.py path/to/PDF/file
```

will create a new PDF file in the same folder as the original file,
with pages rearranged. It will not overwrite the original PDF document.

The number of pages **must be a multiple of 4**.

## Steps to print a booklet

- The original PDF is ideally in A5 format. A4 is acceptable, howver the resulting font size ay be too small.
- Rearrange the PDF document you want to print using this python script.
- Print the PDF in A4
- Fold it and staple it.

## Caveats

Not related to this script but to printers and drivers.
When printing the booklet, you typically want small margins but:

- On macOS, Preview.app tends to add excessive margins.
- On Linux, some drivers may crop the pages.
