#!/usr/bin/python

import argparse


# First Pass
def find_max_profit(prices):
    difference_list = []
    for i in range(1, len(prices)):
        j = i + 1
        while j < len(prices):
            diff = prices[j] - prices[i]
            difference_list.append(diff)
            j += 1
    return max(difference_list)


if __name__ == '__main__':
    # This is just some code to accept inputs from the command line
    parser = argparse.ArgumentParser(description='Find max profit from prices.')
    parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
    args = parser.parse_args()

    print("A profit of ${profit} can be made from the stock prices {prices}.".format(
        profit=find_max_profit(args.integers), prices=args.integers))

# print(find_max_profit([1050, 270, 1540, 3800, 2]))
# print(find_max_profit([100, 90, 80, 50, 20, 10]))
