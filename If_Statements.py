#If Statements
is_hot = False
is_cold = False
if is_hot:
    print("\nit's a hot day")
    print('\ndrink a lots of water')
elif is_cold:
    print("\nit's a cold day")
    print("\nwear warm clothes")
else:
    print("\nIt's a lovely day")
print("\nenjoy your day")
#eg
price = 1000000
has_good_credit = True
if has_good_credit:
    down_payment = 0.1 * price
else:
    down_payment = 2.0 * price
print(f"Down paymnet : ${down_payment}")