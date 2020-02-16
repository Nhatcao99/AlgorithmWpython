def isValidSudoku(self, board: List[List[str]]) -> bool:
    # when [{dic}]*n they will be have the same address which made them n but one
    # so in must initialize like this
    hash_row, hash_col, hash_box = [], [], []
    for c in range(9):
        tmp1, tmp2, tmp3 = {"1": 0, "2": 0, "3": 0, "4": 0, "5": 0, "6": 0, "7": 0, "8": 0, "9": 0}, {"1": 0, "2": 0,
                                                                                                      "3": 0, "4": 0,
                                                                                                      "5": 0, "6": 0,
                                                                                                      "7": 0, "8": 0,
                                                                                                      "9": 0}, {"1": 0,
                                                                                                                "2": 0,
                                                                                                                "3": 0,
                                                                                                                "4": 0,
                                                                                                                "5": 0,
                                                                                                                "6": 0,
                                                                                                                "7": 0,
                                                                                                                "8": 0,
                                                                                                                "9": 0}
        hash_row.append(tmp1)
        hash_col.append(tmp2)
        hash_box.append(tmp3)
    for i in range(0, 9):
        for j in range(0, 9):
            if board[i][j] == '1' or board[i][j] == '2' or board[i][j] == '3' or board[i][j] == '4' or board[i][
                j] == '5' or board[i][j] == '6' or board[i][j] == '7' or board[i][j] == '8' or board[i][j] == '9':
                hash_row[i][board[i][j]] += 1
                hash_col[j][board[i][j]] += 1
                if i >= 0 and i <= 2:
                    if j >= 0 and j <= 2: hash_box[0][board[i][j]] += 1
                    if j >= 3 and j <= 5: hash_box[1][board[i][j]] += 1
                    if j >= 6 and j <= 8: hash_box[2][board[i][j]] += 1
                if i >= 3 and i <= 5:
                    if j >= 0 and j <= 2: hash_box[3][board[i][j]] += 1
                    if j >= 3 and j <= 5: hash_box[4][board[i][j]] += 1
                    if j >= 6 and j <= 8: hash_box[5][board[i][j]] += 1
                if i >= 6 and i <= 8:
                    if j >= 0 and j <= 2: hash_box[6][board[i][j]] += 1
                    if j >= 3 and j <= 5: hash_box[7][board[i][j]] += 1
                    if j >= 6 and j <= 8: hash_box[8][board[i][j]] += 1
    for i in range(9):
        c, d, e = hash_row[i], hash_col[i], hash_box[i]
        for key, value in c.items():
            if value >= 2:
                return False
        for key, value in d.items():
            if value >= 2:
                return False
        for key, value in e.items():
            if value >= 2:
                return False
    return True