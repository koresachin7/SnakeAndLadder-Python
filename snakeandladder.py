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


if __name__ == '__main__':
    print("Welcome to Snake and Ladder Problem")
    snake_and_ladder = SnakeAndLadder()
    # calling function her and store method return value
    dice_value = snake_and_ladder.roll_dice()
    print(dice_value)
