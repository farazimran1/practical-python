# pcost.py
#
# Exercise 1.27

import csv
import sys


def portfolio_cost(filename):
    with open(filename, "+rt") as file:
        rows = csv.reader(file)
        next(rows)
        total_cost = 0
        for row in rows:
            try:
                total_cost += int(row[1]) * float(row[2])
            except (ValueError, IndexError):
                print("couldn't parse line")
    return total_cost


if len(sys.argv) == 2:
    cost = portfolio_cost(sys.argv[1])
    print(f"Total cost {cost:.2f}")
else:
    print("usage: python pcost.py <portfolio.csv>")
    sys.exit(1)
