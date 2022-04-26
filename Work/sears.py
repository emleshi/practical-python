# One morning, you go out and place a dollar bill 
# on the sidewalk by the Sears tower in Chicago. 
# Each day thereafter, you go out double the number 
# of bills. How long does it take for the stack 
# of bills to exceed the height of the tower?

h_tower = 442                   # height of Sear's tower in m
h_dollar = 0.11 * (10 ** -3)    # height of dollar bill in m
num_bills = 1
day = 1

while ((h_dollar * num_bills) < h_tower):
    num_bills = num_bills * 2
    day += 1
print (day)
