import pathlib

filename = pathlib.Path(input("Enter file location with: "))
print(f"Splitting '{filename}' into separate 1GB files:")

def read_file_in_chunks(file_path):
 CHUNK_SIZE = 1 * 1024 * 1024 * 1024 # 1GB
 with open(file_path, 'rb') as file:
  while True:
   chunk = file.read(CHUNK_SIZE)
   if not chunk:
    break
   yield chunk

for i, chunk in enumerate(read_file_in_chunks(filename)):
  new_file_name = f"{filename.stem}_{i}{filename.suffix}"
  new_file_path = filename.parent / new_file_name
  with open(new_file_path, 'wb') as file:
    file.write(chunk)
    print(f"{i}. {new_file_name}")

print("Finished.")