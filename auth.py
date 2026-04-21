from model import User
from management import user_management, flight_management

user = User(username='', role='', password='')
stored_user = user.users

def register():
    user.create_user()

def login(username, password):
    username = input("Enter username: ")
    password = input("Enter password: ")

    if not stored_user:
        print("\n404 user found!")

    for u in stored_user:
        if u["username"] == username and u["password"] == password:
            print("\nLogged in successfully!")
            print("Please choose what to do next")
            options = int(input("1. User management 2. Flight Management 3. Exit \n>> "))
            if options == 1:
                user_management()
            elif options == 2:
                flight_management()
            elif options == 3:
                print('Good bye. Have a good day! \n')
                break
            else:
                print("Invalid option. please try again")
        else:
            print("Invalid credentials. Please provide the correct username and password to login!")

def logout():
    pass