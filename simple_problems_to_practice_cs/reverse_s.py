# Problem 2: Reverse a String
#
# Description:
# Given a string s, return the string reversed.

def reverse_string(s):
    return s[::-1]

def reverse_string_2(s):

    chars_list = []


    len_s = len(s)

    for i in range(len_s):
        chars_list.append(i)

    idx = len_s

    for char in s:

        chars_list[idx -1] = char
        if idx != 0:
            idx -= 1

    return ''.join(str(x) for x in chars_list)

sample_input = "frango"

print(reverse_string(sample_input))
print(reverse_string_2(sample_input))
