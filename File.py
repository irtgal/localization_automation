import re
import os
import ntpath

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

    def find_dirty_text(self):
        pattern = re.compile(r"\>[\w|\s|!?.,-/:_;&\\]+\<")
        result = re.findall(pattern, self.lines)
        text = [el for el in result if el[1:-1].strip() != '']
        return text



    def do_work(self): 
        translations = {}
        dirty_text = self.find_dirty_text()
        for dirty_str in dirty_text:
            clean_str = extract_text(dirty_str)
            translated_str = form_translation(clean_str)
            whitespaces = dirty_str.split(clean_str)
            translations[dirty_str[1:-1]] = whitespaces[0]+translated_str+whitespaces[1]     
        
        for t in translations:  
            print(f"->{t}|{translations[t]}<-")

    
def extract_text(dirty_str):
    return dirty_str[1:-1].strip()
    
def form_translation(str):
    str_lower = "-".join(str.split(" ")).lower()
    return f'translate("{str_lower}","{str}")'




