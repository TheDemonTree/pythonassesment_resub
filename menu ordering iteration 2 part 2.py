#  this is the second iteration of my DIT assessment code
# this code will have dictionaries and lists to make it more simple
# this code is the dictionary, lists, and other variables, as well as the food prices.
total = 0
name = input('Enter your name: ')
while True:
    try:
        age = int(input('Enter your age: '))
        break
    except ValueError:
        print('Please enter a valid integer: ')
bun = {'sesame': 2.00, 'white': 1.50, 'wholemeal': 2.00, 'no bun': 0.00}
patty = {'beef': 3.00, 'chicken': 3.00, 'pork': 2.50, 'no patty': 0.00}
extra = {'cheese': 1.50, 'tomato': 1.00, 'lettuce': 1.00, 'no extra': 0.00}
sauce = {'BBQ': 0.50, 'tomato': 0.30, 'mayonnaise': 0.70, 'no sauce': 0.00}
sides = {'small fries': 2.00, 'large fries': 3.50, 'nuggets': 2.50, 'no sides': 0.00}
drink = {'soda': 2.50, 'milkshake': 3.50, 'beer': 3.00, 'no drink': 0.00}

print('Welcome to')
print('-----BURGER BUILDER-----')
print('')

# this code shows the choices of bun, and allows the user to order their bun
print("BUN TYPES:")
for key, value in bun.items():
    print(f"{key} is {value} dollars")
bun_choice = input('Enter your choice of bun: ')
while bun_choice not in bun:
    print('This item is not in the menu')
    bun_choice = input('Enter your choice of bun: ')
bprice = bun[bun_choice]
total += bprice
print('')

# this code shows the choices of patties, and allows the user to order patties
print('PATTY TYPES:')
for key, value in patty.items():
    print(f"{key} is {value} dollars")
patty_choice = input('enter your choice of patty: ')
while patty_choice not in patty:
    print('this item is not in the menu')
    patty_choice = input('enter your choice of patty: ')
pprice = patty[patty_choice]
total += pprice
print('')

# this code shows the choices of extras, and allows the user to order extras
print('EXTRA CHOICES')
for key, value in extra.items():
    print(f"{key} is {value} dollars")
extra_choice = input('enter your choice of extras: ')
while extra_choice not in extra:
    print('this item is not in the menu')
    extra_choice = input('enter your choice of extras: ')
eprice = extra[extra_choice]
total += eprice
print('')

# this code shows the choices of sauce, and allows the user to order sauce
print('SAUCE CHOICES')
for key, value in sauce.items():
    print(f"{key} is {value} dollars")
sauce_choice = input('enter your choice of sauce: ')
while sauce_choice not in sauce:
    print('this item is not in the menu')
    sauce_choice = input('enter your choice of sauce: ')
sprice = sauce[sauce_choice]
total += sprice
print('')

# this code shows the choices of sides, and allows the user to order sides
print('SIDE CHOICES')
for key, value in sides.items():
    print(f"{key} is {value} dollars")
side_choice = input('enter your choice of sides: ')
while side_choice not in sides:
    print('this item is not in the menu')
    side_choice = input('enter your choice of sides: ')
siprice = sides[side_choice]
total += siprice
print('')

# this code shows the choices of drinks, and allows the user to order drinks
print('DRINK CHOICES')
for key, value in drink.items():
    print(f"{key} is {value} dollars")
drink_choice = input('enter your choice drink: ')
while drink_choice not in drink:
    print('this item is not in the menu')
    drink_choice = input('enter your choice of drink: ')
# this code while stop any underage people from ordering beer
while drink_choice == 'beer':
    if age <= 17:
        print('you are not eligible for alcohol')
        drink_choice = input('enter your choice of drink: ')
        while drink_choice not in drink:
            print('this item is not in the menu')
            drink_choice = input('enter your choice of drink: ')
    elif age >= 18:
        print('you are eligible for alcohol')
        break
print('')
dprice = drink[drink_choice]
total += dprice
# this code gets the total price and then thanks the customer and prints the price
print('Thank you for choosing burger builder!')
print('Your cost of ordering is', total,)
print(name, ', your order will be ready within 10-20 minutes')
