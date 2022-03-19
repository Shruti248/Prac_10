from PyPDF2 import PdfFileReader as pfr
myPdf = pfr("C:/Users/dell/Desktop/Marksheet.pdf")
print(myPdf.getNumPages())
print(myPdf.documentInfo)
for p in myPdf.pages:
    print(p.extractText())
