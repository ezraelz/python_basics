from model import User, Flight


def user_management():
    users = User(username="", role="", password="")
    while True:
        print("Welcome back select what to do: ")
        choices = int(input("1. Display all users \n2. Create new user \n3. Update user info \n4. Remove user info \n5. Display user info \n6. Exit: \n>> "))
        if choices == 1:
            users.display_all_users()
        elif choices == 2:
            users.create_user()
        elif choices == 3:
            users.update_user()
        elif choices == 4:
            users.remove_user()
        elif choices == 5:
            users.display_user_info()
        elif choices == 6:
            print("Good bye!")
            break
        else:
            print("Invalid input, please try again!")


def flight_management():
    flight = Flight(place="", day="", time="", amount="")
    while True:
        print("Welcome select what to do: ")
        choices = int(input("1, Display today's flights \n2, Create new flight \n3, Remove flight info \n4, Exit: \n>> "))
        if choices == 1:
            flight.display_flight_info()
        elif choices == 2:
            flight.create_flights()
        elif choices == 3:
            flight.remove_flight_info()
        elif choices == 4:
            print("Good bye!")
            break
        else:
            print("Invalid input, please try again!")


