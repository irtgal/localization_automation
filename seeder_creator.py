import os
import re
import ntpath
import pathlib


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

    def find_translations(self):
        pattern = re.compile(r"{{\s*translate\([\"\'](.+?)[\"\']\s*,\s*[\"\'](.+?)[\"\']")
        result = re.findall(pattern, self.lines)
        self.translations = {}
        for (key, value) in result:
            self.translations[key] = value
        return self.translations
    
def generate_array(translations_dict):
    print(len(translations_dict.items()))
    result = ""
    for x,(key, value) in enumerate(translations_dict.items()):
        line = f"[\"language_id\"=> $language_id, \"key\" => \"{key}\", \"value\" => \"{value}\"],"
        print(result.count("\n"), line)
        result += line + "\n"
    return result
        



def write_file(translations_dict):
    full_path = f"{pathlib.Path().resolve()}/seeds.txt"
    actual_file = open(full_path, "w", encoding="utf-8")
    actual_file.write(translations_dict)
    actual_file.close()


# --MAIN--
base_dir = r"C:\Users\Gal\Desktop\Nucleus\client-stb\src\default"
translations_dict = {}
for root, dirs, files in os.walk(base_dir):
    for filename in files:
        if filename.endswith("vue") or filename.endswith("html"):
            file = File(root, filename)
            file_translations = file.find_translations()
            translations_dict.update(file_translations)

            #file.write_file()
print(len(translations_dict))
write_file(generate_array(translations_dict))
print('File generated inside: ' + f"{pathlib.Path().resolve()}/seeds.txt")
