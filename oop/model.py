import json
import os

if os.path.exists("db_users.json"):
    try:
        with open("db_users.json", "r") as f:
            user_data = json.load(f)
    except json.JSONDecodeError:
        user_data = []
else:
    user_data = []

# User object
# Blue print for user object
class User:
    # Constructor for user object
    def __init__(self, username, role, password):
        # All necessary fields to create the constructor 
        self.username = username
        self.role = role
        self.password = password

    # A method to display all available users in the list
    # Added indexing to make the list more readable
    # The conditional statement checks if users exist or not inside the users list 
    def display_all_users(self):
        print("All Users: ")

        if user_data:
            index = 0
            for u in user_data:
                index = index + 1
                print(f"{index}. {u}")
        else: 
            print("No users found. please add one!")

    # A method to add a new user to the list
    # The new user information is stored in a user_info dictionary and then added into the list
    def create_user(self):
        user_info = {}

        print("Enter user information below,")
        username = input("Enter Username: ")
        role = input("Enter role: ")
        password = input("Enter password: ")

        user_info["username"] = username
        user_info["role"] = role
        user_info["password"] = password

        self.users.append(user_info)
        print(f"User {username} added successfully!")
        
        user_data.append(user_info)

        with open("db_users.json", "w") as f:
            json.dump(user_data, f, indent=4)

        if role == 'admin':
            self.display_all_users()

    # A method to update a user information
    def update_user(self):
        print("Select user to update")
        user = input("Enter username here: ")

        # Loop through the user data to find the user to be updated
        for u in user_data:
            #It checks conditionally if the user exists in the list or not
            if u["username"] == user:
                username = input("Update username: ")
                role = input("Update user role: ")
                password = input("Update user password: ")
                # if the user found then update the fields with necessary values
                u["username"] = username
                u["role"] = role
                u["password"] = password

                with open("db_users.json", "w") as f:
                    json.dump(user_data, f, indent=4)

                print(f"User {user} updated successfully!")
            else:
                # Fall back if the user not found
                print("User not found. Please try again!")

    # This method removes a user from the list if you provide a value for username key
    def remove_user(self):
        print("Remove user")
        username = input("Enter username: ")
        # it looks for the username provided
        for u in user_data:
            # if found it will be removed
            if u["username"] == username:
                user_data.remove(u) 
                print(f"User {username} has been removed successfully!")
                with open("db_users.json", "w") as f:
                    json.dump(user_data, f, indent=4)
            # if not found, fallback to error message
            else:
                print("User not found. Please try again!")

    # Based on the given username value this method tries to display  a user info
    # It is a simple search method
    def display_user_info(self):
        if not user_data:
            print("No users found!")

        print("Search user here")
        username = input("Enter username: ")
        for u in user_data:
            if u["username"] == username:
                print(f"{u}")
            


if os.path.exists("db_flights.json"):
    try:
        with open("db_flights.json", "r") as f:
            flight_data = json.load(f)
    except json.JSONDecodeError:
        flight_data = []
else:
    flight_data = []

class Flight():
    def __init__(self, place, day, time, amount):
        self.place = place
        self.day = day
        self.time = time
        self.amount = amount

    def create_flights(self):
        flight_info = {}

        print("Create New Flight: ")
        place = input("Enter place: ")
        day = input("Enter flight day: ")
        time = input("Enter flight time: ")
        amount = input("Enter flight payment: ")

        flight_info["Place"] = place
        flight_info["Day"] = day
        flight_info["Time"] = time
        flight_info["Amount"] = amount
        
        flight = flight_info
        flight_data.append(flight)
        with open("db_flights.json", "w") as f:
            json.dump(flight_data, f, indent=4)

    def remove_flight_info(self):
        print("Remove flight info: ")
        fly = input("Enter Flight Place: ")
        for f in flight_data:
            if f["Place"] == fly:
                flight_data.remove(f)
                print(f"Flight {f} has been removed successfully!")
            with open("db_flights.json", "w") as f:
                json.dump(flight_data, f, indent=4)

    def display_flight_info(self):
        print(f"\nToday's flights: ")
        if not flight_data:
            return "No flights schedules found!"
        index = 0
        for flight in flight_data:
            index = index + 1
            print(f"{index}. {flight}")
            
