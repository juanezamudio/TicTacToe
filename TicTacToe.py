import random


class TicTacToe:

    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2

        win_states = [[0, 1, 2],
                      [3, 4, 5],
                      [6, 7, 8],
                      [0, 3, 6],
                      [1, 4, 7],
                      [2, 5, 8],
                      [0, 4, 8],
                      [2, 4, 6]]

        while True:
            board_state = [1, 2, 3,
                           4, 5, 6,
                           7, 8, 9]

            print("Let's play Tic-Tac-Toe!\n")

            starting_player = self.set_up_game(board_state)

            winner = self.start_game(starting_player, board_state, win_states)

            if winner == "draw":
                print("It's a tie!. No one wins. Nice playing!\n")
                replay = raw_input("Do you want a rematch? Press anything if YES or press enter if NO.\n")
            else:
                loser = self.player1 if winner == self.player2 else self.player2
                print("Congratulations, " + winner + ". You won! Better luck next time, " + loser + "\n")
                replay = raw_input("Do you want to play again? Press anything if YES or press enter if NO.\n")

            if replay == "":
                break;

        print("Thanks for playing! See you next time.\n")

    def set_up_game(self, board_state):

        rand_int = random.randint(0, 1)
        chosen_player = self.player1 if rand_int else self.player2

        print("You go first, " + chosen_player + "!\n")

        board_display = ""

        for item in board_state:
            if item % 3 != 0:
                board_display += str(item) + "|"
            else:
                if item == 9:
                    board_display += str(item) + "\n"
                else:
                    board_display += str(item) + "\n" + "-----" + "\n"

        print board_display

        return chosen_player

    def player_move(self, board_state, player):

        move = raw_input("What's your move? Choose a number position not yet taken.\n")

        while move.isalpha() or move.isspace() or move == "" or int(move) not in board_state:
            move = raw_input("Invalid position. Try again!\n")

        return self.update_board(board_state, int(move), player)

    def update_board(self, board_state, move, player):

        game_piece = "X" if player == self.player1 else "O"
        board_state[move - 1] = game_piece

        board_display = ""

        for i in range(0, len(board_state)):
            if (i + 1) % 3 != 0:
                board_display += str(board_state[i]) + "|"
            else:
                if i == 8:
                    board_display += str(board_state[i]) + "\n"
                else:
                    board_display += str(board_state[i]) + "\n" + "-----" + "\n"

        print board_display

        curr_player = self.player2 if player == self.player1 else self.player1

        return curr_player

    def draw(self, board_state):
        check_draw = True

        for item in board_state:
            if item != "X" and item != "O":
                check_draw = False
                break;

        return check_draw

    def game_over(self, board_state, win_states):
        check_win = False

        for win in win_states:
            if check_win:
                return check_win

            check_win = board_state[win[0]] == board_state[win[1]] == board_state[win[2]]

        return check_win

    def start_game(self, player, board_state, win_states):

        while not self.game_over(board_state, win_states) and not self.draw(board_state):
            player = self.player_move(board_state, player)

        if self.draw(board_state):
            player = "draw"
        else:
            player = self.player2 if player == self.player1 else self.player1

        return player


game = TicTacToe("Juan", "Lainee")