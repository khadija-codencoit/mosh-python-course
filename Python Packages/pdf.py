import PyPDF2
import os
import time

# with open("pdf-files/Taupe-Notch-SRS(Khadija).pdf","rb") as file:
#     reader = PyPDF2.PdfReader(file)
#     #print(reader)
#     for page in reader.pages:
#         print(page)

merge = PyPDF2.PdfMerger()
file_names = ["pdf-files/Taupe-Notch-SRS(Khadija).pdf","pdf-files/Menu Idea (1).pdf"]
for file_name in file_names:
    merge.append(file_name)

merge.write("pdf-files/comabine.pdf")
merge.close()
os.startfile("pdf-files/comabine.pdf")