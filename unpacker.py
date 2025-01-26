import os
import sys

directory = input("Enter the directory path: ")
os.chdir(directory)
files = os.listdir()

if not files:
    print("No files found in the directory.")
    sys.exit()

file_extension = None
if '.' in files[0]:
    file_extension = files[0].split('.')[-1]
if not file_extension:
    print("No file extention.")
    sys.exit()

file_name = '_'.join(files[0].split('_')[0:-1])
print(file_name)

with open(f'{file_name}.{file_extension}', 'wb') as output_file:
    for file in files:
        if file.endswith(f".{file_extension}") and file.startswith(file_name):
            with open(file, 'rb') as f:
                content = f.read()
                output_file.write(content)

print(f"All files combined into {file_name}")