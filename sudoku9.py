def impmat(mat):
    for l in mat:
        print(l) 
    print()

def sigPosDisp(mat):
    for f in range(len(mat)):
        for c in range(len(mat[0])):
            if mat[f][c] == 0:
                return f, c
    return -1, -1

def valida(mat,f, c, val):
    for fil in range(len(mat)):
        if mat[fil][c] == val:
            return False

    for col in range(len(mat[0])):
        if mat[f][col] == val:
            return False

    nf = f // 3
    nc = c // 3

    minf, maxf = nf*3, nf*3 + 3
    minc, maxc = nc*3, nc*3 + 3

    for fil in range(minf, maxf):
        for col in range(minc, maxc):
            if mat[fil][col] == val:
                return False
    return True


def sudoku9(mat):
    f, c = sigPosDisp(mat)
    if f == -1 and c == -1:
        return True
    else:
        for val in range(1,10):
            if valida(mat, f, c, val):
                mat[f][c] = val
                if sudoku9(mat):
                    return True
                else:
                    mat[f][c] = 0
        return False

mat = [
    [0, 6, 0, 1, 0, 4, 0, 5, 0],
    [0, 0, 8, 3, 0, 5, 6, 0, 0],
    [2, 0, 0, 0, 0, 0, 0, 0, 1],
    [8, 0, 0, 4, 0, 7, 0, 0, 6],
    [0, 0, 6, 0, 0, 0, 3, 0, 0],
    [7, 0, 0, 9, 0, 1, 0, 0, 4],
    [5, 0, 0, 0, 0, 0, 0, 0, 2],
    [0, 0, 7, 2, 0, 6, 9, 0, 0],
    [0, 4, 0, 5, 0, 8, 0, 7, 0]
]


if sudoku9(mat):
    impmat(mat)
    print("Solución")

else:
    print("Ayuda, no hay salida")