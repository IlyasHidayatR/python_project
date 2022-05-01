#solve sudoku game with AI backtracking
board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]

def print_board(bo):
    for i in range(len(bo)): #row
        if i % 3 == 0 and i != 0: #print line
            print("- - - - - - - - - - - - - ")
        for j in range(len(bo[0])): #col
            if j % 3 == 0 and j != 0: #print |
                print(" | ", end="")
            if j == 8: #print new line
                print(bo[i][j])
            else: #print number
                print(str(bo[i][j]) + " ", end="")


def find_empty(bo):
    for i in range(len(bo)): #row
        for j in range(len(bo[0])): #col
            if bo[i][j] == 0: #if empty space
                return (i, j)  # row, col
    return None


def valid(bo, num, pos):
    # Check row
    for i in range(len(bo[0])): #col
        if bo[pos[0]][i] == num and pos[1] != i: #check if number is in row
            return False #number is in row

    # Check column
    for i in range(len(bo)): #row
        if bo[i][pos[1]] == num and pos[0] != i: #check if number is in col
            return False #number is in col

    # Check box
    box_x = pos[1] // 3 #col
    box_y = pos[0] // 3 #row

    for i in range(box_y*3, box_y*3 + 3): #row
        for j in range(box_x * 3, box_x*3 + 3): #col
            if bo[i][j] == num and (i,j) != pos: #check if number is in box
                return False #number is in box

    return True #number is valid


def solve(bo):
    find = find_empty(bo) #find empty space
    if not find: #if no empty space
        return True #solved
    else: #if empty space
        row, col = find #row, col

    for i in range(1, 10): #try numbers 1-9
        if valid(bo, i, (row, col)): #check if number is valid
            bo[row][col] = i #if valid, set number

            if solve(bo): #if solved
                return True #solved

            bo[row][col] = 0 #if not solved, set number to 0

    return False #not solved


print_board(board)
solve(board)
print("___________________")
print("Solve:")
print_board(board)