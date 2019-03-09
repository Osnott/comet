def parse(text: str):
    rows = []
    split_text = text.split("\n")
    for row in split_text:
        rows.append(list(row))
    
    return rows

# print(parse("ABCD\nEFGH\nIJKL\nMNOP"))