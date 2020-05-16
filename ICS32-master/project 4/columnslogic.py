#Arvind Kumar
#18274348
#Game Logic for Columns
gameboard = []

class Faller:
    def __init__ (self, col: int, first: 'char', second: 'char', third: 'char') -> None:
        self.col = col - 1
        self.row = 0
        self.first = first
        self.second = second
        self.third = third
        self.didItLand = False
        self.GameOverLand = False
        self.GameOver = False
        gameboard[0][self.col][0] = '[' + third + ']'
        if gameboard[1][self.col][0] != 0:
            gameboard[0][self.col][0] = '|' + third + '|'
            self.GameOver = True

    def landed (self) -> None:
        if self.row == 1:
            gameboard[0][self.col][0] = '|' + self.third + '|'
        elif self. row == 2:
            gameboard[0][self.col][0] = '|' + self.first + '|'
            gameboard[1][self.col][0] = '|' + self.second + '|'
            gameboard[2][self.col][0] = '|' + self.third + '|'
        else:
            gameboard[self.row -2][self.col][0] = '|' + self.first + '|'
            gameboard[self.row-1][self.col][0] = '|' + self.second + '|'
            gameboard[self.row][self.col][0] = '|' + self.third + '|'
        self.didItLand = True

    def goAway(self) -> None:
        if self.row == 1:
            gameboard[0][self.col][0] = ' ' + self.third + ' '
        elif self. row == 2:
            gameboard[0][self.col][0] = ' ' + self.first + ' '
            gameboard[1][self.col][0] = ' ' + self.second + ' '
            gameboard[2][self.col][0] = ' ' + self.third + ' '
        else:
            gameboard[self.row -2][self.col][0] = ' ' + self.first + ' '
            gameboard[self.row-1][self.col][0] = ' ' + self.second + ' '
            gameboard[self.row][self.col][0] = ' ' + self.third + ' '
        self.didItLand = False

    def dropfaller (self, max_rows: int) -> bool:
        if self.row+1 < max_rows-1 and gameboard[self.row+1][self.col][0] == 0:
            self.row += 1
            if self.row == 1:
                gameboard[0][self.col][0] = '[' + self.second + ']'
                gameboard[1][self.col][0] = '[' + self.third + ']'
            elif self.row == 2:
                gameboard[0][self.col][0] = '[' + self.first + ']'
                gameboard[1][self.col][0] = '[' + self.second + ']'
                gameboard[2][self.col][0] = '[' + self.third + ']'
            else:
                gameboard[self.row -2][self.col][0] = '[' + self.first + ']'
                gameboard[self.row-1][self.col][0] = '[' + self.second + ']'
                gameboard[self.row][self.col][0] = '[' + self.third + ']'
                gameboard[self.row-3][self.col][0] = 0
            if gameboard[self.row+1][self.col][0] != 0:
                self.landed()
        elif self.row+1 < max_rows-1 and gameboard[self.row+1][self.col][0] != 0 and self.row < 2:
            if self.row == 1:
                second = gameboard[0][self.col][0][1]
                third = gameboard[1][self.col][0][1]
                gameboard[0][self.col][0] = '|' + second + '|'
                gameboard[1][self.col][0] = '|' + third + '|'
            self.GameOver = True
        else:
            if self.didItLand != True:
                if self.row+1 == max_rows-1:
                    self.row += 1
                    if self.row == 1:
                        gameboard[0][self.col][0] = '[' + self.second + ']'
                        gameboard[1][self.col][0] = '[' + self.third + ']'
                    elif self.row == 2:
                        gameboard[0][self.col][0] = '[' + self.first + ']'
                        gameboard[1][self.col][0] = '[' + self.second + ']'
                        gameboard[2][self.col][0] = '[' + self.third + ']'
                    else:
                        gameboard[self.row -2][self.col][0] = '[' + self.first + ']'
                        gameboard[self.row-1][self.col][0] = '[' + self.second + ']'
                        gameboard[self.row][self.col][0] = '[' + self.third + ']'
                        gameboard[self.row-3][self.col][0] = 0
                    self.landed()
                else:
                    self.landed()
            else:
                self.goAway()
                rows = len(gameboard)
                cols = len(gameboard[0])
                get_horizontal(rows, cols)
                get_vertical(rows, cols)
                get_right_diagonal(rows, cols)
                get_left_diagonal(rows,cols)
                return False
        return True

    def right(self, max_cols: int) -> None:
        if self.col < max_cols -1 and gameboard[self.row][self.col][0][0] != '|':
            self.col+=1
            if self.row == 0 and gameboard[0][self.col][0] == 0:
                gameboard[0][self.col][0] = '[' + self.third + ']'
                gameboard[0][self.col-1][0] = 0
            elif self.row == 1 and gameboard[0][self.col][0] == 0 and gameboard[1][self.col][0] == 0:
                gameboard[0][self.col][0] = '[' + self.second + ']'
                gameboard[1][self.col][0] = '[' + self.third + ']'
                gameboard[0][self.col-1][0] = 0
                gameboard[1][self.col-1][0] = 0

            elif gameboard[self.row][self.col][0] == 0 and gameboard[self.row-1][self.col][0] == 0 and gameboard[self.row-2][self.col][0] == 0:
                gameboard[self.row -2][self.col][0] = '[' + self.first + ']'
                gameboard[self.row-1][self.col][0] = '[' + self.second + ']'
                gameboard[self.row][self.col][0] = '[' + self.third + ']'
                gameboard[self.row -2][self.col-1][0] = 0
                gameboard[self.row-1][self.col-1][0] = 0
                gameboard[self.row][self.col-1][0] = 0
    def left (self, max_cols: int) -> None:
        if self.col > 0 and gameboard[self.row][self.col][0][0] != '|':
            self.col-=1
            if self.row == 0 and gameboard[0][self.col][0] == 0:
                gameboard[0][self.col][0] = '[' + self.third + ']'
                gameboard[0][self.col+1][0] = 0
            elif self.row == 1 and gameboard[0][self.col][0] == 0 and gameboard[1][self.col][0] == 0:
                gameboard[0][self.col][0] = '[' + self.second + ']'
                gameboard[1][self.col][0] = '[' + self.third + ']'
                gameboard[0][self.col+1][0] = 0
                gameboard[1][self.col+1][0] = 0 
            elif gameboard[self.row][self.col][0] == 0 and gameboard[self.row-1][self.col][0] == 0 and gameboard[self.row-2][self.col][0] == 0:
                gameboard[self.row -2][self.col][0] = '[' + self.first + ']'
                gameboard[self.row-1][self.col][0] = '[' + self.second + ']'
                gameboard[self.row][self.col][0] = '[' + self.third + ']'
                gameboard[self.row -2][self.col+1][0] = 0
                gameboard[self.row-1][self.col+1][0] = 0
                gameboard[self.row][self.col+1][0] = 0
    def rotate (self) -> None:
        first_c = gameboard[self.row][self.col][0][0]
        second_c = gameboard[self.row][self.col][0][2]
        if self.row == 1:
            gameboard[0][self.col][0] = first_c + self.second + second_c
        elif self. row == 2:
            gameboard[0][self.col][0] = first_c + self.third + second_c
            gameboard[1][self.col][0] = first_c + self.first + second_c
            gameboard[2][self.col][0] = first_c + self.second + second_c
        else:
            gameboard[self.row -2][self.col][0] = first_c + self.third + second_c
            gameboard[self.row-1][self.col][0] = first_c + self.first + second_c
            gameboard[self.row][self.col][0] = first_c + self.second + second_c
        temp1 = self.first
        temp2 = self.second
        self.first = self.third
        self.second = temp1
        self.third = temp2


