def impmat(mat):
    for l in mat:
        print(l) 
    print()

def sigPosDisp(mat):
    for f in range(len(mat)):
        for c in range(len(mat[0])):
            if mat[f][c] == 0:
                return f,c
    return -1, -1

def valida(mat,f, c, val):
    for fil in range(len(mat)):
        if mat[fil][c] == val:
            return False
    for col in range(len(mat[0])):
        if mat[f][col] == val:
            return False
    nc = c//2
    nf = f//2
    minc, maxc = (0,2) if nc == 0 else (2,4)
    minf, maxf = (0,2) if nf == 0 else (2,4)
    
    for fil in range(minf, maxf):
        for col in range(minc, maxc):
            if mat[fil][col] == val:
                return False
    return True

def sudoku4(mat ):
    
    f, c = sigPosDisp(mat)
    #print(f"sig ({f},{c})")
    if f == -1 and c == -1:
        return True
    else:
        for val in range(1,4+1):
            #print(f"P{f},{c} = {val}")
            if valida(mat, f, c, val):
                mat[f][c] = val
                impmat(mat)
                if sudoku4(mat ):
                    return True
                else:
                    mat[f][c] = 0
                    return False
        return False

mat = [
    [0,0,2,0],
    [4,2,0,0],
    [0,0,0,0],
    [2,0,0,0]
]
print(f"X{0},{0} = {mat[0][0]}")
if sudoku4(mat):
    impmat(mat)
    print("Solucion")
else:
    print("Ayuda, no hay salida")
