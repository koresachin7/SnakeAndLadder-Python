"""
* @Author: Sachin S Kore
* @Date: 2021-12-4
* @Title : use random generating number
"""
import random


class SnakeAndLadder:
    # initializing position
    position = 0

    def roll_dice(self):
        """
        Description:
            this function generating random vale 1 to 6
        Return:
            this function return random value
        """
        dice = random.randint(1, 6)
        print("Dice Roll is : -", dice)
        return dice

    def player_option(self):
        """
        Description:
            call roll_dice method to update position
            use Random  to generating number between 0 to 2
            use if and elif ladder to check player option
        """
        dice = snake_and_ladder.roll_dice()
        option = random.randint(0, 2)
        print("Player Roll Option is : -", option)
        print("0.no Player 1. Ladder 2.Snake")
        if option == 0:
            print("no Player")
        elif option == 1:
            print("Ladder")
            self.position += dice
        elif option == 2:
            print("Snake")
            self.position -= dice
        else:
            print("System error")


if __name__ == '__main__':
    print("Welcome to Snake and Ladder Problem")
    snake_and_ladder = SnakeAndLadder()
    snake_and_ladder.player_option()