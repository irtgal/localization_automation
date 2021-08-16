import os
import re
import ntpath
import sys

warning_count = 0

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
            self.raise_warning(f"Couldn`t find file")
    
    def write_file(self):
        full_path = f"{self.path}/{self.name}"
        actual_file = open(full_path, "w", encoding="utf-8")
        actual_file.write(self.new_lines)
        actual_file.close()

        
    def raise_warning(self, message):
        global warning_count
        warning_count += 1
        nice_path = self.path.replace("\\", "/")
        print(f'{warning_count}. WARNING: {nice_path}/{self.name} ->\n"{message}"\n')

    def find_dirty_text(self):
        pattern = re.compile(r"\>[\w|\s|!?.,-/:_;&\\\`\'()]+\<")
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
            if clean_str:
                translated_str = form_translation(clean_str)
                whitespaces = dirty_str.split(clean_str)
                self.translations[dirty_str] = whitespaces[0]+translated_str+whitespaces[1]     
        self.replace_translations()


    
def extract_text(file, dirty_str):
    plain_text = re.search(r"[A-Za-z]+", dirty_str[1:-1].strip())
    #dont translate $nbsp;  
    if re.search(r"&[\w]+;", dirty_str):
        file.raise_warning(dirty_str)
        return None

    #dont translate variables
    elif "{" in dirty_str:
        if re.sub(r"\{\{.*?\}\}", "", dirty_str[1:-1]).strip() != "": 
            file.raise_warning(dirty_str)
        return None

    #dont translate text shroter than 2 cahracters
    elif not plain_text or len(plain_text.group(0)) < 2:
        return None
    return dirty_str[1:-1].strip()
    
def form_translation(clean_str):
    clean_str = re.sub(r"[\s]+", " ", clean_str)
    str_lower =clean_str.replace(" ", "-").lower()
    return f'{{{{translate("{str_lower}","{clean_str}")}}}}'



# --MAIN--


def main(base_dir):
    for root, dirs, files in os.walk(base_dir):
        for filename in files:
            if filename.endswith("vue") or filename.endswith("html"):
                file = File(root, filename)
                file.generate_translated_file()
                file.write_file()

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("ERROR: Specify the path to the project!")
        quit()

    base_dir = sys.argv[1]
    if not os.path.exists(base_dir):
        print("ERROR: Specified path doesn`t exist!")
        quit()

    main(base_dir)



        