def calculate_total_cost(default_tax_rate, state_abbr, cost):
    """ Calculate an item cost by adding tax appropriate for state. 

    For example::

        >>> calculate_total_cost(5, "CA", 20)
        21.4

        >>> calculate_total_cost(10, "AK", 10)
        11.0

        >>> calculate_total_cost("", "ME", 10)
        10.5
    """

    if state_abbr == "CA":
        default_tax_rate = float(7) /100 
    elif default_tax_rate:
        default_tax_rate = float(default_tax_rate) /100
    else:
        default_tax_rate = float(5) /100

    total_cost = (default_tax_rate * cost) + cost
    return total_cost



#####################################################################
def is_berry(fruit):
    """ Takes a fruit name as a string and returns a boolean if the fruit is a strawberry, cherry, or blackberry.

    For example::

        >>> is_berry("Strawberry")
        True

        >>> is_berry("cherry")
        True

        >>> is_berry("ham")
        False
    """

    berries = ["strawberry", "cherry",  "blackberry"]
    for berry in berries:
        if fruit.lower() == berry:
            return True
    return False


def shipping_cost(fruit):
    """ Calculates shipping cost.

    Requires fruit name to be passed and the is_berry function.

    For example::

        >>> shipping_cost("Strawberry")
        '0'

        >>> shipping_cost("banana")
        '5'


    """
    if fruit:
        result = is_berry(fruit)
    if result == True:
        return '0'
    elif result == False:
        return '5'
    else:
        return None



def is_hometown(town_name):
    """ Takes a town name and tells if it is your hometown..

    For example::

        >>> is_hometown("San Francisco")
        True

        >>> is_hometown("Anchorage")
        False


    """
    hometown = "San Francisco"
    if town_name == hometown:
        return True
    else:
        return False

def full_name(first_name, last_name):
    """ Takes a first and last name and returns full name.

    For example:

        >>> full_name("Manisha", "Patel")
        'Manisha Patel'

        >>> full_name("Sam", "Spade")
        'Sam Spade'

    """
    return first_name + " " + last_name

def hometown_greeting(town_name, first_name, last_name):
    """ Prints a personalized greeting.

    For example:

        >>> hometown_greeting("San Francisco", "Manisha", "Patel")
        Hi Manisha Patel, we're from the same place!

    """
    greeting = full_name(first_name, last_name)
    if is_hometown(town_name):
        msg = "Hi {}, we're from the same place!".format(greeting)
    else:
        msg = "Hi {}, where are you from?".format(greeting)

    print msg

#####################################################################

def increment(y, x=1):
    """ Increment passed value by the value.

    For example:

        >>> increment(5)
        6

        >>> increment(15, 4)
        19


    """

    def add(y):
        result = x + y
        return result

    result = add(y)

    #print result
    return result


addfive = increment(0, 5)
addfive = increment(20)
addfive = increment(5)

def join_numbers(number, list_of_numbers):
    """ takes in a number and a list of numbers. It should append the number to the list of numbers and return the list.

    For example:

        >>> join_numbers(2, [3, 4, 5])
        [3, 4, 5, 2]


    """

    list_of_numbers.append(number)
    return list_of_numbers


# 3. Make a function that takes in a number and a list of numbers. It should append
#    the number to the list of numbers and return the list.


#####################################################################

# END OF ASSESSMENT: You can ignore everything below.

if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED. GOOD WORK!"
    print