"""
The function written below constructs an integer based on the digits given in the list.
Let's say that our list contains digits [1, 2, 3, 4]. The resulting integer should have value of 1234.
We can think of constructing this number in the following way: 1234 = 1000 + 200 + 30 + 4.
If we look closely, we can see that each digit from the list is multiplied by 10^i, where i is the exponent starting
from 0 and is incrementing for each next digit. Note that we start from the last digit and keep moving to the left in the list

Thus, the expression can be rewritten as: 1234 = 1*(10^3) + 2*(10^2) + 3*(10^1) + 4*(10^0).
"""


def convert(lst):
    """
    The following code constructs an integer based on the digits given in the list. For example, if the list contains
    digits [1,2,3,4], the resulting integer will be 1234. We solve this problem by thinking of the resulting integer as
    a sum of numbers: 1234 can be presented as 1000 + 200 + 30 + 4.
    :param lst: a list of digits that will be used to construct an integer.
    :return: a newly constructed integer.
    """
    # Initialise the resulting integer as 0
    result = 0
    # Initialise the factor that will be increased with each new digit
    factor = 0

    # Go through all the digits in the list starting from the last digit
    # Constructing an integer process
    for i in range(len(lst) - 1, -1, -1):
        # Add a new part of the integer to the result variable
        result = result + (lst[i] * (10 ** factor))
        # Increment the factor by 1 with each iteration
        factor += 1
    return result


def main():
    """
    The main function performs several calls to the convert function on different lists to perform testing.
    """
    print(convert([8, 3, 5, 1]))
    print(convert([1, 2, 3, 4, 5, 6]))
    print(convert([9, 5, 2]))


main()
