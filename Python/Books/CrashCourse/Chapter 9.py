#9-1
class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(self.restaurant_name.title() + ' serves ' + self.cuisine_type.title() + ' food.')

    def open_restaurant(self):
        print(self.restaurant_name.title() + ' is now open.')

restaurant = Restaurant("Louie's",'Italiano')

print(restaurant.restaurant_name)
print(restaurant.cuisine_type)

restaurant.describe_restaurant()
restaurant.open_restaurant()

#9-2
class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(self.restaurant_name.title() + ' serves ' + self.cuisine_type.title() + ' food.')

    def open_restaurant(self):
        print(self.restaurant_name.title() + ' is now open.')

restaurant1 = Restaurant("Louie's",'Italiano')
restaurant2 = Restaurant("Rita's",'Mexicano')
restaurant3 = Restaurant("Coconut Grill",'Hay-way-ian')

restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()

#9-3 Users
class User():
    def __init__(self):
        self.first_name = input('Please input your First Name: ')
        self.last_name = input('Please input your Last Name: ')
        self.set_creds()

    def set_creds(self):
        self.user_name = input('Please input your User Name: ')
        self.password = input('Please enter your password: ')

    def print_all_user_info(self):
        self.print_user_name()
        self.print_creds()

    def print_user_name(self):
        print('First Name: ' + self.first_name)
        print('Last Name: ' + self.last_name)

    def print_creds(self):
        print('User Name: ' + self.user_name)
        print('Password: ' + self.password)

user1 = User()
user1.print_all_user_info()

#9-4
class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(self.restaurant_name.title() + ' serves ' + self.cuisine_type.title() + ' food.')

    def open_restaurant(self):
        print(self.restaurant_name.title() + ' is now open.')

    def set_number_served(self, people_served):
        self.number_served = people_served

    def increment_number_served(self):
        self.number_served += 12

Louies = Restaurant("Louie's",'Italiano')
Louies.set_number_served(10)
print(str(Louies.number_served))
i = 0
while i<5:
    Louies.increment_number_served()
    print(str(Louies.number_served))
    i+=1