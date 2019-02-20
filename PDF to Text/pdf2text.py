#pip install PyPDF2

import PyPDF2
pdfFileObj = open('Restaurant.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
print(pdfReader.numPages)


for i in range(pdfReader.numPages):
    pageObj = pdfReader.getPage(i)
    print("Page - ",i,"\n")
    print(pageObj.extractText())
    print("\n\n\n")
