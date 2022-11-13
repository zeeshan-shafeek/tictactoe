import os


class TicTacToe:
    def __init__(self):
        self.matrix = ['1', '2', '3',
                       '4', '5', '6',
                       '7', '8', '9']

        self.matrix_print()

        # clearing the matrix
        self.matrix = [' ', ' ', ' ',
                       ' ', ' ', ' ',
                       ' ', ' ', ' ']

    def matrix_print(self):
        os.system("cls")  # to clear the console after every turn
        print('')
        print(f' {self.matrix[0]} | {self.matrix[1]} | {self.matrix[2]} ')
        print('---|---|---')
        print(f' {self.matrix[3]} | {self.matrix[4]} | {self.matrix[5]} ')
        print('---|---|---')
        print(f' {self.matrix[6]} | {self.matrix[7]} | {self.matrix[8]} ')

    def line_find(self, coordinate1, coordinate2, coordinate3):
        if self.matrix[coordinate1 - 1] == self.matrix[coordinate2 - 1] == self.matrix[coordinate3 - 1]:
            # making sure that we don't mistake empty spaces with a line
            if self.matrix[coordinate1 - 1] != ' ':
                if self.matrix[coordinate2 - 1] != ' ':
                    if self.matrix[coordinate3 - 1] != ' ':
                        return 1

        return 0

    def win_calc(self):
        if self.line_find(1, 2, 3):  # every possible line in TicTacToe
            return 'win'
        elif self.line_find(4, 5, 6):
            return 'win'
        elif self.line_find(7, 8, 9):
            return 'win'
        elif self.line_find(1, 4, 7):
            return 'win'
        elif self.line_find(2, 5, 8):
            return 'win'
        elif self.line_find(3, 6, 9):
            return 'win'
        elif self.line_find(1, 5, 9):
            return 'win'
        elif self.line_find(3, 5, 7):
            return 'win'
        else:
            for cell in range(9):  # checking if there are still empty spaces left
                if self.matrix[cell] == ' ':
                    return 'next turn'
            return 'draw'

    def end_turn(self):

        self.matrix_print()
        return self.win_calc()

    def x_turn(self, location):

        if self.matrix[int(location) - 1] == ' ':
            self.matrix[int(location) - 1] = 'X'
            return self.end_turn()
        else:
            return 'occupied'

    def o_turn(self, location):
        if self.matrix[int(location) - 1] == ' ':
            self.matrix[int(location) - 1] = 'O'
            return self.end_turn()
        else:
            return 'occupied'
