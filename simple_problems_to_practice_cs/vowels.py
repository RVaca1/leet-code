# Count Vowels in a String (Easy)
#
# Description:
# Given a string s, count the number of vowels (a, e, i, o, u) in it.

def vowels_count(word):
    # define all vowels
    vowels = ['a','e','i','o','u']
    # Init

    q_vowels = 0


    for letter in word:
        if letter in vowels:
            q_vowels += 1

    return q_vowels



input_problem = "frango"
print(vowels_count(input_problem))
 # vowels in this example = a and o so vowels count = 2

