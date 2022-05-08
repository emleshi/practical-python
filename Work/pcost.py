# pcost.py
#
# Exercise 1.27

def portfolio_cost(filename):
    # Total cost variable
    total = 0

    # Open portfolio file
    with open(filename, 'rt') as file:
        # Get header
        header = next(file)

        # Add cost of purchasing all shares
        for line in file:
            stock = line.split(',')
            total += int(stock[1]) * float(stock[2])

    return total

cost = portfolio_cost('Data/portfolio.csv')
print(f'Total cost {cost}')