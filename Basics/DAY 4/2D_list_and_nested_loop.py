number_grid = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [0]
]
print(number_grid[0][0])

#for row in number_grid:
#    for colomn in row:
#        print(colomn)
for row in number_grid:
    for colomn in range(len(row)):
        print(number_grid[colomn])