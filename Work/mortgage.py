# mortgage.py
#
# Exercise 1.7

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
month = 0

extra_payment = 1000.0
extra_payment_start_month = 61
extra_payment_end_month = 108

while principal > 0:
    month += 1

    principal = principal * (1+rate/12) - payment
    total_paid = total_paid + payment
   
    if month >= extra_payment_start_month and month <= extra_payment_end_month:
        principal -= extra_payment
        total_paid += extra_payment

    if principal < 0:
        principal = 0
    
    print(f'{month} {round(total_paid,2):0.2f} {round(principal,2):0.2f}')


print(f'\nTotal paid\t{round(total_paid,2)}')
print(f'Months\t\t{month}')
