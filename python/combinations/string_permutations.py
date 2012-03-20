# encoding: utf-8
"""
Returns all permutations of a given string.

@author: Ofir Picazo - ofirpicazo@gmail.com
@date: March 2012
"""


def get_permutations(input_string):
    permutations = []

    if len(input_string) == 1:
        permutations.append(input_string)
    else:
        previous_str = input_string[:-1]
        new_char = input_string[-1]
        previous_permutations = get_permutations(previous_str)

        for permutation in previous_permutations:
            permutation_length = len(permutation)
            i = 0

            while i <= permutation_length:
                new_permutation = permutation[:i] + new_char + permutation[i:]
                permutations.append(new_permutation)
                i += 1

    return permutations
