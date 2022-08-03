# py -m pip install pypdf2
# cmd: cd    for å bytte folder 
# cmd: dir   for å se hva som er i folderen
# Gå til mappen du har doc_to_pdf i
# cmd: doc_to_pdf.py "Path to folder"

import glob
from PyPDF2 import PdfFileMerger
import sys
from docx2pdf import convert
import re
import os
import win32com.client as win32
from win32com.client import constants
from time import sleep

def save_as_docx(path):
    paths = glob.glob(f"{path}\*.doc")

    for path2 in paths:
        # Opening MS Word
        word = win32.gencache.EnsureDispatch('Word.Application')
        doc = word.Documents.Open(path2)
        doc.Activate ()

        # Rename path with .docx
        new_file_abs = os.path.abspath(path2)
        new_file_abs = re.sub(r'\.\w+$', '.docx', new_file_abs)

        # Save and Close
        word.ActiveDocument.SaveAs(
            new_file_abs, FileFormat=constants.wdFormatXMLDocument
        )
        doc.Close(False)


def _docx_to_pdf(path):
    convert(path)


def PPTtoPDF(inputFileName, outputFileName, formatType = 32):
    powerpoint = win32.Dispatch("Powerpoint.Application")
    powerpoint.Visible = 1

    if outputFileName[-3:] != 'pdf':
        outputFileName = outputFileName + ".pdf"
    deck = powerpoint.Presentations.Open(inputFileName)
    sleep(10)  # Give time to load all images
    deck.SaveAs(outputFileName, formatType) # formatType = 32 for ppt to pdf
    deck.Close()
    powerpoint.Quit()

def pptx_handler(path):
    paths = glob.glob(f"{path}\*.pptx")
    paths = [*paths, *glob.glob(f"{path}\*.ppt")]

    for p in paths:
        PPTtoPDF(p, p.split('.')[0])


def merge_files(path):
    pdfs = glob.glob(f"{path}\*.pdf")

    merger = PdfFileMerger(strict=False)

    for pdf in pdfs:
        merger.append(pdf)

    merger.write(f"{path}\merged.pdf")
    merger.close()

def print_info():
    print("""
    -- Merge files in folder with .doc, .docx, pptx --
    cmd: office_to_pdf.py "Path to folder" [do_merge_files-bool]
    """)



if __name__ == "__main__":
    if len(sys.argv) == 1 or sys.argv[1] == 'info':
        print_info()
    else:
        path = sys.argv[1]

        print("Processing: .doc to .docx", end="")
        save_as_docx(path)
        print(" - Complete")

        print("Processing: .docx to pdf")
        _docx_to_pdf(path)
        print("Processing: .docx to pdf - Complete")

        print("Processing: .pptx and .ppt to pdf", end="")
        pptx_handler(path)
        print(" - Complete")

        if len(sys.argv) == 3:
            if sys.argv[2] == "1":
                print("Processing: merge pdfs", end="")
                merge_files(path)
                print(" - Complete")
                # print(f" -- Merged all files to {path}\merged.pdf --")
