
def zeroify(matrix):
    m = len(matrix)
    n = len(matrix[0])

    rows = [0]*m
    cols = [0]*n

    for i, y in enumerate(matrix):
        for j, x in enumerate(y):
            if x == 0:
                rows[j] = 1
                cols[i] = 1

    for i, y in enumerate(matrix):
        for j, x in enumerate(y):
            if cols[i] or rows[j]:
                matrix[i][j] = 0
    
    return matrix


if __name__ == '__main__':
    matrix = [
        [0, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
    ]

    zeroify(matrix)
    assert matrix == [
        [0, 0, 0],
        [0, 5, 6],
        [0, 8, 9],        
    ]

    m2 = [
            [1, 2, 3, 4, 0],
            [6, 0, 8, 9, 10],
            [11, 12, 13, 14, 15],
            [16, 0, 18, 19, 20],
            [21, 22, 23, 24, 25]
        ]
    zeroify(m2)
    assert m2 == [
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [11, 0, 13, 14, 0],
            [0, 0, 0, 0, 0],
            [21, 0, 23, 24, 0]
        ]