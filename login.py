from auth import User, Main

def login(username, password):
    username = input("Enter username: ")
    password = input("Enter password: ")

    user = User(username="", role="", password="")
    for u in user.users:
        if u["username"] == username and u["password"] == password:
            print("Logged in successfully!")
            Main()
        else:
            print("Invalid credentials. Please provide the correct username and password to login!")

