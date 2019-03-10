def parse(text: str):
    rows = []
    split_text = text.split("\n")
    for row in split_text:
        rows.append(list(row))
    
    return rows

def rev_parse(rows):
    text = ""
    for i in range(len(rows)):
        for j in range(len(rows[i])):
            text += rows[i][j]
    
    return text