# pcost.py
#
# Exercise 1.27

# Total cost variable
total = 0

# Open portfolio file
with open('Data/portfolio.csv', 'rt') as file:
    # Get header
    header = next(file)

    # Add cost of purchasing all shares
    for line in file:
        stock = line.split(',')
        total += int(stock[1]) * float(stock[2])

print(f'Total cost {total}')