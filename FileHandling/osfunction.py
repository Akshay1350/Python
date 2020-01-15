import os
from datetime import *
#os.system("py marriage_list.py")


stats = os.stat("Penguins.jpg")
print("filesize : ",stats.st_size)
print("atime : ",datetime.fromtimestamp(stats.st_atime))
print("mtime : ",datetime.fromtimestamp(stats.st_mtime))
print("ctime : ",datetime.fromtimestamp(stats.st_ctime))
