class User:
    def __init__(self, username, role, password):
        self.username = username
        self.role = role
        self.password = password
        self.users = []

    def display_all_users(self):
        print("All Users: ")
        if self.users:
            index = 0
            for user in self.users:
                index = index + 1
                print(f"{index}. {user}")
        else:
            print("No users found. try to add one.")

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

    def update_user(self):
        pass

    def remove_user(self):
        print("Remove user")
        username = input("Enter username")
        for u in self.users:
            if u["username"] == username:
                self.users.remove(u)
                print(f"User {username} has been removed successfully!")

    def display_user_info(self):
        print("Search user here")
        username = input("Enter username")
        for u in self.users:
            if u["username"] == username:
                for user in u:
                    print(f"{user}")


class Main():
    users = User(username="", role="", password="")
    while True:
        print("Welcome back select what to do: ")
        choices = int(input("1, Display all users \n2, Create new user \n3, Remove user info \n4, Exit: \n>> "))
        if choices == 1:
            users.display_all_users()
        elif choices == 2:
            users.create_user()
        elif choices == 3:
            users.remove_user()
        elif choices == 4:
            print("Good bye!")
            break
        else:
            print("Invalid input, please try again!")


if __name__ == "__main__":
    Main()
        
