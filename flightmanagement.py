class FlightManagement():
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
                print("remove successfull!")

    def display_flight_info(self):
        print(f"Today's flights: ")
        index = 0
        for flight in self.flights:
            index = index + 1
            print(f"{index}. {flight}")
            


class Main():
    flight = FlightManagement(place="", day="", time="", amount="")
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


if __name__ == "__main__":
    Main()
