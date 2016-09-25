
def rotate(matrix):
    N = len(matrix)
    
    for depth in range(N//2):
        for i in range(depth, N-depth-1):
            
            top = list(matrix[depth])
            # left->top
            matrix[depth][i] = matrix[~i][depth]
            # bot->left
            matrix[~i][depth] = matrix[~depth][~i]
            # right -> bot
            matrix[~depth][~i] = matrix[i][~depth]
            # top -> right
            matrix[i][~depth] = top[i]

    return matrix



if __name__ == '__main__':

    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
    ]
    rotate(matrix)
    assert matrix == [
        [7, 4, 1],
        [8, 5, 2],
        [9, 6, 3],
    ]