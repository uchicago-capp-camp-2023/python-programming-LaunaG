"""
Launa Greer (launagreer)

A mock homework assignment to practice writing
Python expressions and using Visual Studio
Code and GradeScope.

CAPP Camp
August 25, 2023
Python Programming Lab
"""


def is_divisible(a, b):
    """PROBLEM 1. (5 pts)

    Determines whether an integer, a, can be
    divided by another integer, b, without
    any remainder. NOTE: For the sake of
    testing, you are guaranteed to only receive
    integers that are greater than zero.

    Args:
        a (int): The first integer.
        b (int): The second integer.

    Returns:
        (bool): True if a is divisible
            by b and False otherwise.
    """
    return a % b == 0


def max_integer(a, b, c):
    """PROBLEM 2. (5 pts)

    Returns the max of three integers
    a, b, and c.

    Args:
        a (int): The first integer.
        b (int): The second integer.
        c (int): The third integer.

    Returns:
        (int): The max integer
    """
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c


def fizzbuzz(a):
    """PROBLEM 3. (5 pts)

    Receives an integer, a, as input and returns
    the string "Fizz!" if that integer is
    divisible by 3, "Buzz!" if it is divisible
    by 5, and "FizzBuzz!" if it is divisible
    by both 3 and 5. If the number is not
    divisible by 3 or 5, it returns the
    number as a string.

    HINT: To turn the integer, a, into a string,
    you can use str(a).

    Args:
        a (int): An integer.

    Returns:
        (str): A string that is "Fizz!", "Buzz!",
            "FizzBuzz!", or the original input number
    """
    if a % 3 == 0 and a % 5 == 0:
        return "FizzBuzz!"
    elif a % 3 == 0:
        return "Fizz!"
    elif a % 5 == 0:
        return "Buzz!"
    else:
        return str(a)


def is_square(pt1, pt2, pt3, pt4):
    """PROBLEM 4. (5 pts)

    Takes four XY coordinate pairs as input
    and returns True if the four coordinates
    form a square and False otherwise.
    
    NOTE: Each point/coordinate pair will
    look something like [0, 1] or [-2, 3],
    where the first number is the x-coordinate
    and the second number is the y-coordinate.
    These points exist on a Cartesian plane
    (2D space). For the sake of testing, all
    points are guaranteed to be integers.

    Args:
        pt1 (list of int): The first point/XY
            coordinate pair.

        pt2 (list of int): The second point/XY
            coordinate pair.

        pt3 (list of int): The third point/XY
            coordinate pair.

        pt4 (list of int): The fourth point/XY
            coordinate pair.

    Returns:
        (bool): True if the coordinates make a
            square and False otherwise.
    """
    # Extract coordinates from each point.
    # Each coordinate (i.e., x1, y1, x2, y2...)
    # is an integer.
    x1, y1 = pt1
    x2, y2 = pt2
    x3, y3 = pt3
    x4, y4 = pt4

    # Define local function for calculating distances
    def distance(x1, y1, x2, y2):
        return ((x2 - x1)**2 + (y2 - y1)**2)**0.5
    
    # Calculate distances for all possible segments
    # between points (i.e., diagonals and sides)
    distances = [
        distance(x1, y1, x2, y2), # Pt1 <-> Pt2
        distance(x1, y1, x3, y3), # Pt1 <-> Pt3
        distance(x1, y1, x4, y4), # Pt1 <-> Pt4
        distance(x2, y2, x3, y3), # Pt2 <-> Pt3
        distance(x2, y2, x4, y4), # Pt2 <-> Pt4
        distance(x3, y3, x4, y4), # Pt3 <-> Pt4
    ]

    # Sort distances to be ascending
    distances.sort()

    # Determine whether coordinates represent a square.
    # NOTE: In a square, the diagonals will be the two longest
    # segments, and they will be equal.  In addition, all four
    # sides will be equal.
    has_length = min(distances) > 0
    sides_equal = distances[0] == distances[1] == distances[2] == distances[3]
    diagonals_equal = distances[4] == distances[5]

    return has_length and sides_equal and diagonals_equal
    

