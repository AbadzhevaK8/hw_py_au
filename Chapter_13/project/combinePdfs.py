  #!python3
# combinePdfs.py - обьединяет все пдфки из одного каталога в один файл без титульных листов.

import PyPDF2
import os

# получение списка имен пдфок
pdfFiles = []
for filename in os.listdir('.'):
    if filename.endswith('.pdf'):
        pdfFiles.append(filename)

pdfFiles.sort(key=str.lower)

pdfWriter = PyPDF2.PdfFileWriter()

# организация цикла по всем пдфкам
for filename in pdfFiles:
    pdfFileObj = open(filename, 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    # оргинизация цикла по всем страницам, кроме первой, с их добавлением в результирующий документ
    for pageNum in range(1, pdfReader.numPages):
        pageObj = pdfReader.getPage(pageNum)
        pdfWriter.addPage(pageObj)

# сохранить результирующий документ в файл
pdfOutput = open('allminutes.pdf', 'wb')
pdfWriter.write(pdfOutput)
pdfOutput.close()
