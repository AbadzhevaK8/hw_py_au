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
