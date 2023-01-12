# try:
#     open("text.txt")
#     print("File exists")
# except FileNotFoundError:
#     print("File not found")

import os.path

print('File exists' if os.path.exists('text.txt') else 'File not found')