#7-1
requested_car = input("What kind of car would you like? ")
print('I\'ll try to find you a ' + requested_car)

#7-2
party = input("How many people are in your party? ")
party = int(party)
if party > 8:
    print('It will be a few minutes before we can seat you.')
else:
    print('Please follow the hostess to your table.')

#7-3
your_number = input('Please enter a number. ')
your_number = int(your_number)
if your_number % 10 == 0 :
    print('Yep, your number is a multiple of 10.')
else:
    print('Nope, your number is not a multiple of 10.')


#7-8 Deli
sandwich_orders = ['meatball','hero','philly','bobby','monte cristco']
finished_sandwiches = []
while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print('I made a ' + current_sandwich.title() + ' sandwich...it looks ifo')
    finished_sandwiches.append(current_sandwich)

i=1
for sand in finished_sandwiches:
    if i==1:
        print('\nHere is a list of all the sandwhiches that I made:')
    print('\t' + str(i) + '. ' + sand.title())
    i += 1

#7-9 Deli
sandwich_orders = ['pastrami','meatball','hero','pastrami','philly','bobby','monte cristco','pastrami','tuna']
print('86 Pastrami sandwiches')
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
finished_sandwiches = []
while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print('I made a ' + current_sandwich.title() + ' sandwich...it looks ifo')
    finished_sandwiches.append(current_sandwich)

i=1
for sand in finished_sandwiches:
    if i==1:
        print('\nHere is a list of all the sandwhiches that I made:')
    print('\t' + str(i) + '. ' + sand.title())
    i += 1

#7-10
vacation_spots = {}

active = True

while active:
    again = ''
    name = input("What is your name? ")
    spot = input("Where would you like to go? ")
    vacation_spots[name] = spot
    while again.upper() not in ['Y','N']:
       again = input("Would you like to continue (y/n)? ")
    if again.upper() == 'N':
        active = False

print('\n')

for name, spot in vacation_spots.items():
    print(name.title() + ' would like to visit ' + spot.title())