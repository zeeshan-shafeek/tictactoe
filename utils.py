import os


class TicTacToe:
    def __init__(self, rows, columns):

        self.rows = rows
        self.columns = columns
        self.matrix = []
        for cell in range(rows * columns):
            self.matrix.append(cell + 1)
        # self.matrix = ['1', '2', '3',
        #                '4', '5', '6',
        #                '7', '8', '9']
        cell = 0
        self.matrix_print()

        # clearing the matrix
        for cell in range(rows * columns):
            self.matrix[cell] = ' '

        # self.matrix = [' ', ' ', ' ',
        #                ' ', ' ', ' ',
        #                ' ', ' ', ' ']

    def matrix_print(self):
        os.system("cls")  # to clear the console after every turn
        print('')

        for row in range(self.rows):

            print(end=' ')
            for column in range(self.columns):
                print(f'{self.matrix[column + row * self.columns]}', end='')
                if column != self.columns - 1:
                    print(end=' | ')
            print()
            if row != self.rows - 1:
                for i in range(self.columns):
                    print(end='---')
                    if i != self.columns - 1:
                        print(end='|')
                print()

        # print(f' {self.matrix[0]} | {self.matrix[1]} | {self.matrix[2]} ')
        # print('---|---|---')
        # print(f' {self.matrix[3]} | {self.matrix[4]} | {self.matrix[5]} ')
        # print('---|---|---')
        # print(f' {self.matrix[6]} | {self.matrix[7]} | {self.matrix[8]} ')

    def win_calc(self):

        draw = 1
        for cell in range(self.rows * self.columns):  # checking if there are still empty spaces left
            if self.matrix[cell] == ' ':
                draw = 0
                break
        if draw == 1:
            return 'draw'

        # checking rows
        for row in range(self.rows):
            win = 0
            for column in range(self.columns):
                if self.matrix[row * self.columns] == self.matrix[column + row * self.columns] != ' ':
                    win = 1
                else:
                    win = 0
                    break
            if win == 1:
                return 'win'

        row, column, win = 0, 0, 0

        # checking Columns
        for column in range(self.columns):
            win = 0
            for row in range(self.rows):
                if self.matrix[column] == self.matrix[column + row * self.columns] != ' ':
                    win = 1
                else:
                    win = 0
                    break
            if win == 1:
                return 'win'
        i, win = 0, 0
        # Checking Diagonally
        for i in range(self.rows - 1):
            if self.matrix[0] == self.matrix[(i + 1) * (self.rows + 1)] != ' ':
                win = 1
            else:
                win = 0
                break
        if win:
            return 'win'

        i, win = 0, 0

        for i in range(self.rows-1):
            if self.matrix[self.rows - 1] == self.matrix[(i+2) * (self.rows - 1)] != ' ':
                win = 1
            else:
                win = 0
                break
        if win:
            return 'win'
        return 'next turn'

        # if self.line_find(1, 2, 3):  # every possible line in TicTacToe
        #     return 'win'
        # elif self.line_find(4, 5, 6):
        #     return 'win'
        # elif self.line_find(7, 8, 9):
        #     return 'win'
        # elif self.line_find(1, 4, 7):
        #     return 'win'
        # elif self.line_find(2, 5, 8):
        #     return 'win'
        # elif self.line_find(3, 6, 9):
        #     return 'win'
        # elif self.line_find(1, 5, 9):
        #     return 'win'
        # elif self.line_find(3, 5, 7):
        #     return 'win'
        # else:
        #     for cell in range(9):  # checking if there are still empty spaces left
        #         if self.matrix[cell] == ' ':
        #             return 'next turn'
        #     return 'draw'

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
