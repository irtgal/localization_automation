from File import *
import os
import re

folder = r"C:\Users\Student\Desktop\Nucleus\manager\src\modules\Epgs"
for f in os.listdir(folder):
    if f.endswith("vue") or f.endswith("txt"):
        file = File(folder, f)
        file.generate_translated_file()
        file.write_file()
