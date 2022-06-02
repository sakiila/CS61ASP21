def twenty_twenty_one():
    """Come up with the most creative expression that evaluates to 2021,
    using only numbers and the +, *, and - operators.

    >>> twenty_twenty_one()
    2021
    """
    return 1 * 2 + 3 + 4 * ((5 // 6) + 7 * 8 * 9)


if __name__ == '__main__':
    print(twenty_twenty_one())
