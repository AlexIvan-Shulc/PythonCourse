a = [
    [2, 5, 7, 3, 5],
    [3, 11, 43, 2, 9],
    [5, 8, 32, 13, 6],
    [4, 2, 1, 4, 8]
]

for i in reversed(range(len(a))):
    for j in reversed(range(len(a[i]))):
        if a[i][j] == 13:
            for n in a:
                n.pop(j)

print(a)



