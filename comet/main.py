from ocr import recognize
from parse import parse
from solver import solve

raw_text = recognize()
print(raw_text + "\n")
rows = parse(raw_text)
print(rows)
print("")
print(solve("YAY", rows))