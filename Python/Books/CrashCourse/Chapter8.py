#8-1 Message
def display_message():
    print("This chapter is about functions.")

display_message()

#8-2 Favorite Book
def favorite_book(title):
    print("One of my favorite books is " + title.title())

favorite_book('ready player one')

#8-3 T-Shirt
def make_shirt(size,shirt_text):
    print('Shirt Size: '+ size.upper() + ' \nShirt text: ' + shirt_text + '\n')

make_shirt('XXL','Living Large')
make_shirt(shirt_text='Taco Time', size='l')

#8-4 Large Shirts
def make_shirt(size='L',shirt_text='Python is da bomb'):
    print('Shirt Size: '+ size.upper() + ' \nShirt text: ' + shirt_text + '\n')

make_shirt()
make_shirt('M')
make_shirt(shirt_text='#TacoTime', size='xxxl')

#8-5 Cities
def describe_city(city_name, country_name='United States'):
    print(city_name.title() + ' is in ' + country_name.title())

describe_city('SLC')
describe_city('NYC')
describe_city('Paris', 'France')

#8-6
def city_county(city,country):
    formatted_info = city.title()+', ' + country.title()
    return formatted_info

print(city_county('paris','france'))
print(city_county('Bismark','usa'))
print(city_county('london','england'))

#8-7
def make_album(artist,album_title,track_count=0):
    album = {'artist':artist,'album_title':album_title}
    if track_count:
        album['track_count']=track_count
    return album
albums = []

albums.append(make_album('Dr Dre','The Chronic'))
albums.append(make_album('Snoop Dog','Doggy Style'))
albums.append(make_album('Bob Marley','Excedous'))

albums.append(make_album('DJ Rectangle','Ill Rated',10))

for album in albums:
    print(album)

#8-8
def make_album(artist,album_title,track_count=0):
    album = {'artist':artist,'album_title':album_title}
    if track_count:
        album['track_count']=track_count
    return album

albums = []
active = True

while active:
    input_artist = input('Enter an arist. ')
    input_album = input('Enter an album. ')
    input_again = input('Do you want to enter another? (y/n) ')
    if input_again.upper() != 'Y':
        active = False
    albums.append(make_album(input_artist,input_album))

i=1
for album in albums:
    print(str(i) + '. ' + album['artist'] + ' - ' + album['album_title'])
    i+=1

#8-9&10 Magicians
def show_magicians(list_of_magicians):
    for person in list_of_magicians:
        print(person.title())

def make_great(list_to_make_great):
    list_count = len(list_to_make_great)
    i = 0
    while i < list_count:
        list_to_make_great[i] = 'The Great ' + list_to_make_great[i]
        i+=1

magicians = ['harry hoodini','david copperfield','chris angel','shen len']
make_great(magicians)
show_magicians(magicians)

#8-11 Magicians
def show_magicians(list_of_magicians):
    for person in list_of_magicians:
        print(person.title())

def make_great(list_to_make_great):
    new_list = []
    list_count = len(list_to_make_great)
    i = 0
    while i < list_count:
        new_list.append('The Great ' + list_to_make_great[i])
        i+=1
    return new_list

magicians = ['harry hoodini','david copperfield','chris angel','shen len']
great_magicians = make_great(magicians[:])
show_magicians(magicians)
print('-'*40)
show_magicians(great_magicians)

#8-12 Sandwiches
def my_sandwich(*sandwich_items):
    for item in sandwich_items:
        print(item.title())
    print('\n')

my_sandwich('turkey','bacon','avacado')
my_sandwich('roast beef','mayo')
my_sandwich('egg plant parm','mozerlla')

#8-13 Cars
def make_car(make,model,**car_data):
    car_info = {}
    car_info['make'] = make
    car_info['model'] = model
    for key, value in car_data.items():
        car_info[key] = value
    return car_info

mycar = make_car('toyota','4runner',rims='22s',interior='black leather')
yourcar = make_car('honda','civic',color='white',drive='4WD')

print(mycar)
print(yourcar)