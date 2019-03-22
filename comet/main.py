from ocr import recognize
from parse import parse
from solver import solve

file = open("words.txt", "r")

words = file.readlines()

for i in range(len(words)):
    words[i] = words[i].upper().rstrip("\n")

print("\nSolving for the words: " + str(words) + "\n")

raw_text = recognize()
print("Wordsearch out:")
print(raw_text + "\n")
rows = parse(raw_text)
solves = []

for word in words:
    xs, ys = solve(word, rows)
    solves.append([xs, ys])

print("Solves:")
print(solves)

# print("Pretty print:")
# print(rev_parse(display(rows, words, solves)))

# TODO: Do pretty print
