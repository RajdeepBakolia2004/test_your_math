#this part of the program generate a random integer in three level of difficulty
#level easy: 1-50
#level medium: 25-150
#level hard: 100-500
from random import randint as r
"""
    Generates a random integer based on the given level.

    Parameters:
        level (int): The level of difficulty. Must be an integer between 1 and 3.

    Returns:
        int: A random integer within the specified range for the given level.

"""
def random_number(level : int) -> int:
    if level == 1:
        return r(1, 50)
    elif level == 2:
        return r(25, 150)
    elif level == 3:
        return r(100, 500)