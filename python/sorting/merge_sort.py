# encoding: utf-8
"""
Merge sort implementation.

@author: Ofir Picazo - ofirpicazo@gmail.com
@date: March 2012
"""


def merge_sort(input_list):
    length = len(input_list)
    if length < 2:
        return input_list

    middle = length // 2
    left = merge_sort(input_list[:middle])
    right = merge_sort(input_list[middle:])

    return _merge(left, right)


def _merge(left, right):
    # Optimization!
    if left[-1] <= right[0]:
        return left + right

    result = []
    left_length = len(left)
    right_length = len(right)
    r, l = 0, 0
    while l < left_length and r < right_length:
        if left[l] <= right[r]:
            result.append(left[l])
            l += 1
        else:
            result.append(right[r])
            r += 1
    result += left[l:]
    result += right[r:]
    return result
