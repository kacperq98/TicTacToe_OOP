import shutil

import TicTacToe_class as Board


column = shutil.get_terminal_size().columns

print("\n" + 8*('------------------'))
print("Let's play!\n".center(column))

player = Board.Board.input_and_validation()
board = Board.Board(player)


while (not board.check_if_win()) and (not board.check_if_draw()):
    board.show_board()

    try:
        print()
        x, y = [(x) for x in input(
            "Type a coordinates where you want to put your sign (you need split them by using space).\n"). split()]

        print()
        board.put_to_board(x, y)

    except ValueError:
        board.quit(x, y)
        print("\n*** You have typed bad coordinates. Try again. *** \n ")

print()
board.show_board()
print()
if board.check_if_win():
    if board.get_player() == "X":
        print("*** Player 'O' wins! ***\n")

    else:
        print("*** Player 'X' wins! ***\n")
else:
    print("*** It's a draw! ***\n")
