# import comtypes.client
import win32com.client as win32
import glob
import sys
from time import sleep

def PPTtoPDF(inputFileName, outputFileName, formatType = 32):
    paths = glob.glob(f"{path}\*.doc")


    powerpoint = win32.Dispatch("Powerpoint.Application")
    powerpoint.Visible = 1

    if outputFileName[-3:] != 'pdf':
        outputFileName = outputFileName + ".pdf"
    deck = powerpoint.Presentations.Open(inputFileName)
    sleep(10) # Give time to load all images
    deck.SaveAs(outputFileName, formatType) # formatType = 32 for ppt to pdf
    deck.Close()
    powerpoint.Quit()

def print_info():
    print("""
    -- Merge files in folder with .pptx --
    cmd: pptx_to_pdf.py "Path to folder"
    """)

if __name__ == "__main__":
    if len(sys.argv) == 1 or sys.argv[1] == 'info':
        print_info()
    else:
        path = sys.argv[1]

        paths = glob.glob(f"{path}\*.pptx")

        for p in paths:
            PPTtoPDF(p, p + '_pdf_version')