from pathlib import Path
from zipfile import ZipFile

with ZipFile("files.zip", "w") as zip:
    for path in Path("test").rglob("*.*"):
        zip.write(path)
