#!/usr/bin/env python3
"""Convert PDF file to CSV file"""

import argparse
import os
import tabula
import lowbar

# define and parse args
parser = argparse.ArgumentParser(
    description="Convert PDF file to CSV file")
parser.add_argument("-i", "--input", type=str, nargs='+',
                    help='path to pdf file to convert')
parser.add_argument("-o", "--outfile", type=str, nargs='+',
                    help='path to desired csv output file')
args = parser.parse_args()


def convert_to_csv(path_tup):
    """Export pdf to csv file"""
    bar = lowbar.LowBar()
    if args.outfile:
        out_file = args.outfile[0]
    else:
        out_file = f"{path_tup[0]}.csv"
    print(f"Converting `{path_tup[0]+path_tup[1]}` to csv file...")
    try:
        bar.update(0)
        tabula.convert_into(
            path_tup[0]+path_tup[1], f"{out_file}", output_format="csv", pages='all')
        bar.update_smooth(100)
        bar.clear()
        print(f"[SUCCESS] CSV file saved: `{out_file}`")
    except Exception as err:
        print(f"Error: {err}")


def main():
    """Main"""
    pdf_path = os.path.splitext(str(args.input[0]))
    convert_to_csv(pdf_path)


if __name__ == "__main__":
    main()
