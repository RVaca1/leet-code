# Problem 1: Sum of Even Numbers in a List
#
# Description:
# Given a list of integers, return the sum of all even numbers in the list.


def sum_even(list_nums):

    sum_even_total = 0

    for num in list_nums:
        if num % 2 == 0:
            sum_even_total += num

    return sum_even_total




input_test = [1,2,3,4,5,6]
# should return 12

print(sum_even(input_test))



# possible improvement

def sum_even_improved(list_nums):
    return sum(num for num in list_nums if num % 2 == 0)
print(sum_even_improved(input_test))
