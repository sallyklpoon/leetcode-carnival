"""
Toggle = choose a column or row to invert
ex. row = 0, 1, 0, 1 --> toggle --> 1, 0, 1, 0

- no moves indicated, input is matrix
- return the highest sum or value we can get from every row

1110
1111
1001
1111

- a binary number is greatest with more 1s ++ more 1s to the left side of the grid
- Row: I want to toggle in a way that increases more 1s on the left side (MSB)
- Columns: I want as many 1s as possible

1. Iterate through every row.
 - MSB that is 1 will always be > even if remaining bits are one

2. Iterate through every column and check if we have 'enough 1s'
 - We toggle if sum of the 1s is < half of number of rows

3. sum up all the numbers and return
"""


def matrix_score(grid: list) -> int:
    rows, cols = len(grid), len(grid[0])

    # go through the rows and toggle if needed
    for i in range(rows):
        if grid[i][0] == 0:
            for j in range(cols):
                grid[i][j] ^= 1

    # go through the columns and flag for toggle if needed
    flag = [0] * cols
    for j in range(cols):
        col = []
        for i in range(rows):
            col.append(grid[i][j])
        if sum(col) <= rows / 2:
            flag[j] = 1

    for j in range(cols):
        if flag[j]:
            for i in range(rows):
                grid[i][j] ^= 1

    ans = 0
    for i in range(rows):
        ans += int(''.join([str(digit) for digit in grid[i]]), 2)

    return ans


print(matrix_score([[0, 0, 1, 1], [1, 0, 1, 0], [1, 1, 0, 0]]))
