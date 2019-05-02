#!/usr/bin/python

import sys
from copy import deepcopy


# First Pass
def rock_paper_scissors(n):
    def inner_recurse(list_of_lists):
        list_rock = deepcopy(list_of_lists)
        list_paper = deepcopy(list_of_lists)
        list_scissors = deepcopy(list_of_lists)
        for r in list_rock:
            r.append("rock")
        for p in list_paper:
            p.append("paper")
        for s in list_scissors:
            s.append("scissors")
        return list_rock + list_paper + list_scissors

    array_of_lists = [[]]
    for i in range(n):
        array_of_lists = inner_recurse(array_of_lists)
    print("<----------Order may not match the unit tests.---------->")
    return array_of_lists


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_plays = int(sys.argv[1])
        print(rock_paper_scissors(num_plays))
    else:
        print('Usage: rps.py [num_plays]')

# print(rock_paper_scissors(2))
