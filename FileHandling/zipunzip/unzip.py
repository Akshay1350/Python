from zipfile import *
f=ZipFile("archive.zip",'r',ZIP_STORED)
names=f.namelist()
print(names)
f.extractall()
