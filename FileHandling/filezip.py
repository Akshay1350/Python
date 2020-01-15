from zipfile import *
f=ZipFile("archive.zip",'w',ZIP_DEFLATED)
f.write("csvread.py")
f.write("csvwrite.py")
f.close()
print("zipped")

