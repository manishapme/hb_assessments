#Sorting

def bubble_sort(lst):
    """returns a sorted list using a optimized bubble sort algorithm
    i.e. using a variable to track if there hasn't been a swap
        >>> bubble_sort([3, 5, 7, 2, 4, 1])
        [1, 2, 3, 4, 5, 7]
    """
    # couldn't do this without rereading handouts
    for i in range(len(lst)-1):
        for j in range(len(lst)-1-i):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j] 

    return lst
        




def merge_lists(list1, list2):
    """Given two sorted lists of integers, returns a single sorted list containing all
    integers in the input lists
    >>> merge_lists([1, 3, 9], [4, 7, 11])
    [1, 3, 4, 7, 9, 11]
    """


    new_list = []

    while list1 or list2:
        if not list1:
            new_list.append(list2.pop(0))
        elif not list2:
            new_list.append(list1.pop(0))
        elif list1[0] > list2[0]:
            new_list.append(list2.pop(0))
        elif list2[0] > list1[0]:
            new_list.append(list1.pop(0))

    return new_list            


##########ADVANCED##########
def merge_sort(lst):
    """
    Given a list, returns a sorted version of that list.
    Finish the merge sort algorithm by writing another function that
    that takes in a single unsorted list of integers and uses recursion and the 'merge_lists'
    function you already wrote to return a new sorted list containing all integers from
    thin input list. In other words, the new function should sort a list using merge_lists
    and recursion.
    >>> merge_sort([6, 2, 3, 9, 0, 1])
    [0, 1, 2, 3, 6, 9]
    """
    if len(lst) < 2:
        return lst

    mid = int(len(lst)/2)
    lst1 = merge_sort(lst[0:mid])
    lst2 = merge_sort(lst[mid:])

    return merge_join(lst1, lst2)


def merge_join(lst1, lst2):
    """Given two lists that are s orted, merge them into one list"""

    new_list = []
    while lst1 or lst2:
        if not lst1:
            new_list.append(lst2.pop(0))

        elif not lst2:
            new_list.append(lst1.pop(0))

        elif lst1[0] > lst2[0]:
            new_list.append(lst2.pop(0))

        elif lst2[0] > lst1[0]:
            new_list.append(lst1.pop(0))

    return new_list





#####################################################################
# END OF ASSIGNMENT: You can ignore everything below.

if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED. GOOD WORK!"
    print