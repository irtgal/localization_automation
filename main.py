from File import *
import os
import re
import ntpath

folder = r"C:\Users\Student\Desktop\Nucleus\manager\src\modules\Epgs"
for f in os.listdir(folder):
    if f.endswith("vue") or f.endswith("txt"):
        file = File(folder, f)
        file.generate_translated_file()
        file.write_file()
        
class File:
    def __init__(self, path, file_name):
        self.name = file_name
        self.path = path

        self.read_file()

    def __str__(self):
        return f"FILE: {self.name}"

    def read_file(self):
        full_path = f"{self.path}/{self.name}"
        if (os.path.exists(full_path)):
            file = open(full_path, 'r', encoding='utf-8')
            lines = file.readlines()
            self.lines = "".join(lines)
        else:
            raise Exception(f"Couldn`t find {self.path}/{self.name}")
    
    def write_file(self):
        full_path = f"{self.path}/{self.name}"
        actual_file = open(full_path, "w", encoding="utf-8")
        actual_file.write(self.new_lines)
        actual_file.close()

        
    def raise_warning(self, message):
        print(f'WARNING: "{message}" in {self.path}/{self.name}')

    def find_dirty_text(self):
        pattern = re.compile(r"\>[\w|\s|!?.,-/:_;&\\]+\<")
        result = re.findall(pattern, self.lines)
        text = [el for el in result if el[1:-1].strip() != '']
        return text
    
    def replace_translations(self):
        new_lines = self.lines
        for dirty_str in self.translations:
            new_lines = new_lines.replace(dirty_str, self.translations[dirty_str])
        self.new_lines = new_lines

 
    def generate_translated_file(self): 
        self.translations = {}
        dirty_text = self.find_dirty_text()
        for dirty_str in dirty_text:
            clean_str = extract_text(self, dirty_str)
            translated_str = form_translation(clean_str)
            whitespaces = dirty_str.split(clean_str)
            self.translations[dirty_str] = whitespaces[0]+translated_str+whitespaces[1]     
        self.replace_translations()


    
def extract_text(file, dirty_str):
    if re.search(r"&[\w]+;", dirty_str):
        file.raise_warning(dirty_str)
    return dirty_str[1:-1].strip()
    
def form_translation(clean_str):
    clean_str = re.sub(r"[\s]+", " ", clean_str)
    str_lower =clean_str.replace(" ", "-").lower()
    return f'{{{{translate("{str_lower}","{clean_str}")}}}}'
