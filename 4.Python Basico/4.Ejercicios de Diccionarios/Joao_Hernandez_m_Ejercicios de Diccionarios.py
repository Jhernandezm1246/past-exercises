#Excercise 1 

# Create a diccionary that holds the following information from a hotel name, number of stars , rooms 

# The key value for room has to be a list that holds the following information, number, floor, price per night 

dic_hotels = {
    
    

}

room_list_info = []

name_of_hotel = str(input("Type the hotel name: "))
hotel_of_rooms = int(input("Type the amount of rooms: "))
hotel_of_stars = int(input("Type the amount of stars from 1 to 5: "))

counter = 0 

while counter < hotel_of_rooms:
    hotel_of_room = int(input("Type the hotel room number: "))
    room_floor = int(input("Type the room floor: "))
    price_per_night = float(input("Price per night: "))
    counter += 1 

    entry_dict = dict(Room_number = hotel_of_room, Price = price_per_night, Floor = room_floor) 
    room_list_info.append(entry_dict)


dic_hotels["name"] = name_of_hotel
dic_hotels["room"] = room_list_info
dic_hotels["number of stars"] = hotel_of_stars



print(dic_hotels)


#Excercise 2
#Create a program that combines 2 lists with the same size using 1 for their keys and other for its values 
dic_list = {}

list_a = ["first_name","last_name","role"]
list_b = ["Joao","hernandez","Software Engineer"]




dic_list = dict(zip(list_a, list_b))



print(dic_list)



#Excercise 3 
#Create a program uses a list that delets keys from a diccionary 

list_of_keys = ["access_level", "age"]
employee = {"name": "John", "email": "john@ecorp.com", "access_level": 5, "age": 28}

for key in list_of_keys:
    employee.pop(key)

print(employee)




