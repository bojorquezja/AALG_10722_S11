def impmat(mat):
    for l in mat:
        print(l) 
    print()
    
lab = [
    [1,0,0,0],
    [1,1,1,1],
    [0,1,0,0],
    [1,1,1,1]
]
res = [[0 for _ in range(4)] for _ in range(4)]
impmat(res)

