import random


class TicTacToe:

    def __init__(self, player1, player2):

        # Initializes player name variables
        self.player1 = player1
        self.player2 = player2

        # Possible win states for the game
        win_states = [[0, 1, 2],
                      [3, 4, 5],
                      [6, 7, 8],
                      [0, 3, 6],
                      [1, 4, 7],
                      [2, 5, 8],
                      [0, 4, 8],
                      [2, 4, 6]]

        # Loop that runs the game and will only break if player decides to
        # quit playing
        while True:

            # Initial state of the game
            board_state = [1, 2, 3,
                           4, 5, 6,
                           7, 8, 9]

            # Sets up the player to token association by randomly assigning
            # player token every new game
            rand_int = random.randint(0, 1)
            player_store = {}

            if rand_int:
                player_store[self.player1] = "X"
                player_store[self.player2] = "O"
            else:
                player_store[self.player1] = "O"
                player_store[self.player2] = "X"

            print("Let's play Tic-Tac-Toe!\n")

            # Set up the game with a starting player
            starting_player = self.set_up_game(board_state)

            # Starts and runs the game with starting player, initial board state,
            # and possible win states and determines a winner depending on game play
            winner = self.start_game(starting_player, board_state, win_states, player_store)

            # checks to see if game is a win or a draw and prints proper message
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
        """
        Sets up the game and the console board display and returns the
        randomly chosen first-turn player

        @param board_state: the initial board state of the game
        @return: the randomly chosen first-turn player
        """

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

    def player_move(self, player, board_state, player_store):
        """
        Makes a player move by asking the player for a move position, checking
        if it's a valid position or input and then updating the board

        @param player: the current player
        @param board_state: the current state of the board
        @param player_store: the player-token association map
        @return: None
        """

        move = raw_input("What's your move, " + player + "? Choose a number position not yet taken.\n")

        while move.isalpha() or move.isspace() or move == "" or int(move) not in board_state:
            move = raw_input("Invalid position. Try again!\n")

        return self.update_board(player, board_state, int(move), player_store)

    def update_board(self, player, board_state, move, player_store):
        """
        Updates the display and current state of the board according to
        the current players chosen move and switches the current player
        to the opposing player

        @param player: the current player
        @param board_state: the current state of the board
        @param move: the current player's chosen move
        @param player_store: the player token-association map
        @return: the opposing player
        """

        game_piece = player_store[player]
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

        return self.player2 if player == self.player1 else self.player1

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

    def start_game(self, player, board_state, win_states, player_store):

        while not self.game_over(board_state, win_states) and not self.draw(board_state):
            player = self.player_move(player, board_state, player_store)

        if self.draw(board_state):
            return "draw"
        else:
            return self.player2 if player == self.player1 else self.player1

player1 = raw_input("What is your name, Player 1?")
player2 = raw_input("What is your name, Player 2?")
game = TicTacToe(player1, player2)