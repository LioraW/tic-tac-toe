# for computer turn generator library and Enum:
from typing import Any

from random import randint
from enum import Enum


class Winner(Enum):
    NO_WIN = 0
    CATS_GAME = 1
    X_WIN = 2
    O_WIN = 3


class Board:
    def __init__(self):
        self.boardArray = [["   ", "|", "   ", "|", "   "], ["---", "+", "---", "+", "---"],
                           ["   ", "|", "   ", "|", "   "], ["---", "+", "---", "+", "---"],
                           ["   ", "|", "   ", "|", "   "]]
        self.gameWon = False
        self.winner = Winner.NO_WIN

    def display_board(self):
        for row in self.boardArray:
            print("".join(row))

    def spot_is_filled(self, row, column):
        if self.boardArray[row][column] == "   ":
            return False
        else:
            return True

    def insert_player_choice(self, playerSymbol, row, column):
        # to accommodate the other deliminators in the board like +, -, |
        row = row * 2
        column = column * 2

        if self.spot_is_filled(row, column):
            return False
        else:
            self.boardArray[row][column] = playerSymbol
            return True

    def game_is_won(self, playerSymbol):

        self.check_horizontals(playerSymbol)
        self.check_verticals(playerSymbol)
        self.check_diagonals(playerSymbol)

        # return the state of the game
        if self.gameWon:
            if playerSymbol == " X ":
                self.winner = Winner.X_WIN
            elif playerSymbol == " O ":
                self.winner = Winner.O_WIN
            return True
        else:
            if self.check_if_cats_game():
                return True
            else:
                return False

    def check_horizontals(self, playerSymbol):
        for row in range(0, 3):
            row = row * 2  # to accommodate the other deliminators in the board like +, -, |
            if self.boardArray[row][0] == playerSymbol and self.boardArray[row][2] == playerSymbol and \
                    self.boardArray[row][4] == playerSymbol:
                self.gameWon = True

    def check_verticals(self, playerSymbol):
        for col in range(0, 3):
            col = col * 2  # to accommodate the other deliminators in the board like +, -, |
            if self.boardArray[0][col] == playerSymbol and self.boardArray[2][col] == playerSymbol and \
                    self.boardArray[4][col] == playerSymbol:
                self.gameWon = True

    def check_diagonals(self, playerSymbol):
        if self.boardArray[0][0] == playerSymbol and self.boardArray[2][2] == playerSymbol and self.boardArray[4][
            4] == playerSymbol:
            self.gameWon = True
        if self.boardArray[0][4] == playerSymbol and self.boardArray[2][2] == playerSymbol and self.boardArray[4][
            0] == playerSymbol:
            self.gameWon = True

    def check_if_cats_game(self):
        for row in range(0, 5):
            for col in range(0, 5):
                if self.boardArray[row][col] == "   ":
                    return False  # if there is a blank space, it's not a cat's game
        self.gameWon = True
        self.winner = Winner.CATS_GAME
        return True  # if it went through the whole loop and there was no blank spaces, it's a cat's game


class Player:
    def __init__(self):
        self.currentRow = 0
        self.currentCol = 0


class ComputerPlayer(Player):
    def __init__(self):
        super().__init__()
        self.name = "the computer"

    def take_turn(self):
        self.currentRow = randint(0, 2)
        self.currentCol = randint(0, 2)

    def try_again(self):
        self.take_turn()


class HumanPlayer(Player):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def take_turn(self):
        row = int(input("Which row do you want to choose?"))
        while not (1 <= row <= 3):
            row = int(input("That is not a digit 1-3. Please choose a row, 1-3:"))

        column = int(input("which column do you want to choose?"))
        while not (1 <= column <= 3):
            column = int(input("This is not a digit 1-3. Please choose a column, 1-3:"))

        self.currentRow = int(row) - 1
        self.currentCol = int(column) - 1

    def try_again(self):
        print("That spot is already filled. Please try again.")
        self.take_turn()


def game_setup():
    # Heading
    print("Let's Play Tic Tac Toe!")
    print("-----------------------")
    print("")

    mode_choice = input(
        'Would you like to play against another human or against the computer? Type "human" or "computer":').lower()
    while mode_choice != "human" and mode_choice != "computer":
        mode_choice = input(
            "We don't offer that version yet. Coming soon to the next version: demi-god. For now, choose human or "
            "computer.").lower()

    if mode_choice == "computer":
        name = input("What is your name?")
        firstPlayer = HumanPlayer(name)
        secondPlayer = ComputerPlayer()
    elif mode_choice == "human":
        name1 = input("What is player one's name?")
        name2 = input("what is player two's name?")
        firstPlayer = HumanPlayer(name1)
        secondPlayer = HumanPlayer(name2)

    return firstPlayer, secondPlayer


def game_play(playerOne, playerTwo, myBoard):
    turnAlternator: int = 1  # gets incremented every time a turn is taken, so player one goes on odd numbers
    # player two goes on even numbers

    while not myBoard.gameWon:

        if turnAlternator % 2 == 1:
            currentPlayer = playerOne
            currentSymbol = " X "
        else:
            currentPlayer = playerTwo
            currentSymbol = " O "

        print(f"It's {currentPlayer.name}'s turn!")

        currentPlayer.take_turn()

        while not myBoard.insert_player_choice(currentSymbol, currentPlayer.currentRow, currentPlayer.currentCol):
            currentPlayer.try_again()

        if myBoard.game_is_won(currentSymbol):
            print_win_message(myBoard.winner, currentPlayer.name)
            return

        myBoard.display_board()

        turnAlternator += 1


def print_win_message(winner, playerName):
    print("------------------------------------------")
    print(" ")
    if winner == Winner.CATS_GAME:
        print("It's a cat's game. Meow.")
    else:
        print(f"{playerName} won the game!")


theBoard = Board()
theBoard.display_board()  # display board before game

player1, player2 = game_setup()
game_play(player1, player2, theBoard)

theBoard.display_board()  # display board after game
print("All done. Thanks for playing!")
