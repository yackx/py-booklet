#!/usr/bin/env python

"""Rearrange the order of a PDF document so that it can be printed as a booklet.

The printed booklet can be folded and stapled to form a small book.

E.g., for a document with 8 pages, this script rearranges the pages as follows:
8, 1, 2, 7, 6, 3, 4, 5
"""

import argparse
import os

from pypdf import PdfReader as Reader, PdfWriter as Writer


def order_booklet(number_of_pages):
    if number_of_pages % 4 != 0:
        raise ValueError(f"Number of pages must be a multiple of 4 (got {number_of_pages})")

    page_order = []
    n = number_of_pages
    m = 0
    for i in range(number_of_pages // 4):
        page_order.append(n)
        page_order.append(m + 1)
        page_order.append(m + 2)
        page_order.append(n - 1)
        n -= 2
        m += 2

    return page_order


def parse_arguments():
    parser = argparse.ArgumentParser(description="""
Rearrange the order of a PDF document so that it can be printer as a booklet.\n
The setting of your printer should be:
\t(1). Paper size: Tabloid (11*17 in) for academic papers, books, etc;
\t(2). Layout: 2 pages per sheet. Set layout direction to normal 'Z' layout. Set two-sided to Short-Edge binding.
\t(3). Scale to fit the page. An example setup for ARA&A:
\t\t162% on 11*17 Borderless""")
    parser.add_argument(dest='file', type=str, help="The PDF file to convert")
    parser.add_argument('-p', '--dry-run', action="store_true", help="Do not re-arrrange")
    return parser.parse_args()


def main(file_path: str, dry_run: bool):
    original_pdf = Reader(open(file_path, 'rb'))
    original_page_count = len(original_pdf.pages)
    booklet_pdf = Writer()
    page_order = order_booklet(original_page_count)
    print(f"Rearranged:\n{page_order}")
    for page in page_order:
        booklet_pdf.add_page(original_pdf.pages[page - 1])

    output_file_name = os.path.join(
        os.path.dirname(file_path),
        os.path.basename(file_path) + ".booklet.pdf"
    )
    print(output_file_name)
    if not dry_run:
        with open(output_file_name, 'wb') as f:
            booklet_pdf.write(f)
        print(f"File saved as {output_file_name}")


if __name__ == "__main__":
    args = parse_arguments()
    main(args.file, args.dry_run)
