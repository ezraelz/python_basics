from auth import login, logout, register

def main():
    print("\nWelcome back ==^== ")
    while True:
        options = int(input("\n1. Login 2. Register 3. Logout\n>> "))
        if options == 1:
            login(username="", password="")
        elif options == 2:
            register()
        elif options == 3:
            print("Good bye! Dont forget to comeback! \n")
            break
        else:
            print("Invalid choice. Please try again!")


if __name__ == "__main__":
    main()