def impmat(mat):
    for l in mat:
        print(l) 
    print()

def valida(lab, f, c):
    if f < 0 or c < 0:
        return False
    if f >= len(lab) or c >= len(lab[0]):
        return False
    if lab[f][c] == 0:
        return False
    if res[f][c] == 1:
        return False
    return True

def labbas(lab, res, f, c):
    if f == len(lab)-1 and c == len(lab[0])-1:
        if valida(lab, f, c):
            res[f][c] = 1
            return True
        else:
            return False
    else:
        if valida(lab, f, c):
            res[f][c] = 1
            impmat(res)
            if labbas(lab, res, f+1, c):
                return True
            elif labbas(lab, res, f, c+1):
                return True
            elif labbas(lab, res, f-1, c):
                return True
            elif labbas(lab, res, f, c-1):
                return True
            else:
                res[f][c] = 0
                return False
        else:
            return False

lab = [
    [1,1,1,1,0,1,1,1,1],
    [1,0,0,1,0,1,0,0,0],
    [1,1,0,1,1,1,1,0,1],
    [0,1,0,1,0,0,1,0,1],
    [1,1,1,1,1,1,1,1,1],
    [1,0,1,0,0,0,1,0,1],
    [1,1,1,1,0,1,1,0,1],
    [1,0,0,1,0,1,0,0,1],
    [1,1,1,1,0,1,1,1,1]
]

res = [[0 for _ in range(9)] for _ in range(9)]

if labbas(lab, res, 0, 0):
    impmat(res)
    print("Salimos")
else:
    print("Ayuda, no hay salida")