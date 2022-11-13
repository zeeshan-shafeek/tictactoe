from utils import TicTacToe

game = TicTacToe()

while 1:
    turn_result = ''

# X's turn
    while turn_result == 'occupied' or turn_result == '':
        try:
            turn_result = game.x_turn(input("X's turn, Enter location (1 - 9): "))
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

# O's Turn
    while turn_result == 'occupied' or turn_result == '':
        try:
            turn_result = game.o_turn(input("O's turn, Enter location(1 - 9): "))
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
