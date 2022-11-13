from utils import TicTacToe


rows = 5
game = TicTacToe(rows, rows)

while 1:
    turn_result = ''

    # X's turn
    while turn_result == '':
        try:
            turn_result = game.x_turn(input(f"X's turn, Enter location (1 - {rows*rows}): "))
        except ValueError:
            print('Invalid Location!')
        except IndexError:
            print('Invalid Location!')
        if turn_result == 'win':
            print("*******   X wins!   *******")
            input("press enter to quit...")
            quit()
        elif turn_result == 'draw':
            print("*******   Draw!   *******")
            input("press enter to quit...")
            quit()
        elif turn_result == 'occupied':
            print("location already occupied!")
            turn_result = ''

    turn_result = ''

    # O's Turn
    while turn_result == '':
        try:
            turn_result = game.o_turn(input(f"O's turn, Enter location(1 - {rows*rows}): "))
        except ValueError:
            print("Invalid Location!")
        except IndexError:
            print('Invalid Location!')
        if turn_result == 'win':
            print("*******   O wins!   *******")
            input("press enter to quit...")
            quit()
        elif turn_result == 'occupied':
            print("location already occupied!")
            turn_result = ''

