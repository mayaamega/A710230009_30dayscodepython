class Passenger:
    def __init__(self, name, passport_number):
        self.name = name
        self.passport_number = passport_number

    def __str__(self):
        return f"Name: {self.name}, Passport Number: {self.passport_number}"

class Flight:
    def __init__(self, flight_number, destination):
        self.flight_number = flight_number
        self.destination = destination
        self.passengers = []

    def add_passenger(self, passenger):
        self.passengers.append(passenger)

    def remove_passenger(self, passport_number):
        for passenger in self.passengers:
            if passenger.passport_number == passport_number:
                self.passengers.remove(passenger)
                return True
        return False

    def print_passenger_list(self):
        print(f"Passengers on flight {self.flight_number} to {self.destination}:")
        for passenger in self.passengers:
            print(passenger)

# Contoh penggunaan program:
if __name__ == "__main__":
    # Membuat objek penumpang
    passenger1 = Passenger("Nishimura Riki", "ABC123")
    passenger2 = Passenger("Huang Renjun", "DEF456")

    # Membuat objek penerbangan
    flight1 = Flight("KL123", "New York")

    # Menambahkan penumpang ke penerbangan
    flight1.add_passenger(passenger1)
    flight1.add_passenger(passenger2)

    # Menampilkan daftar penumpang
    flight1.print_passenger_list()

    # Menghapus penumpang
    flight1.remove_passenger("ABC123")

    # Menampilkan daftar penumpang setelah penghapusan
    flight1.print_passenger_list()
