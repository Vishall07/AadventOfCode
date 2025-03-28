f = open("day4input.txt", "r")
strs = ""
for x in f:
    strs += x
print(strs)

grid = strs.split('\n')

print(grid)

def count_xmas(grid):
    rows, cols = len(grid), len(grid[0])
    target = "XMAS"
    target_len = len(target)
    directions = [
        (0, 1), (1, 0), (1, 1), (1, -1), 
        (0, -1), (-1, 0), (-1, -1), (-1, 1) 
    ]
    count = 0
    
    def is_inbound(r, c):
        return 0 <= r < rows and 0 <= c < cols
    
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 'X':
                for dr, dc in directions:
                    if all(is_inbound(r + i * dr, c + i * dc) and grid[r + i * dr][c + i * dc] == target[i] for i in range(target_len)):
                        count += 1
    return count


print(count_xmas(grid))


def xmas_patterns(grid):
    rows = len(grid)
    cols = len(grid[0])
    count = 0

    for r in range(1,rows-1):
        for c in range(1,cols-1):
            if grid[r][c] == 'A':  
                if(grid[r-1][c-1] == 'M' and  grid[r+1][c-1] == 'M' and grid[r-1][c+1] == 'S' and  grid[r+1][c+1] == 'S' ):
                    count += 1
                if(grid[r-1][c-1] == 'M' and  grid[r+1][c-1] == 'S' and grid[r-1][c+1] == 'M' and  grid[r+1][c+1] == 'S' ):
                    count += 1
                if(grid[r-1][c-1] == 'S' and  grid[r+1][c-1] == 'S' and grid[r-1][c+1] == 'M' and  grid[r+1][c+1] == 'M' ):
                    count += 1
                if(grid[r-1][c-1] == 'S' and  grid[r+1][c-1] == 'M' and grid[r-1][c+1] == 'S' and  grid[r+1][c+1] == 'M' ):
                    count += 1
    return count


result = xmas_patterns(grid)
print(result)  