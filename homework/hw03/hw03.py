HW_SOURCE_FILE = __file__


def num_eights(x):
    """Returns the number of times 8 appears as a digit of x.

    >>> num_eights(3)
    0
    >>> num_eights(8)
    1
    >>> num_eights(88888888)
    8
    >>> num_eights(2638)
    1
    >>> num_eights(86380)
    2
    >>> num_eights(12345)
    0
    >>> from construct_check import check
    >>> # ban all assignment statements
    >>> check(HW_SOURCE_FILE, 'num_eights',
    ...       ['Assign', 'AugAssign'])
    True
    """
    "*** YOUR CODE HERE ***"
    # takes a positive integer x and returns the number or times the digit 8 appears in x
    # no statements that have the equal sign
    # base case: x<10 and not 8 return 0
    # else do recursive call stuff
    # count number of digits x has
    if x == 0:
        return 0
    if x % 10 == 8:
        return num_eights(x // 10) + 1
    return num_eights(x // 10)


def pingpong(n):
    """Return the nth element of the ping-pong sequence.

    >>> pingpong(8)
    8
    >>> pingpong(10)
    6
    >>> pingpong(15)
    1
    >>> pingpong(21)
    -1
    >>> pingpong(22)
    -2
    >>> pingpong(30)
    -2
    >>> pingpong(68)
    0
    >>> pingpong(69)
    -1
    >>> pingpong(80)
    0
    >>> pingpong(81)
    1
    >>> pingpong(82)
    0
    >>> pingpong(100)
    -6
    >>> from construct_check import check
    >>> # ban assignment statements
    >>> check(HW_SOURCE_FILE, 'pingpong', ['Assign', 'AugAssign'])
    True
    """
    "*** YOUR CODE HERE ***"

    # if index is a multiple or contains 8, switch directions
    # return the ping pong value
    # how to keep track of all the variables? helper function should return helper
    # index, ppn, and direction change

    def helper1(index, ppn, dir):
        while index != n:
            if num_eights(index) or index % 8 == 0:
                return helper1(index + 1, ppn - dir, -dir)
            return helper1(index + 1, ppn + dir, dir)
        return ppn

    return helper1(1, 1, 1)

    """
    index, ppn, dir = 1, 1, 1
    while index != n:
        index += 1
        ppn += dir
        if num_eights(index) or index % 8 == 0:
            dir = -dir
    return ppn"""


def missing_digits(n):
    """Given a number a that is in sorted, increasing order,
    return the number of missing digits in n. A missing digit is
    a number between the first and last digit of a that is not in n.
    >>> missing_digits(1248) # 3, 5, 6, 7
    4
    >>> missing_digits(19) # 2, 3, 4, 5, 6, 7, 8
    7
    >>> missing_digits(1122) # No missing numbers
    0
    >>> missing_digits(123456) # No missing numbers
    0
    >>> missing_digits(3558) # 4, 6, 7
    3
    >>> missing_digits(35578) # 4, 6
    2
    >>> missing_digits(12456) # 3
    1
    >>> missing_digits(16789) # 2, 3, 4, 5
    4

    >>> missing_digits(4) # No missing numbers between 4 and 4
    0
    >>> from construct_check import check
    >>> # ban while or for loops
    >>> check(HW_SOURCE_FILE, 'missing_digits', ['While', 'For'])
    True
    """
    "*** YOUR CODE HERE ***"
    # takes a number n that is sorted in increasing order
    # returns the number of missing digits in n
    # variables: return count
    # base case: n<10
    """ idea: look at the last digit of n using modulo 
    then go through the n by floor dividing and comparing
    the last digit to the second to last digit
    """
    if n < 10:
        return 0
    else:
        # last digit - second to last digit is equal to one or 0 no missing digits
        if n % 10 - (n // 10) % 10 == 1:
            return missing_digits(n // 10)
        if n % 10 - (n // 10) % 10 == 0:
            return missing_digits(n // 10)
        return (n % 10) - (n // 10) % 10 - 1 + missing_digits(n // 10)


def get_next_coin(coin):
    """Return the next coin.
    >>> get_next_coin(1)
    5
    >>> get_next_coin(5)
    10
    >>> get_next_coin(10)
    25
    >>> get_next_coin(2) # Other values return None
    """
    if coin == 1:
        return 5
    elif coin == 5:
        return 10
    elif coin == 10:
        return 25


def count_coins(change):
    """Return the number of ways to make change using coins of value of 1, 5, 10, 25.
    >>> count_coins(15)
    6
    >>> count_coins(10)
    4
    >>> count_coins(20)
    9
    >>> count_coins(100) # How many ways to make change for a dollar?
    242
    >>> from construct_check import check
    >>> # ban iteration
    >>> check(HW_SOURCE_FILE, 'count_coins', ['While', 'For'])
    True
    """
    "*** YOUR CODE HERE ***"
    # use get next coin to calculate the next largest coin denomination of your coin
    """reminder: num of ways to partintion n using integers up to m
    1. the number of ways to partition n-m (change - 25) using integers up to m, and
        partition a smaller number
    2. the number of ways to partition n using integers up to m-1.
        partition smaller components
    """

    # base case: change = 0 or change < 0 or the next coin doesnt exist
    def helper(change, y):
        if change == 0:
            return 1
        elif change < 0 or y == None:
            return 0
        elif y == 0:
            return 0
        else:
            with_coin = helper(change - y, y)
            without_coin = helper(change, get_next_coin(y))
            return with_coin + without_coin

    return helper(change, 1)


from operator import sub, mul


def make_anonymous_factorial():
    """Return the value of an expression that computes factorial.

    >>> make_anonymous_factorial()(5)
    120
    >>> from construct_check import check
    >>> # ban any assignments or recursion
    >>> check(HW_SOURCE_FILE, 'make_anonymous_factorial', ['Assign', 'AugAssign', 'FunctionDef', 'Recursion'])
    True
    """
    return 'YOUR_EXPRESSION_HERE'


def print_move(origin, destination):
    """Print instructions to move a disk."""
    print("Move the top disk from rod", origin, "to rod", destination)


def move_stack(n, start, end):
    """Print the moves required to move n disks on the start pole to the end
    pole without violating the rules of Towers of Hanoi.

    n -- number of disks
    start -- a pole position, either 1, 2, or 3
    end -- a pole position, either 1, 2, or 3

    There are exactly three poles, and start and end must be different. Assume
    that the start pole has at least n disks of increasing size, and the end
    pole is either empty or has a top disk larger than the top n start disks.

    >>> move_stack(1, 1, 3)
    Move the top disk from rod 1 to rod 3
    >>> move_stack(2, 1, 3)
    Move the top disk from rod 1 to rod 2
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 2 to rod 3
    >>> move_stack(3, 1, 3)
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 1 to rod 2
    Move the top disk from rod 3 to rod 2
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 2 to rod 1
    Move the top disk from rod 2 to rod 3
    Move the top disk from rod 1 to rod 3
    """
    assert 1 <= start <= 3 and 1 <= end <= 3 and start != end, "Bad start/end"
    "*** YOUR CODE HERE ***"