def drop_the_mic(rows:int, cols: int) -> None:
    for x in range(rows-1,-1,-1):
        for y in range(cols):
            if gameboard[x][y][0] != 0:
                temp_row = x
                while temp_row+1 < rows and gameboard[temp_row+1][y][0] == 0:
                    gameboard[temp_row+1][y][0] = gameboard[temp_row][y][0]
                    gameboard[temp_row][y][0] = 0
                    temp_row += 1


def get_horizontal (rows: int, cols: int) -> None:
    for x in range(rows):
        for y in range(cols):
            if y + 1 < cols and gameboard[x][y][0] != 0 and gameboard[x][y+1][0] != 0:
                first = gameboard[x][y][0][1]
                second = gameboard[x][y+1][0][1]
                if y + 2 < cols and first == second and gameboard[x][y+2][0] != 0:
                    third = gameboard[x][y+2][0][1]
                    if second == third and first == third:
                        gameboard[x][y][0] = '*' + first + '*'
                        gameboard[x][y+1][0] = '*' + second + '*'
                        gameboard[x][y+2][0] = '*' + third + '*'
def get_vertical (rows: int, cols: int) -> None:
    for x in range(rows):
        for y in range(cols):
            if x+1 < rows and gameboard[x][y][0] != 0 and gameboard[x+1][y][0] != 0:
                first = gameboard[x][y][0][1]
                second = gameboard[x+1][y][0][1]
                if x+2 < rows and first == second and gameboard[x+2][y][0] != 0:
                    third = gameboard[x+2][y][0][1]
                    if second == third and first ==third: 
                        gameboard[x][y][0] = '*' + first + '*'
                        gameboard[x+1][y][0] = '*' + second + '*'
                        gameboard[x+2][y][0] = '*' + third + '*'

def get_right_diagonal (rows:int, cols:int) -> None:
    for x in range(rows):
        for y in range(cols):
            if x+1<rows and y+1<cols and gameboard[x][y][0] != 0 and gameboard[x+1][y+1][0] !=0:
                first = gameboard[x][y][0][1]
                second = gameboard[x+1][y+1][0][1]
                if x+2<rows and y+2<cols and first == second and gameboard[x+2][y+2][0] != 0:
                    third = gameboard[x+2][y+2][0][1]
                    if second == third and first == third:
                        gameboard[x][y][0] = '*' + first + '*'
                        gameboard[x+1][y+1][0] = '*' + second + '*'
                        gameboard[x+2][y+2][0] = '*' + third + '*'

def get_left_diagonal (rows:int, cols:int) -> None:
    for x in range(rows):
        for y in range(cols):
            if x+1<rows and y-11<cols and gameboard[x][y][0] != 0 and gameboard[x+1][y-1][0] !=0:
                first = gameboard[x][y][0][1]
                second = gameboard[x+1][y-1][0][1]
                if x+2<rows and y-2<cols and first == second and gameboard[x+2][y-2][0] != 0:
                    third = gameboard[x+2][y-2][0][1]
                    if second == third and first == third:
                        gameboard[x][y][0] = '*' + first + '*'
                        gameboard[x+1][y-1][0] = '*' + second + '*'
                        gameboard[x+2][y-2][0] = '*' + third + '*'
                        

def clear_matching(rows: int, cols: int) -> None:
    for x in range(rows):
        for y in range(cols):
            if gameboard[x][y][0] != 0 and gameboard[x][y][0][0] == '*':
                gameboard[x][y][0] = 0
    drop_the_mic(rows, cols)
                

def get_rows() -> int:
    return len(gameboard)

def get_cols() -> int:
    return len(gameboard[0])

def creategameboard (rows: int, cols: int) -> None:
    for r in range(rows):
        row_list = []
        for c in range(cols):
            row_list.append([0])
        gameboard.append(row_list)
