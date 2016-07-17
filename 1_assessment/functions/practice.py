"""
Skills function assessment.

Please read the the instructions first (separate file). Your solutions should
go below this docstring.

PART ONE:

    >>> hello_world()
    Hello World

    >>> say_hi("Balloonicorn")
    Hi Balloonicorn

    >>> print_product(3, 5)
    15

    >>> repeat_string("Balloonicorn", 3)
    BalloonicornBalloonicornBalloonicorn

    >>> print_sign(3)
    Higher than 0

    >>> print_sign(0)
    Zero

    >>> print_sign(-3)
    Lower than 0

    >>> is_divisible_by_three(12)
    True

    >>> is_divisible_by_three(10)
    False

    >>> num_spaces("Balloonicorn is awesome!")
    2

    >>> total_meal_price(30)
    34.5

    >>> total_meal_price(30, .3)
    39.0

    >>> sign_and_parity(3)
    ['Positive', 'Odd']

    >>> sign_and_parity(-2)
    ['Negative', 'Even']

PART TWO:

    >>> full_title("Balloonicorn")
    'Engineer Balloonicorn'

    >>> full_title("Jane Hacks", "Hacker")
    'Hacker Jane Hacks'

    >>> write_letter("Jane Hacks", "Hacker", "Balloonicorn")
    Dear Hacker Jane Hacks, I think you are amazing! Sincerely, Balloonicorn

    >>> nums = [1, 2]
    >>> add_new_number(5, nums)
    >>> nums
    [1, 2, 5]

    
    """
################################################################################

def hello_world():
    """ Prints "Hello World"."""

    print "Hello World"

def say_hi(name):
    """ Takes a name as a string and prints "Hi" followed by the name."""

    print "Hi", name

def print_product(a, b):
    """ Takes two integers, multiplies them together. and prints the result."""

    print int(a) * int(b)

def repeat_string(txt, num):
    """ Takes a string and an integer and prints the string that many times"""

    print txt * int(num)


def print_sign(num):
    """ Take an integer and prints message about value.

    Print "Higher than 0" if higher than zero and 
    "Lower than 0" if lower than zero. 
    If the integer is 0 print "Zero"."""

    num = int(num)
    if num > 0:
        print "Higher than 0"
    elif num < 0:
        print "Lower than 0"
    elif num == 0:
        print "Zero"
    else:
        print "Not an integer"


def is_divisible_by_three(num):
    """ Take an integer and determine if it is evenly divisible by 3.

    Return a boolean (True or False)"""
    if num % 3 == 0:
        result = True
    else:
        result = False

    return result



def num_spaces(txt):
    """ Take a sentence as one string and returns the number of spaces."""

    return txt.count(" ")


def total_meal_price(price, tip_pct=.15):
    """ Returns the total amount paid for a meal (price + price * tip).

    Can be passed a meal price and a tip percentage.
    **However:** passing in the tip percentage should be optional; 
    if not given, it should default to 15%."""

    return price + (tip_pct*price)


def sign_and_parity(integer):
    """ Determines value of integer and prints attributes.

    Returns two pieces of information as strings ---
    "Positive" or "Negative" and "Even" or "Odd".
    The two strings should be returned in a list."""

    if integer % 2:
        parity = "Odd"
    else:
        parity = "Even"

    if integer >= 0:
        sign = "Positive"
    else:
        sign = "Negative"

    return [sign, parity]

sign, parity = sign_and_parity(12)
print sign, parity 

#    Then, write code that shows the calling of this function
#    on a number and unpack what is returned into two
#    variables --- sign and parity (whether it's even or odd).
#    Print sign and parity.


################################################################################
# PART TWO

def full_title(name, title="Engineer"):
    """ Return the person's title and name in one string.

    Take a name and a job title as parameters, making it so the job title 
    defaults to "Engineer" if a job title is not passed in."""

    # use concatenation '+' to ensure variables returned as one string
    return title + " " + name

def write_letter(name, title, sender):
    """ Given a recipient name & job title and a sender name, print a letter"""

    title = full_title(name, title)

    print "Dear {}, I think you are amazing! Sincerely, {}".format(title, sender)

def add_new_number(num, nums):
    """ Take a single number and add a list of numbers to it, returning a list of numbers. """

    return nums.append(num)

    

#####################################################################
# END OF PRACTICE: You can ignore everything below.

if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED. GOOD WORK!"
    print


