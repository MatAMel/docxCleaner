from zipfile import ZipFile
import re
import sys

fileName = sys.argv[1]
safeFile = "safeFile.txt"

safe = open(safeFile, "w", encoding="utf-8")

with ZipFile(fileName, "r") as zip:
    data = zip.read("word/document.xml").decode("utf-8")
    data = re.sub(r"<(.*?)>" , "", str(data))
    data = re.sub(r"\\r\\n\\t", "", str(data))
    
    safe.write(data)
    safe.close()
    zip.close()