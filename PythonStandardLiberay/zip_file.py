from pathlib import Path
from zipfile import ZipFile

with ZipFile("Zip","w") as z:
    for i in Path("Data Structures").rglob("*"):
        z.write(i)


for z in ZipFile('Zip', 'r').namelist():
    print(z)