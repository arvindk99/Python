import connectfour
import connectfour_tools


def movechecker(gamestate,column,move) -> 'current_gamestate':
    ''' This function will take in the game state and column input
        and ask the user if they want to drop or pop.
        Then it will perform the action, and return the new current game state.
        If it is an invalid move, it will ask the user to re-input the moves.
        If the game is over, it will print game over.'''
    while True:
        try:
            if move == 'DROP':
                current_gamestate = connectfour.drop(gamestate, column)
                print("MOVE: " + move + ' {}'.format(column + 1))
                return current_gamestate

            
            elif move == 'POP':
                current_gamestate = connectfour.pop(gamestate, column)
                print("MOVE: " + move + ' {}'.format(column + 1))
                return current_gamestate

            
        except connectfour.InvalidMoveError:
            print("INVALID MOVE ERROR")
            column = connectfour_tools.columninput()
            move = connectfour_tools.moveinput()
            
        except connectfour.GameOverError:
            print("Game is over.")
            break
        

def console():
    '''This function runs the game from start to finish.
        It will first starta  new game, then while there is no winner, it will loop between
        the red player and the yellow player. Once there is a winner, it will print the winner and end the program.'''
    gamestate = connectfour_tools.gamestart()
    winner = connectfour.winner(gamestate)
    turn = connectfour_tools.turnchecker(gamestate)
    
    while winner == connectfour.NONE:
        if turn == connectfour.RED:
            print("Red player's turn.")
            column = connectfour_tools.columninput()
            move = connectfour_tools.moveinput()
            gamestate = movechecker(gamestate,column,move)
            connectfour_tools.gameboard(gamestate)
            winner = connectfour.winner(gamestate)
            turn = connectfour_tools.turnchecker(gamestate)

            
        elif turn == connectfour.YELLOW:
            print("Yellow player's turn.")
            column = connectfour_tools.columninput()
            move = connectfour_tools.moveinput()
            gamestate = movechecker(gamestate,column, move)
            connectfour_tools.gameboard(gamestate)
            winner = connectfour.winner(gamestate)
            turn = connectfour_tools.turnchecker(gamestate)

    if winner == connectfour.RED:
        print("Red player wins.")
        
    else:
        print("Yellow player wins.")


if __name__ == "__main__":
    console()
