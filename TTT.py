from os import system
from random import randint
clear = lambda: system('cls')


def display_board(board):
    clear()
    print("   |   |   ")
    print(board[7] + "  | " + board[8] + " |  " + board[9])
    print("___|___|___")
    print("   |   |   ")
    print(board[4] + "  | " + board[5] + " |  " + board[6])
    print("   |   |   ")
    print("___|___|___")
    print("   |   |   ")
    print(board[1] + "  | " + board[2] + " |  " + board[3])
    print("   |   |   ")


test_board = ['0', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X']
# display_board(test_board)


def player_input():
    marker = ''
    while marker not in ("X", "O"):
        marker = input("Player 1: Choose your marker X or O: ")
        if marker not in ("X", "O"):
            print('Sorry, you have to choose X or O')
    if marker == "X":
        return ("X", "O")
    else:
        return ("O", "X")


def place_marker(board, position, marker):
    board[position] = marker


# place_marker(test_board, 2, "$")
# display_board(test_board)


def win_check(board, mark):
    return (
            (board[7] == mark and board[8] == mark and board[9] == mark) or
            (board[4] == mark and board[5] == mark and board[6] == mark) or
            (board[1] == mark and board[2] == mark and board[3] == mark) or
            (board[7] == mark and board[4] == mark and board[1] == mark) or
            (board[8] == mark and board[5] == mark and board[2] == mark) or
            (board[9] == mark and board[6] == mark and board[3] == mark) or
            (board[7] == mark and board[5] == mark and board[3] == mark) or
            (board[1] == mark and board[5] == mark and board[9] == mark)
    )


# print(win_check(test_board, "X"))


def space_check(board, position):
    return board[position] == " "


def full_board_check(board):
    for i in range(1, 10):
        if space_check(board, i):
            return False
    return True


def choose_first():
    flip = randint(0, 1)
    if flip == 0:
        return 'Player 1'
    else:
        return 'Player 2'


def player_choice(board):
    position = 0
    while position not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not space_check(board, position):
        position = int(input("Choose your position (1-9): "))
        if position not in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
            print('Sorry, Make sure choose (1-9).')
    return position


def replay():
    choice = "Wrong"
    while choice not in ("Yes", "No"):
        choice = input('Do you want to play again? Yes or No: ')
        if choice not in ("Yes", "No"):
            print("Sorry, I don't understand. Yes or No.")
    return choice == "Yes"


print('Welcome to Tic Tac Toe!!')

while True:
    the_board = [" "] * 10
    display_board(the_board)
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print(turn, "will go first.")
    play_game = input("DO YOU WANT TO PLAY GAME? Yes or No: ")
    if play_game == "Yes":
        game_on = True
    else:
        game_on = False

    while game_on:
        if turn == "Player 1":
            display_board(the_board)
            position = player_choice(the_board)
            place_marker(the_board, position, player1_marker)
            if win_check(the_board, player1_marker):
                display_board(the_board)
                print("Player 1: Has Won !")
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print('TIE GAME !')
                    game_on = False
                else:
                    turn = "Player 2"
        else:
            display_board(the_board)
            position = player_choice(the_board)
            place_marker(the_board, position, player2_marker)
            if win_check(the_board, player2_marker):
                display_board(the_board)
                print('Player 2: Has Won !')
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print("TIE GAME !")
                    game_on = False
                else:
                    turn = "Player 1"
    if not replay():
        break
print('GOOD LUCK :)')
