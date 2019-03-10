def display(rows, words, solves):
    for word in range(len(words)):
        for letter in range(len(words[word][0])):
            for i in range(len(rows)):
                for j in range(len(rows[i])):
                    try:
                        if i == solves[word][0][letter] and j == solves[word][1][letter]:
                            rows[i][j] = "|"
                            continue
                            # rows[i][j] = Color.BOLD + rows[i][j] + Color.END
                    except:
                        continue
    

    for i in range(len(rows)):
        for j in range(len(rows[i])):
            if j == 0:
                rows[i][j] = rows[i][j] + " "
            elif j == len(rows[i])-1:
                rows[i][j] = " " + rows[i][j] + "\n"
            else:
                rows[i][j] = " " + rows[i][j] + " "
    
    return rows
