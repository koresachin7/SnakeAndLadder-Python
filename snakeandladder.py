import random
import sys

MAX_VAL = 100
# snake takes you down from 'key' to 'value'
snakes = {8: 4, 18: 1, 26: 10, 39: 5, 51: 6, 54: 36, 60: 23, 90: 48, 92: 25, 97: 87, 99: 63}

# ladder takes you up from 'key' to 'value'
ladders = {3: 20, 6: 14, 11: 28, 15: 34, 17: 74, 22: 37, 38: 59, 49: 67, 57: 76, 61: 78, 73: 86, 81: 98, 88: 91}


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

    def get_player_names(self):
        """
        Description:
            this function assign players name
        Return:
            this function return players name
        """
        player1_name = None
        while not player1_name:
            player1_name = input("Please enter a valid name for first player: ")

        player2_name = None
        while not player2_name:
            player2_name = input("Please enter a valid name for second player: ")

        print("Match will be played between '" + player1_name + "' and '" + player2_name + "")
        return player1_name, player2_name

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

    def snake_ladder(self, player_name, current_value, dice_value):
        """
        Description:
            this function for assign snake and ladder value
            and check current value are not cross maximum value
        Return:
            this function return fine value of player position
        """
        old_value = current_value
        current_value = current_value + dice_value

        if current_value > MAX_VAL:
            print("You need " + str(MAX_VAL - old_value) + " to win this game. Keep trying.")
            return old_value

        print("\n" + player_name + " moved from " + str(old_value) + " to " + str(current_value))
        if current_value in snakes:
            final_value = snakes.get(current_value)
            self.got_snake_bite(current_value, final_value, player_name)

        elif current_value in ladders:
            final_value = ladders.get(current_value)
            self.got_ladder_jump(current_value, final_value, player_name)

        else:
            final_value = current_value

        return final_value

    def check_win(self, player_name, position):
        """
        Description:
            this function for check wining status of players
        """
        if MAX_VAL == position:
            print("That's it .." + player_name + " won the game.")
            print("congratulations " + player_name)
            sys.exit(1)

    def start(self):
        """
        Description:
            this function for start program calling multiple function
            and roll dice till one of the player win
        """
        welcome_msg()
        player1_name, player2_name = self.get_player_names()

        player1_current_position = 0
        player2_current_position = 0

        while True:
            input_1 = input("\n" + player1_name + ": "  "  enter to roll dice: ")
            print("rolling dice...")
            dice_value = self.get_dice_value()
            print(player1_name + " moving....")
            player1_current_position = self.snake_ladder(player1_name, player1_current_position, dice_value)

            self.check_win(player1_name, player1_current_position)

            input_2 = input("\n" + player2_name + ": "  "  enter to roll dice: ")
            print("Rolling dice...")
            dice_value = self.get_dice_value()
            print(player2_name + " moving....")
            player2_current_position = self.snake_ladder(player2_name, player2_current_position, dice_value)

            self.check_win(player2_name, player2_current_position)


if __name__ == '__main__':
    snake_and_ladder = SnakeAndLadder()
    snake_and_ladder.start()
