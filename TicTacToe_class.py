import sys 

class Board:
    """A class representing a main board in game."""

    def __init__(self, player):
        self.board = [['.'] * 3 for i in range(3)]
        self.player = player
        self.win = False

    def input_and_validation():
        while True:
            player = input("Who start the game? Type (X/O) depend on what you would like play or type 'Q' to exit:\n")
            player = player.upper()
            if player == "Q":
                print("Goodbye")
                sys.exit()
            if player == "X" or player == "O":
                return player
                



    def check_if_win(self):                     # Checking the layout on board and conditions of win.


        for x in range(0, 3):
            if self.board[x][0] == self.board[x][1] and self.board[x][1] == self.board[x][2] and (self.board[x][2] == "X" or self.board[x][2] == "O"):
                self.win = True
                return True

            if self.board[0][x] == self.board[1][x] and self.board[1][x] == self.board[2][x] and (self.board[2][x] == "X" or self.board[2][x] == "O"):
                self.win = True
                return True

        if self.board[0][0] == self.board[1][1] and self.board[1][1] == self.board[2][2] and (self.board[2][2] == "X" or self.board[2][2] == "O"):
            self.win = True
            return True

        if self.board[0][2] == self.board[1][1] and self.board[1][1] == self.board[2][0] and (self.board[2][0] == "X" or self.board[2][0] == "O"):
            self.win = True
            return True

        return False

    def check_if_draw(self):                    # Checking the layout on the board when nobody win.

        if not self.check_if_win():
            for row in self.board:
                for element in row:
                    if element == ".":
                        return False
            return True
        else:
            return False

    def show_board(self):

        print("  1 2 3")
        numberRow = 1
        for row in self.board:
            print(numberRow, end=" ")
            for element in row:
                print(element, end=" ")
            print()
            numberRow += 1

    def check_if_free(self, x, y):              # Checking that the place in the board is free.
        return self.board[int(x)-1][int(y)-1] == "."

    def change_player(self):
        if self.player == "O":
            self.player = "X"
        else:
            self.player = "O"

    def put_to_board(self, x, y):               # Insert a X or O using the coordinates on the board.
        try:
            if self.check_if_free(x, y):
                self.board[int(x)-1][int(y)-1] = self.player
                self.change_player()
            else:
                print("\n*** This place is taken. Try again. ***\n")

        except IndexError:
            print("*** You have typed bad coordinates. Try again. *** \n ")

    def get_player(self):
        return self.player

    def quit(self, x , y):
        if str(x).upper() == 'Q' or str(y).upper()== 'Q':
            print('Goodbye!')
            sys.exit()
    
