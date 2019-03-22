from enum import Enum


class Direction(Enum):
    DOWN = 0
    RIGHT = 1
    UP = 2
    LEFT = 3
    IDLE = 4
    R_DIAGONAL = 5
    R_DIAGONAL_REV = 6
    L_DIAGONAL = 7
    L_DIAGONAL_REV = 8

# rows = [["A", "I", "C", "D"], ["A", "B", "U", "D"], ["A", "B", "C", "O"]];
# words = ["OUI"]


def getNeighbor(i, j, rows, direct: Direction):
    letter = ""
    if direct == Direction.DOWN:
        try:
            letter = rows[i + 1][j]
        except IndexError:
            return "", "", ""

        i += 1
    elif direct == Direction.RIGHT:
        try:
            letter = rows[i][j + 1]
        except IndexError:
            return "", "", ""

        j += 1
    elif direct == Direction.UP:
        try:
            letter = rows[i - 1][j]
        except IndexError:
            return "", "", ""

        i -= 1
    elif direct == Direction.LEFT:
        try:
            letter = rows[i][j - 1]
        except IndexError:
            return "", "", ""

        j -= 1
    elif direct == Direction.R_DIAGONAL:
        try:
            letter = rows[i + 1][j + 1]
        except IndexError:
            return "", "", ""

        j += 1
        i += 1
    elif direct == Direction.R_DIAGONAL_REV:
        try:
            letter = rows[i - 1][j - 1]
        except IndexError:
            return "", "", ""

        j -= 1
        i -= 1
    elif direct == Direction.L_DIAGONAL:
        try:
            letter = rows[i - 1][j + 1]
        except IndexError:
            return "", "", ""

        j += 1
        i -= 1
    elif direct == Direction.L_DIAGONAL_REV:
        try:
            letter = rows[i + 1][j - 1]
        except IndexError:
            return "", "", ""

        j -= 1
        i += 1
    elif direct == Direction.IDLE:
        try:
            letter = rows[i][j]
        except IndexError:
            return "", "", ""

    return i, j, letter


def solve(word, rows):
    i_cords = []
    j_cords = []
    for i in range(len(rows)):
        for j in range(len(rows[i])):
            c_i = i
            c_j = j

            p_i, p_j, p_letter = getNeighbor(c_i, c_j, rows, Direction.IDLE)

            if p_letter == word[0]:
                failed = False
                num_failed = 0

                i_cords = [i]
                j_cords = [j]

                for letter in word[1:]:

                    p_i, p_j, p_letter = getNeighbor(c_i, c_j, rows, Direction.DOWN)

                    if p_letter == letter:
                        c_i = p_i
                        c_j = p_j
                        i_cords.append(c_i)
                        j_cords.append(c_j)
                    else:
                        failed = True
                        num_failed += 1
                        c_i = i
                        c_j = j
                        break

                if failed:
                    failed = False
                    i_cords = [i]
                    j_cords = [j]
                    for letter in word[1:]:
                        p_i, p_j, p_letter = getNeighbor(c_i, c_j, rows, Direction.RIGHT)

                        if p_letter == letter:
                            c_i = p_i
                            c_j = p_j
                            i_cords.append(c_i)
                            j_cords.append(c_j)
                        else:
                            failed = True
                            num_failed += 1
                            c_i = i
                            c_j = j
                            break

                if failed:
                    failed = False
                    i_cords = [i]
                    j_cords = [j]
                    for letter in word[1:]:
                        p_i, p_j, p_letter = getNeighbor(c_i, c_j, rows, Direction.UP)

                        if p_letter == letter:
                            c_i = p_i
                            c_j = p_j
                            i_cords.append(c_i)
                            j_cords.append(c_j)
                        else:
                            failed = True
                            num_failed += 1
                            c_i = i
                            c_j = j
                            break

                if failed:
                    failed = False
                    i_cords = [i]
                    j_cords = [j]
                    for letter in word[1:]:
                        p_i, p_j, p_letter = getNeighbor(c_i, c_j, rows, Direction.LEFT)

                        if p_letter == letter:
                            c_i = p_i
                            c_j = p_j
                            i_cords.append(c_i)
                            j_cords.append(c_j)
                        else:
                            failed = True
                            num_failed += 1
                            c_i = i
                            c_j = j
                            break

                if failed:
                    failed = False
                    i_cords = [i]
                    j_cords = [j]
                    for letter in word[1:]:
                        p_i, p_j, p_letter = getNeighbor(c_i, c_j, rows, Direction.R_DIAGONAL)

                        if p_letter == letter:
                            c_i = p_i
                            c_j = p_j
                            i_cords.append(c_i)
                            j_cords.append(c_j)
                        else:
                            failed = True
                            num_failed += 1
                            c_i = i
                            c_j = j
                            break

                if failed:
                    failed = False
                    i_cords = [i]
                    j_cords = [j]
                    for letter in word[1:]:
                        p_i, p_j, p_letter = getNeighbor(c_i, c_j, rows, Direction.R_DIAGONAL_REV)

                        if p_letter == letter:
                            c_i = p_i
                            c_j = p_j
                            i_cords.append(c_i)
                            j_cords.append(c_j)
                        else:
                            failed = True
                            num_failed += 1
                            c_i = i
                            c_j = j
                            break

                if failed:
                    failed = False
                    i_cords = [i]
                    j_cords = [j]
                    for letter in word[1:]:
                        p_i, p_j, p_letter = getNeighbor(c_i, c_j, rows, Direction.L_DIAGONAL)

                        if p_letter == letter:
                            c_i = p_i
                            c_j = p_j
                            i_cords.append(c_i)
                            j_cords.append(c_j)
                        else:
                            failed = True
                            num_failed += 1
                            c_i = i
                            c_j = j
                            break

                if failed:
                    failed = False
                    i_cords = [i]
                    j_cords = [j]
                    for letter in word[1:]:
                        p_i, p_j, p_letter = getNeighbor(c_i, c_j, rows, Direction.L_DIAGONAL_REV)

                        if p_letter == letter:
                            c_i = p_i
                            c_j = p_j
                            i_cords.append(c_i)
                            j_cords.append(c_j)
                        else:
                            failed = True
                            num_failed += 1
                            c_i = i
                            c_j = j
                            break

                if num_failed != 8:
                    return i_cords, j_cords
                else:
                    continue
    return [], []
