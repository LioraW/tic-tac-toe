#Tic Tac Toe Game By Liora Wachsstock
#Finished 1/20/2020


#computer turn generator library:
from random import randint

#Heading
print("Let's Play Tic Tac Toe!")
print("-----------------------")
print("")
# The origonal board and the function to print the board:
board = [["   ", "|","   ", "|","   "], ["---", "+", "---", "+", "---"], ["   ", "|","   ", "|","   "], ["---", "+", "---", "+", "---"], ["   ", "|","   ", "|","   "]]

def print_board(board_array):
    for row in board_array:
        print("".join(row))
print_board(board)

#Two player or one player game?
mode_choice = input('Would you like to play against another human or against the computer? Type "human" or "computer":').lower()
while mode_choice != "human" and mode_choice != "computer":
    mode_choice = input("We don't offer that version yet. Coming soon to the next version: demi-god. For now, choose human or computer.").lower()

#check if someone wins
def game_win(mode):
    x_wins = False
    o_wins = False
    cats_game = False
    #check if X won (horizontal, vertical, diagonal)
    #horizontal:
    for row in range (0, 3):
        if board[row*2][0] == " X " and board[row*2][2] == " X " and board[row*2][4] == " X ":
             x_wins = True
    #vertical:
    for col in range(0, 3):
         if board[0][col*2] == " X " and board[2][col*2] == " X " and board[4][col*2] == " X ":
            x_wins = True
    #diagonal:
    if board[0][0] == " X " and board[2][2] == " X " and board[4][4] == " X ":
        x_wins = True
    if board[0][4] == " X " and board[2][2] == " X " and board[4][0] == " X ":
        x_wins = True

    #check if O won (horizontal, vertical, diagonal):
    # horizontal:
    for row in range(0, 3):
        if board[row * 2][0] == " O " and board[row * 2][2] == " O " and board[row * 2][4] == " O ":
            o_wins = True
    # vertical:
    for col in range(0, 3):
        if board[0][col * 2] == " O " and board[2][col * 2] == " O " and board[4][col * 2] == " O ":
            o_wins = True
    # diagonal:
    if board[0][0] == " O " and board[2][2] == " O " and board[4][4] == " O ":
        o_wins = True
    if board[0][4] == " O " and board[2][2] == " O " and board[4][0] == " O ":
        o_wins = True

    #check if it's a cat's game:
    for row in range(0,5):
        for col in range (0,5):
            if board[row][col] == "   ":
                cats_game = False
                break
            else:
                cats_game = True
        if not cats_game:
            break

    #if someone wins or it's a cats game, display message. If not, move on in life:
    if x_wins:
        if mode == "human":
            print ("Congrats, human, you won! You are smarter than a dumb computer.")
        elif mode == "computer":
            print("Congrats player one, you won!")
        print_board(board)
        return True
    elif o_wins:
        if mode == "human":
            print("Congrats player two, you won!")
        elif mode == "computer":
            print("Congrats computer, somehow you managed to win! This human must be pretty stupid. Sorry human.")
        print_board(board)
        return True
    elif cats_game:
        print("It's a cat's game. Meow.")
        print_board(board)
        return True
    else:
        return False

# Human Player
def player_row_choice():
    choose_a_row = int(input("Which row do you want to choose?"))-1
    while not choose_a_row <= 2 or not choose_a_row >= 0:
        choose_a_row = int(input("This is only a 3x3 board. Please choose a row, 1-3:"))-1
    return choose_a_row*2

def player_col_choice():
    choose_a_column = int(input("which column do you want to choose?"))-1
    while not choose_a_column <= 2 or not choose_a_column >= 0:
        choose_a_column = int(input("This is only a 3x3 board. Please choose a column, 1-3:"))-1
    return choose_a_column*2

def insert_player_choice(player, row, column):
    if board[row][column] == " X " or board[row][column] == " O ":
        print("That place is already filled. Try again. ")
        #true means the loop that calls the fuction has to do it again.
        return True
    if player == "player1":
        board[row][column] = " X "
    elif player == "player2":
        board[row][column] = " O "
        #false means the loops that calls the fuction does not have to call it again.
    return False

#Computer player
def computer_choice():
    row = randint(0, 2)*2
    col = randint(0, 2)*2
    while not board[row][col] == "   ":
        row = randint(0, 2)*2
        col = randint(0, 2)*2
    board[row][col] = " O "

#Game play:
    #Human vs. computer
def game_play(mode):
    if mode == "computer":
        while not game_win(mode):
            #player1's turn
            print ("It's your turn!")
            while insert_player_choice("player1", player_row_choice(), player_col_choice()):
                if game_win(mode):
                    return
                continue
            print_board(board)

            # Computer's turn!
            computer_choice()
            if game_win(mode):
                return
            print("Now it's the computer's turn!")
            print_board(board)

    # Human vs Human
    elif mode == "human":
        while not game_win(mode):
            # player 1's turn
            print("It's player one's turn!")
            while insert_player_choice("player1", player_row_choice(), player_col_choice()):
                if game_win(mode):
                    return
                continue
            print_board(board)

            if game_win(mode):
                break

            #player 2's turn
            print ("It's player two's turn!")
            while insert_player_choice("player2", player_row_choice(), player_col_choice()):
                if game_win(mode):
                    return
                continue
            print_board(board)


game_play(mode_choice)

while(input("Would you like to play again? type 'yes' or 'no':").lower() == "yes"):
    board = [["   ", "|", "   ", "|", "   "], ["---", "+", "---", "+", "---"], ["   ", "|", "   ", "|", "   "],
             ["---", "+", "---", "+", "---"], ["   ", "|", "   ", "|", "   "]]
    game_play(mode_choice)