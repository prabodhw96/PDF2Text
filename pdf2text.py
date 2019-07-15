from PyPDF2 import PdfFileWriter, PdfFileReader
import os, errno
from subprocess import call
import sys

def split(directory, filename):
    inputpdf = PdfFileReader(open(filename, "rb"))
    try:
        os.makedirs(directory)
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise
            
    for i in range(inputpdf.numPages):
        output = PdfFileWriter()
        output.addPage(inputpdf.getPage(i))
        with open(directory + "/%s.pdf" % i, "wb") as outputStream:
            output.write(outputStream)
            
if len(sys.argv) < 2:
    print("Error\nFormat: \n\tpython main.py your-pdf-file")
else:
    filename = sys.argv[1]
    directory = "splitted/" + filename
    
    split(directory, filename)
    pdfFileObj = open(filename, 'rb')
    pdfReader = PdfFileReader(pdfFileObj)
    
    for i in range(pdfReader.numPages):
        splitted_file_name = directory + "/" + repr(i)
        call(["pdftotext", splitted_file_name + ".pdf"])