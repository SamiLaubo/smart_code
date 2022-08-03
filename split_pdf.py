from PyPDF2 import PdfFileWriter, PdfFileReader
import sys
from os import path as os_path

# notes = PdfFileReader(open(r"C:\Users\Sami Laubo\OneDrive - NTNU\2021v\Kjemi\Eksamen\Diagrammer\Notater.pdf", "rb"))
# ovs = PdfFileReader(open(r"C:\Users\Sami Laubo\OneDrive - NTNU\2021v\Kjemi\Eksamen\Diagrammer\Øvinger.pdf", "rb"))
# output = PdfFileWriter()

# notes_pages = [38, 42]
# ovs_pages = [6, 16, 18, 66]

# for p in notes_pages:
#     output.addPage(notes.getPage(p - 1))

# for p in ovs_pages:
#     output.addPage(ovs.getPage(p - 1))

# output.write(open(r"C:\Users\Sami Laubo\OneDrive - NTNU\2021v\Kjemi\Eksamen\Diagrammer\Diagrammer.pdf", "wb"))

# for i in range(inputpdf.numPages):
#     output = PdfFileWriter()
#     output.addPage(inputpdf.getPage(i))
#     with open("document-page%s.pdf" % i, "wb") as outputStream:
#         output.write(outputStream)
#
#
#
def split_files(path, pstart, pend = -1):
    notes = PdfFileReader(open(f"{path}.pdf", "rb"))
    output = PdfFileWriter()

    if pend == -1: pend = pstart

    for p in range(int(pstart), int(pend) + 1):
        output.addPage(notes.getPage(p - 1))

    path = '\\'.join(path.split('\\')[:-1])

    new_name = "split"
    if os_path.exists(f"{path}\{new_name}.pdf"):
        i = 1
        new_name = "split1"
        while os_path.exists(f"{path}\{new_name}.pdf") and i < 1000:
            i += 1
            new_name = "split" + str(i)

    output.write(open(f"{path}\{new_name}.pdf", "wb"))

    print(f"Sucess: {path}\{new_name}.pdf")

    


if __name__ == "__main__":
    if len(sys.argv) == 1 or sys.argv[1] == 'info':
        print(
        """ 
        INFO:

        cmd: split_pdf.py path pstart [pend]

        path - Path to folder with name of file without .pdf
        split from - [pstart, pend] (page number, not index)
        pend = pstart as default
        """
        )
    else:        
        split_files(*(sys.argv[1:]))
