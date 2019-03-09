from enum import Enum

class Direction(Enum):
    DOWN = 0
    RIGHT = 1
    UP = 2
    LEFT = 3
    IDLE = 4

rows = [["A", "D", "O", "G"], ["A", "B", "C", "D"], ["A", "B", "C", "D"]];
words = ["DOG"]

def getNeighbor(i, j, direct: Direction):
    letter = ""
    if direct == Direction.DOWN:
        try:
            letter = rows[i + 1][j]
        except:
            return "", "", ""

        i += 1
    elif direct == Direction.RIGHT:
        try:
            letter = rows[i][j + 1]
        except:
            return "", "", ""

        j += 1
    elif direct == Direction.UP:
        try:
            letter = rows[i - 1][j]
        except:
            return "", "", ""

        i -= 1
    elif direct == Direction.LEFT:
        try:
            letter = rows[i][j - 1]
        except:
            return "", "", ""

        j -= 1
    elif direct == Direction.IDLE:
        try:
            letter = rows[i][j]
        except:
            return "", "", ""
    
    return i, j, letter


def solve(word):
    i_cords = []
    j_cords = []
    for i in range(len(rows)):
        for j in range(len(rows[i])):
            c_i = i
            c_j = j

            p_i, p_j, p_letter = getNeighbor(c_i, c_j, Direction.IDLE)

            if p_letter == word[0]:
                failed = False

                p_word = p_letter

                i_cords = [i]
                j_cords = [j]

                for letter in word[1:]:

                    p_i, p_j, p_letter = getNeighbor(c_i, c_j, Direction.DOWN)

                    if p_letter == letter:
                        c_i = p_i
                        c_j = p_j
                        i_cords.append(c_i)
                        j_cords.append(c_j)
                    else:
                        failed = True
                        break
                
                if failed:
                    failed = False
                    i_cords = [i]
                    j_cords = [j]
                    for letter in word[1:]:
                        p_i, p_j, p_letter = getNeighbor(c_i, c_j, Direction.RIGHT)

                        if p_letter == letter:
                            c_i = p_i
                            c_j = p_j
                            i_cords.append(c_i)
                            j_cords.append(c_j)
                        else:
                            failed = True
                            break
                
                if failed:
                    failed = False
                    i_cords = [i]
                    j_cords = [j]
                    for letter in word[1:]:
                        p_i, p_j, p_letter = getNeighbor(c_i, c_j, Direction.UP)

                        if p_letter == letter:
                            c_i = p_i
                            c_j = p_j
                            i_cords.append(c_i)
                            j_cords.append(c_j)
                        else:
                            failed = True
                            break

                if failed:
                    failed = False
                    i_cords = [i]
                    j_cords = [j]
                    for letter in word[1:]:
                        p_i, p_j, p_letter = getNeighbor(c_i, c_j, Direction.LEFT)

                        if p_letter == letter:
                            c_i = p_i
                            c_j = p_j
                            i_cords.append(c_i)
                            j_cords.append(c_j)
                        else:
                            failed = True
                            break
                
                return i_cords, j_cords
    return i_cords, j_cords



print(solve(words[0]))
    
# if rows[i][j] == word[0]:
#     for letter in word:
#             p_i, p_j, p_letter = getNeighbor(i, j, Direction.DOWN)
#             if p_letter == letter:
#                 i = p_i
#                 j = p_j

                    
