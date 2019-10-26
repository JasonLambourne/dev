#-----------------------------------------------------------------------------------------------------------------------
#Chapter 5
#-----------------------------------------------------------------------------------------------------------------------
#Functions, keywords, classes, methods, etc.
#-----------------------------------------------------------------------------------------------------------------------
in/not in keywords - act the same as in SQL

#-----------------------------------------------------------------------------------------------------------------------
#Exercises
#-----------------------------------------------------------------------------------------------------------------------
#5-1
Keeper = ['Leno','Chech']
AttackingMid = ['Ozil','Torreria','Mkhi']
CenterMid = ['Ramsey','Xhaka']
HoldingMid = ['Guendouzi','Ramsey']
Forward = ['Auba','Laca','Iwobi','Welbeck']
CenterBack = 'Mustafi'
LeftBack = 'Monreal'
RightBack = 'Kolasinac'

print('Is Ozil an attacking mid?')
print('Answer is...' + str('Ozil' in AttackingMid))

print('\nIs Ramsey an attacking mid?')
print('Answer is...' + str('Ramsey' in AttackingMid))

print('\nIs Ramsey a CenterMid mid?')
print('Answer is...' + str('Ramsey' in CenterMid))

print('\nIs Monreal a LeftBack ?')
print('Answer is...' + str('Monreal' == LeftBack))

print('\nIs Monreal a CenterBack ?')
print('Answer is...' + str('Monreal' == CenterBack))

#5-2
print('1. '+ str('blah' == 'BLAH'))
print('2. '+ str('blah'.upper() == 'BLAH'))
print('3. '+ str('BLAH'.lower() == 'BLAH'))
print('4. '+ str('BLAH'.lower() == 'blah'))

for number in range(5,11):
    print(str(number)+'. ' + str(number <= 8))

nba_all_stars = ['MJ','Lebron','KD','Steph']
print('11. '+ str('KD' in nba_all_stars))
print('12. '+ str('Westbrook' in nba_all_stars))
print('13. '+ str('MJ' not in nba_all_stars))

#5-3
for number in range(1,30):
    if number != 1:
        alien_color = 'green'
    else:
        alien_color = 'red'
    if alien_color == 'green':
        print('You just earned 5 points!')
#5-4
green_list = list(range(0,102,3))
for number in range(1,10):
    if number in green_list:
        print('You just earned 5 points!')
    else:
        print('You just earned 10 points!')

#5-5
green_list = list(range(0,102,2))
yellow_list = list(range(0,102,3))
red_list = list(range(0,102))

for number in range(1,10):
    if number in green_list:
        print('You just earned 5 points!')
    elif number in yellow_list:
        print('You just earned 10 points!')
    else:
        print('You just earned 15 points!')

#5-6
for age in range(1,75,4):
    if age < 2:
        print('You\'re a baby.')
    elif age >= 2 and age < 4:
        print('You\'re a toddler.')
    elif age >= 4 and age < 13:
        print('You\'re a kid.')
    elif age >= 13 and age < 20:
        print('You\'re a teenager.')
    elif age >= 20 and age < 65:
        print('You\'re a adult.')
    else:
        print('You\'re a seasoned citizen.')

#5-7
favorite_fruits = ['apple','oragne','pear','banana','mango','papya','berries']
fruits = favorite_fruits[3:]
fruits.append('grapefruit')
fruits.append('Darun')
fruits.append('Star Fruit')
fruits.append('plantaine')
fruits.sort()
for fruit in fruits:
    if fruit in favorite_fruits:
        print('So, you like ' +fruit +' too?')

#5-8&9
#users = ['admin','Bill','Bob','Jane','Sarah']
users = []
if users:
    for user in users:
        if user =='admin':
            print('Yo, want to check da status?')
        else:
            print('Yo, '+user.upper())
else:
    print('We need some users, yo.')
#5-10
current_users = ['Jeff','Dan','Brian','Tony','Matt']
new_users = current_users[3:]
new_users.append('Jerry')
new_users.append('Barry')
new_users.append('Terry')
new_users.sort()
if new_users:
    for user in new_users:
        if user in current_users:
            print('Sorry, burdda '+user+', no can use da name')
        else:
            print('Auuuuuuright brudda '+user+', CAN use da name!')
#5-11
numbers = list(range(1,10))
if numbers:
    for number in numbers:
        if number == 1:
            print(str(number)+'st')
        elif number == 2:
            print(str(number) + 'nd')
        elif number == 3:
            print(str(number) + 'rd')
        else:
            print(str(number) + 'th')
