##### Brukes slik
# cmd -> cd to folder with merger.py
# eks.: cd "C:\Users\Sami Laubo\OneDrive - NTNU\2021v"
# cmd -> merge.py "PATH to folder with pdfs"
# eks.: merge.py "C:\Users\Sami Laubo\OneDrive - NTNU\2021v\pdfs"

import glob
from PyPDF2 import PdfFileMerger
import sys
from os import path as os_path


# pdfs = glob.glob(r"C:\Users\Sami Laubo\OneDrive - NTNU\2021v\Vitber\Eksamensforberedelse\pdfer\*.pdf")
# # *.pdf gir en array med alle pdf paths
# # pdfs = glob.glob(r"C:\Users\Sami Laubo\OneDrive - NTNU\2020h\Termisk\Eksamner\Alle_eksamner\*.pdf")
#
# # pdfs.append(r"C:\Users\Sami Laubo\OneDrive - NTNU\2021v\Optikk\A5\1bd.pdf"
#
# merger = PdfFileMerger(strict=False)
#
# for pdf in pdfs:
#     merger.append(pdf)
#
# merger.write(r"C:\Users\Sami Laubo\OneDrive - NTNU\2021v\Vitber\Eksamensforberedelse\pdfer\Alle.pdf")
# merger.close()


def merge_files(path):
    pdfs = glob.glob(f"{path}\*.pdf")

    merger = PdfFileMerger(strict=False)

    for pdf in pdfs:
        merger.append(pdf)

    new_name = "merged"
    if os_path.exists(f"{path}\{new_name}.pdf"):
        i = 1
        new_name = "merged1"
        while os_path.exists(f"{path}\{new_name}.pdf") and i < 1000:
            i += 1
            new_name = "merged" + str(i)

    merger.write(f"{path}\{new_name}.pdf")
    merger.close()

    print(f"# merged all files to {path}\{new_name}.pdf")

def print_info():
    print("""
    -- Merge files in folder --
    cmd: merge.py "Path to folder"
    """)


if __name__ == "__main__":
    if len(sys.argv) == 1 or sys.argv[1] == 'info':
        print_info()
    else:
        merge_files(sys.argv[1])
