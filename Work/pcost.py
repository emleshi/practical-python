# pcost.py
#
# Exercise 1.27

def portfolio_cost(filename):
    # Total cost variable
    total = 0

    # Open portfolio file
    with open(filename, 'rt') as file:
        # Get header
        try:
            header = next(file)
        except ValueError:
            print('Header could not be read')

        # Add cost of purchasing all shares
        for line in file:
            try:
                stock = line.split(',')
                total += int(stock[1]) * float(stock[2])
            except ValueError:
                print('Data could not be read')

    return total

cost = portfolio_cost('Data/portfolio.csv')
print(f'Total cost {cost}')