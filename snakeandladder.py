import random
import sys
from logging import *

MAX_VAL = 50
# snake takes you down from 'key' to 'value'
snakes = {8: 4, 18: 1, 26: 10, 39: 5}

# ladder takes you up from 'key' to 'value'
ladders = {3: 20, 6: 14, 11: 28, 15: 34, 17: 74, 22: 37}


def welcome_msg():
    """
    Description:
        this function print instructions for user
    """

    msg = """
    Welcome to Snake and Ladder Game......
    Rules:
      1. initially both the players a
         take it in turns to roll the dice. 
      2. if you lands at the bottom of a ladder, you can move up to the top of the ladder.
      3. if you lands on the head of a snake, you must slide down to the bottom of the snake.
      4. enter to roll the dice.
    """
    print(msg)


class SnakeAndLadder:
    def __init__(self):
        self.list = []

    # def get_player_names(self):
    #     """
    #     Description:
    #         this function assign players name
    #     Return:
    #         this function return players name
    #     """
    #     player1_name = None
    #     while not player1_name:
    #         player1_name = input("Please enter a valid name for first player: ")
    #
    #     player2_name = None
    #     while not player2_name:
    #         player2_name = input("Please enter a valid name for second player: ")
    #
    #     print("Match will be played between '" + player1_name + "' and '" + player2_name + "")
    #     return player1_name, player2_name

    def get_dice_value(self):
        """
        Description:
            this function generating random vale 1 to 6
        Return:
            this function return random value
        """
        dice_value = random.randint(1, 6)
        print("it's a ", dice_value)
        return dice_value

    def got_snake_bite(self, old_value, current_value, player_name):
        """
        Description:
            this function for snake bite detail
        """
        print("\n" + player_name + " got a snake bite. Down from " + str(old_value) + " to " + str(current_value))

    def got_ladder_jump(self, old_value, current_value, player_name):
        """
        Description:
            this function for climbed ladder detail
        """
        print("\n" + player_name + " climbed the ladder from " + str(old_value) + " to " + str(current_value))

    def snake_ladder(self, player, dice_value):
        """
        Description:
            this function for assign snake and ladder value
            and check current value are not cross maximum value
        Return:
            this function return fine value of player position
        """
        old_value = player.player1_current_position
        player.player1_current_position = player.player1_current_position + dice_value

        if player.player1_current_position > MAX_VAL:
            print("You need " + str(MAX_VAL - old_value) + " to win this game. Keep trying.")
            return old_value

        print("\n" + player.player_name + " moved from " + str(old_value) + " to " + str(player.player1_current_position))
        if player.player1_current_position in snakes:
            final_value = snakes.get(player.player1_current_position)
            self.got_snake_bite(player.player1_current_position, final_value, player.player_name)

        elif player.player1_current_position in ladders:
            final_value = ladders.get(player.player1_current_position)
            self.got_ladder_jump(player.player1_current_position, final_value, player.player_name)

        else:
            final_value = player.player1_current_position

        return final_value

    def check_win(self, player):
        """
        Description:
            this function for check wining status of players
        """
        if MAX_VAL == player.player1_current_position:
            print("That's it .." + player.player_name + " won the game.")
            print("congratulations " + player.player_name)
            sys.exit(1)

    def start(self):
        """
        Description:
            this function for start program calling multiple function
            and roll dice till one of the player win
        """

        # player1_name, player2_name = self.get_player_names()

        player2_current_position = 0

        while True:
            for player in self.list:
                input_1 = input("\n" + player.player_name + ": "  "  enter to roll dice: ")
                print("rolling dice...")
                dice_value = self.get_dice_value()
                print(player.player_name + " moving....")
                player.player1_current_position = self.snake_ladder(player, dice_value)

                self.check_win(player)

                # input_2 = input("\n" + player2_name + ": "  "  enter to roll dice: ")
                # print("Rolling dice...")
                # dice_value = self.get_dice_value()
                # print(player2_name + " moving....")
                # player2_current_position = self.snake_ladder(player2_name, player2_current_position, dice_value)
                #
                # self.check_win(player2_name, player2_current_position)


class Players:

    def __init__(self, player_name):
        self.player_name = player_name
        self.player1_current_position = 0
    #
    # def get_player_names(self):
    #     """
    #     Description:
    #         this function assign players name
    #     Return:
    #         this function return players name
    #     """
    #     self.player_name = None
    #     while not self.player_name:
    #         self.player_name = input("Please enter a valid name  player: ")
    #     return self.player_name


if __name__ == '__main__':
    snake_and_ladder = SnakeAndLadder()
    LOG_FORMAT = '{lineno} *** {name} *** {asctime} *** {message}'
    basicConfig(filename='logfile.log', level=DEBUG, style='{', format=LOG_FORMAT)

    welcome_msg()
    try:
        player_num = int(input("Enter Player Quantity : --"))
        if player_num > 1:
            for player in range(player_num):
                player_name = input("Please enter a valid name  player: ")
                player_obj = Players(player_name)
                # player_obj.get_player_names()
                snake_and_ladder.list.append(player_obj)
                print(snake_and_ladder.list)
        else:
            print("player is always greater than One please enter again....")
            warning("player is always greater than One please enter again....")

    except Exception:
        print("Please Enter Number Only...")
        error("Please Enter Number Only...")

    snake_and_ladder.start()
