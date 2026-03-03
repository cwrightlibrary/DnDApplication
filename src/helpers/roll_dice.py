from random import randint
from typing import List


def roll_dice(num_rolls: int = 4, die_sides: int = 6, ability_gen: bool = True) -> int:
    """
    Rolls a specified die a certain amount of times.

    Args:
        num_rolls: The amount of times to roll.
        die_sides: The type of die to roll, D6 is the default.
        ability_gen: If this is used to generate abilities, remove the lowest roll.
       
    Returns:
        The sum of the rolls.
    """

    # Collect a list of rolls
    rolls: List[int] = []

    # Roll a dice num_rolls times
    for roll in range(0, num_rolls):
        # What type? D6 is the default
        rand_roll = randint(1, die_sides)
        # Add roll to list
        rolls.append(rand_roll)
    
    # Sort the rolls least -> most
    rolls.sort()

    # If this is being used to generate ability scores...
    if ability_gen:
        # Remove the lowest roll
        rolls.pop(0)
    # Return the sum of the remaining rolls
    return sum(rolls)