#! usr/bin/env
# -*- coding: utf-8 -*-
"""Duke Phung Assignment 1 Part 1"""


def listDivide(number, divide=2):
    """REturns count of times items in number is divisible by divide without remainders.

    Args:
        number (list): list used to store items.
        divide (int, optional): value used as divider.

    Returns:
        count (int): number of items that are divisible by divide without remainders.

    Example:
        >>>listDivider([1, 2, 3, 4, 5])
        2
    """

    count = 0

    for x in number:
        try:
            x = int(x)
        except ValueError:
            pass

        if x % divide == 0:
            count += 1


    return (count)
