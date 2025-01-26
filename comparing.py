import sys

file_1 = input("Enter 1 file path: ")
file_2 = input("Enter 2 file path: ")

if open(file_1, 'rb').read() == open(file_2, 'rb').read():
    print("Files are eqal!")
else:
    print("Files are different!")
sys.exit()