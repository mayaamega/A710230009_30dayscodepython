class Mobil:
    def move(self):
        print("Berjalan di jalan raya")

class Pesawat:
    def move(self):
        print("Terbang di udara")

class Kapal:
    def move(self):
        print("Berlayar di laut")

# create instances of each class and call the move() method
mobil = Mobil()
mobil.move()  # Output: Berjalan di jalan raya

pesawat = Pesawat()
pesawat.move()  # Output: Terbang di udara

kapal = Kapal()
kapal.move()  # Output: Berlayar di laut