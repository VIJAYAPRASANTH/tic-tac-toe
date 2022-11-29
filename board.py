from p1 import p1
from p2 import p2


class Board:
    def __init__(self, p1, p2):
        self.board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        self.ava_blocks = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.winner = None

    def change_player(self, p):
        print("{} | {} | {}".format(*self.board[0]))
        print("____________")
        print("{} | {} | {}".format(*self.board[1]))
        print("____________")

        print("{} | {} | {}".format(*self.board[2]))

        print()

        chosen_block = input("Player {}".format(p.sym)+' Choose a block : ')
        if not chosen_block.isdigit():
            print("Please Enter a Valid Number!")
            print()

            return self.change_player(p)
        else:
            chosen_block = int(chosen_block)

        print()

        if chosen_block in self.ava_blocks:

            for row in self.board:
                if chosen_block in row:
                    row[row.index(chosen_block)] = p.sym
                    break
            p.blocks[chosen_block-1] = p.sym
            self.ava_blocks.remove(chosen_block)

            return self.validate_user(p)

        elif chosen_block > 9 or chosen_block < 1:
            print("Please Enter a Valid Number!")
            print()
            return self.change_player(p)
        else:
            print("This block is already selected!")
            return self.change_player(p)

    def validate_user(self, player):
        is_row = False
        column = False
        diagnol = False
        anti = False

        board = self.board
        for row in range(len(board)):
            if set(board[row]) == {player.sym}:
                is_row = True
                break
            n_column = []
            for i in board:
                n_column.append(i[row])
            if set(n_column) == {player.sym}:
                column = True
                break
        n_d = []
        a_d = []
        for i in range(len(board)):
            n_d.append(board[i][i])
            a_d.append(board[i][-(i+1)])
        if set(n_d) == {player.sym} or set(a_d) == {player.sym}:
            self.winner = player

        if is_row or column:
            self.winner = player

        if self.winner != None:
            print("{} | {} | {}".format(*self.board[0]))
            print("{} | {} | {}".format(*self.board[1]))
            print("{} | {} | {}".format(*self.board[2]))
            print()


def start_players(p1_sym, p2_sym):
    player1 = p1(p1_sym)
    player2 = p2(p2_sym)
    board = Board(player1, player2)
    players = [player1, player2]
    first = 0
    for i in range(9):
        board.change_player(players[first])
        if board.winner != None:
            print("Player {} is the winner!".format(board.winner.sym))
            break
        if first:
            first = 0
        else:
            first = 1
        if i == 8 and board.winner == None:
            print("It's a Tie.")


def start_game():
    print("Do you want to start the game?")
    answer = input("Please Enter Yes or No: ")
    if answer.lower() == "yes":
        print("Choose Player1 Symbol")
        p1_sym = input('Please Enter P1 symbol: ').upper()
        print()
        print("Choose Player2 Symbol")
        p2_sym = input("Please Enter P2 symbol: ").upper()
        print()
        if p1_sym == p2_sym:
            print("Both Players Chosen Same Symbols So Player2 Symbol Changed to '{}'".format(
                chr(ord(p1_sym)+1)))
            print()
            p2_sym = chr(ord(p1_sym)+1)
        print("Player1 is {}".format(p1_sym))
        print()
        print("Player2 is {}".format(p2_sym))
        print()

        start_players(p1_sym, p2_sym)

    else:
        print("See You Soon!")
        exit()


start_game()
