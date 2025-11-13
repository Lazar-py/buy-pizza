print('Welcome to Python Pizza deliveries!')
size = input('What size pizza do you want? S, M, or L ')
pepperoni = input('Do you want pepperoni on your pizza? Y or N')
extra_cheese = input('Do you want extra cheese? Y or N')

size_of_pizza = 0
extra_pepperoni = 0
cheese = 0


if size == 'S':
    size_of_pizza = 15
    if pepperoni == 'Y':
        extra_pepperoni = 2
    else:
        print('No pepperoni')
    if extra_cheese == 'Y':
        cheese = 1
    else:
        print('No extra cheese')
elif size == 'M':
    size_of_pizza = 20
    if pepperoni == 'Y':
        extra_pepperoni = 3
    else:
        print('No pepperoni')
    if extra_cheese == 'Y':
        cheese = 1
    else:
        print('No extra cheese')
elif size == 'L':
    size_of_pizza = 25
    if pepperoni == 'Y':
        extra_pepperoni = 3
    if extra_cheese == 'Y':
        cheese = 1
    else:
        print('No extra cheese')

totalBill = size_of_pizza + extra_pepperoni + cheese
print(f'Your final bill is ${totalBill}')