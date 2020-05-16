#Arvind Kumar
#18274348
#Columns game

import columnslogic

def typeofgames (typeofgames: str, rows: int, cols: int) -> None:
    if gametype == 'EMPTY':
        print_board(rows, cols)
    elif gametype == 'CONTENTS':
        for i in range(rows):
            row_input = input()
            for j in range(cols):
                if row_input[j] == ' ':
                    columnslogic.gameboard[i][j][0] = 0
                else:
                    columnslogic.gameboard[i][j][0] = ' ' + row_input[j] + ' '
        columnslogic.drop_the_mic(rows, cols)
        print_board(rows, cols)

def print_board (rows: int, cols: int) -> None:
    for r in range(rows):
        row_str = '|'
        for c in range(cols):
            if columnslogic.gameboard[r][c][0] == 0:
                row_str += '   '
            else:
                if columnslogic.gameboard[r][c][0][0] == '|':
                    row_str += columnslogic.gameboard[r][c][0]
                elif columnslogic.gameboard[r][c][0][0] == ' ':
                    row_str += ' ' + columnslogic.gameboard[r][c][0][1] + ' '
                else:
                    row_str += columnslogic.gameboard[r][c][0]
        print(row_str + '|')
    bottom = ' '
    for c in range(cols):
        bottom += '---'
    print(bottom + ' ')
        

def play_game(rows: int, cols: int,) -> None:
    is_quit = False
    faller_present = False
    gameover = False
    while not gameover:
        move = input()
        if move != "" and move[0] == 'F':
            possible = 'STVWXYZ'
            if move[4] in possible and move[6] in possible and move[8] in possible:
                dropper = columnslogic.Faller(int(move[2]), move[4], move[6], move[8])
                faller_present = True
                gameover = dropper.GameOver
        elif move == "":
            if faller_present == True:
                exists = dropper.dropfaller(columnslogic.get_rows())
                gameover = dropper.GameOver
                if exists == False:
                    faller_present = False
            else:
                columnslogic.clear_matching(rows, cols)
        elif move == '>':
            dropper.right(columnslogic.get_cols())
        elif move == '<':
            dropper.left(columnslogic.get_cols())
        elif move == 'R':
            dropper.rotate()
        elif move == 'Q':
            is_quit = True
            break
        
        print_board(columnslogic.get_rows(), columnslogic.get_cols())
    if gameover:
        print("Game Over")
        
        

        
if __name__== '__main__':
    rows = int(input())
    cols = int(input())
    gametype = str(input())
    columnslogic.creategameboard(rows, cols)
    typeofgames(gametype, rows, cols)
    play_game(rows, cols)
  
