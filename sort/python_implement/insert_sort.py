#!/usr/bin/env python3
# coding: utf-8
#
# author: kaku
# date: 19/10/07

# GitHub:
#
#   https://github.com/kakukosaku
#
# © 2019-2022 Kaku Kosaku All Rights Reserved
#
# Usage:
#   python -m python_implement.insert_sort

from .array import random_array, show_array, check_sorted

ARRAY_SIZE = 10


def insert_sort(arr, array_size):
    """Insert Sort

    Notes:
        1. In Python arguments pass by reference to mutable variables, needn't return arr.
        2. Pass array size to function `even in Python can get array(list) len on runtime`.
        3. Replace for loop with while since Python for loop is not friendly to use index.

        4. Find the Right position; Move for space; Put it in.

    """
    i = 1  # Not handle Exception case
    while i < array_size:
        # from small to big
        if arr[i] < arr[i - 1]:
            temp = arr[i]
            j = i - 1
            while j >= 0 and arr[j] > temp:
                arr[j + 1] = arr[j]
                j -= 1

            arr[j + 1] = temp

        i += 1


if __name__ == '__main__':
    arr = random_array(ARRAY_SIZE)
    show_array(arr, "Original Array")
    insert_sort(arr, len(arr))
    show_array(arr, "After Insert Sort")
    check_sorted(arr)
