burger_cost = 2.99
fries_cost = 1.99
soda_cost = 1.75
print('Hello! Welcome to our automated order window!')
print('Burgers', burger_cost)
print('Fries', fries_cost)
print('Sodas', soda_cost)
b = int(input('How many burgers would you like?'))
f = int(input('How many fries would you like?'))
s = int(input('How many sodas would you like?'))
total = burger_cost * b + fries_cost * f + soda_cost * s
print('Thank you your total is %.2f' % total)
payment = float(input('How much money are you paying with?'))
print('Thank you. Your change is %.2f' % (payment - total))

