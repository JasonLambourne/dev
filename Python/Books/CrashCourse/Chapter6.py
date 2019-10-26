#-----------------------------------------------------------------------------------------------------------------------
#Chapter 6 - Dictionaries
#-------------------------------------------------------------------------------------------------------
#Functions, Methods, Keywords, etc.
#-------------------------------------------------------------------------------------------------------
Empty dictionary definition - use blank curly braces to create a blank dictionary myDictionary = {}
Separate Key:Values with a ":" and then delimit with a ","
Access dictionary value by the key - print(dictionary['key'])
To remove a key value pair use the del statement - del dictionary['key']
#-------------------------------------------------------------------------------------------------------
#Exercises - these can be out of order because later exercises can build on earlier ones
#-------------------------------------------------------------------------------------------------------
#6-1. Person
Person = {}
Person['first_name'] = 'Michael'
Person['last_name'] = 'Scott'
Person['age'] = '44'
Person['city'] = 'Scranton'
print(Person)

#6-2 Favorite Numbers
favorite_numbers = {}
favorite_numbers['Jim'] = 3
favorite_numbers['Pam'] = 14
favorite_numbers['Dwight'] = 357
favorite_numbers['Stanley'] = 10
favorite_numbers['Kelly'] = 8675309
print('Jim\'s favorie number is ' + str(favorite_numbers['Jim']))
print('Pam\'s favorie number is ' + str(favorite_numbers['Pam']))
print('Dwight\'s favorie number is ' + str(favorite_numbers['Dwight']))
print('Stanley\'s favorie number is ' + str(favorite_numbers['Stanley']))
print('Kelly\'s favorie number is ' + str(favorite_numbers['Kelly']))

#6-3 Glossary
glossary = {}
glossary['function'] = 'reusable chunk of code that isn\'t part of a class'
glossary['dictionary'] = 'advanced data structure based on key:value pairs'
glossary['list'] = 'variable type that holds multiple values similar to an array'
glossary['range'] = 'numeric function that produces a range of numbers'
glossary['boolean'] = 'variable type with two values - true or false'
print('function:\n ' + glossary['function'] + '\n')
print('dictionary:\n ' + glossary['dictionary'] + '\n')
print('list:\n ' + glossary['list'] + '\n')
print('range:\n ' + glossary['range'] + '\n')
print('boolean:\n ' + glossary['boolean'] + '\n')

#6-7. People
people = []
person1 = {
    'first_name':'Michael'
    ,'last_name':'Scott'
    ,'age':44
    ,'city':'Scranton'
    ,'st':'PA'
    }
person2 = {
    'first_name':'Dwight'
    ,'last_name':'Schrewt'
    ,'age':38
    ,'city':'Scranton'
    ,'st':'PA'
    }
people.append(person1)
people.append(person2)
for person in people:
    for key, value in person.items():
        print(str(key.title()) + ':' + str(value))
    print('\n')

#6-8 Pets
pets = []
fido = {
    'animal':'dog'
    ,'owner':'Jim'
    }
sebastian = {
    'animal':'cat'
    ,'owner':'Sabrina'
    }
nemo = {
    'animal':'fish'
    ,'owner':'Darla'
    }
polly= {
    'animal':'parrot'
    ,'owner':'John Silver'
    }
pets.append(fido)
pets.append(sebastian)
pets.append(nemo)
pets.append(polly)
for pet in pets:
    for key, value in pet.items():
        print(str(key.title()) + ' : ' + str(value))
    print('\n')

#6-9 Favorite Places
favorite_places = {
     'Jim':'Gary, IN'
    ,'Jack':'Parris, France'
    ,'Bill':'Parris, Idaho'
    }
for k,v in favorite_places.items():
    print(k + '\'s favorite place is ' + v)

#6-10 Favorite Places
favorite_numbers = {}
favorite_numbers['Jim'] = [1,2]
favorite_numbers['Pam'] = [11,22]
favorite_numbers['Dwight'] = [111,211]
favorite_numbers['Stanley'] = [122,233]
favorite_numbers['Kelly'] = [144,2555,3,301]

print(favorite_numbers)
for k, v in favorite_numbers.items():
    print(k + ' ' + str(v))

#6-11 Cities
cities = {
    'Salt Lake City':{
       'country':'USA',
       'population':'2,000,000',
       'fact':'uses the grid system'
    }
    ,'Keaukaha':{
       'country':'USA',
       'population':'1,000',
       'fact':'home to Ken\'s pancake house'
    }
    ,'LA':{
       'country':'USA',
       'population':'10,000,000',
       'fact':'has two NBA basketball teams'
    }
}

for key,value in cities.items():
    print('Did you know that ' + key +':')
    for key2, value2 in value.items():
        if key2 == 'country':
            print('\tIs in the ' + value2)
        elif key2 == 'population':
            print('\tHas approximately '+ value2 +' people living there.')
        elif key2 == 'fact':
            print('\tIt also '+ value2 +'.')