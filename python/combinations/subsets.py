# encoding: utf-8
"""
Returns all the subsets of a given set.

@author: Ofir Picazo - ofirpicazo@gmail.com
@date: March 2012
"""


def get_subsets(input_set):
    def _convert_combination_to_set(combination):
        subset = set()
        for i, value in enumerate(combination):
            if value == '1':
                subset.add(immutable_input_set[i])
        return subset

    subsets = []
    size = len(input_set)
    immutable_input_set = tuple(input_set)
    combination = 0

    while combination < 2**size:
        binary_combination = bin(combination)[2:].rjust(size, '0')
        subset = _convert_combination_to_set(binary_combination)
        subsets.append(subset)
        combination += 1
    return subsets
