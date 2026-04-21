# User object
# Blue print for user object
class User:
    # Constructor for user object
    def __init__(self, username, role, password):
        # All necessary fields to create the constructor 
        self.username = username
        self.role = role
        self.password = password
        self.users = []                  # An empty list to stor all users

    # A method to display all available users in the list
    # Added indexing to make the list more readable
    # The conditional statement checks if users exist or not inside the users list 
    def display_all_users(self):
        print("All Users: ")
        if self.users:
            index = 0
            for user in self.users:
                index = index + 1
                print(f"{index}. {user}")
        else:
            print("No users found. try to add one.")

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

        if role == 'admin':
            self.display_all_users()

    # A method to update a user information
    def update_user(self):
        print("Select user to update")
        user = input("Enter username here: ")
        # Loop through the list to find the user to be updated
        for u in self.users:
            #It checks conditionally if the user exists in the list or not
            if u["username"] == user:
                username = input("Update username: ")
                role = input("Update user role: ")
                password = input("Update user password: ")
                # if the user found then update the fields with necessary values
                u["username"] = username
                u["role"] = role
                u["password"] = password

                print(f"User {user} updated successfully!")
            else:
                # Fall back if the user not found
                print("User not found. Please try again!")

    # This method removes a user from the list if you provide a value for username key
    def remove_user(self):
        print("Remove user")
        username = input("Enter username: ")
        # it looks for the username provided
        for u in self.users:
            # if found it will be removed
            if u["username"] == username:
                self.users.remove(u)
                print(f"User {username} has been removed successfully!")
            # if not found, fallback to error message
            else:
                print("User not found. Please try again!")

    # Based on the given username value this method tries to display  a user info
    # It is a simple search method
    def display_user_info(self):
        print("Search user here")
        username = input("Enter username: ")
        for u in self.users:
            if u["username"] == username:
                print(f"{u}")
            else:
                print("User not found. Please try again!")


class Flight():
    def __init__(self, place, day, time, amount):
        self.place = place
        self.day = day
        self.time = time
        self.amount = amount
        self.flights = []

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
        self.flights.append(flight)

    def remove_flight_info(self):
        print("Remove flight info: ")
        fly = input("Enter Flight Place: ")
        for f in self.flights:
            if f["Place"] == fly:
                self.flights.remove(f)
                print("remove successfully!")

    def display_flight_info(self):
        print(f"\nToday's flights: ")
        if not self.flights:
            return "No flights schedules found!"
        index = 0
        for flight in self.flights:
            index = index + 1
            print(f"{index}. {flight}")
            
