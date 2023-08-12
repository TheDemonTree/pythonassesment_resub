# this is the first program I will be making for the DIT programming assessment
# this program is for food ordering
total = 0
name = input('enter your name: ')
while True:
    try:
        age = int(input('Enter your age:'))
        break
    except ValueError:
        print('PLease enter a valid interger')
# this code is to print and show the user what the menu is.
print('welcome to the bbq palace')
print('please place order from following menu')
print('')
print('1 = pork ribs: 11.00, 2 = steak: 10.00, 3 = sausages: 7.00')
print('4 = cola: 2.50, 5 = sparkling water: 1.50, 6 =smoothie: 3.50')
while True:
    try:
        order = int(input('what would you like to order?(enter the number of the item and 0 to finish): '))
        break
    except ValueError:
        print('please enter a valid order')

# this code is to let the user order their items
while order != 0:
    try:
        if order == 1:
            total += 11.00
            order = int(input('what would you like to order?: '))
        if order == 2:
            total += 10.00
            order = int(input('what would you like to order?: '))
        if order == 3:
            total += 7.00
            order = int(input('what would you like to order?: '))
        if order == 4:
            total += 2.50
            order = int(input('what would you like to order?: '))
        if order == 5:
            total = total + 1.50
            order = int(input('what would you like to order?: '))
        if order == 6:
            total = total + 3.50
            order = int(input('what would you like to order?: '))
            break
    except ValueError:
        print('please enter a valid order.')
# this code is to show the user their total cost.
print('your total is', total)
print('your order will be ready soon', name)
