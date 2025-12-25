def find_saddle_point_coordinates(grid):
    for r in range(len(grid)):
        for c in range(len[r]):
            a = min(grid[r])
            b = min(grid[c])
            return (a, b)
        
Grid= [[1, 2, 3],
 [4, 5, 6],
 [7, 8, 9]]
print(find_saddle_point_coordinates(Grid))