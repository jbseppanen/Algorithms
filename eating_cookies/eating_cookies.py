#!/usr/bin/python

import sys


# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive 
# recursive solution
def eating_cookies(n, cache=None):
    if n == 1:
        return 1
    if n < 1:
        return 0
    counter = 0
    for i in range(1, n + 1):
        for j in range(1, 4):
            counter += eating_cookies(n-j)
    print(counter)
    return counter


# if __name__ == "__main__":
#     if len(sys.argv) > 1:
#         num_cookies = int(sys.argv[1])
#         print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(ways=eating_cookies(num_cookies),
#                                                                                     n=num_cookies))
#     else:
#         print('Usage: eating_cookies.py [num_cookies]')

print(eating_cookies(10))

