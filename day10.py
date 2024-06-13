class Tiket:
    def __init__(self, jumlah_tiket):
        self.jumlah_tiket = jumlah_tiket
        self.harga_per_tiket = 0

    def hitung_total_harga(self):
        total_harga = self.jumlah_tiket * self.harga_per_tiket
        return total_harga

class TiketBiasa(Tiket):
    def __init__(self, jumlah_tiket):
        super().__init__(jumlah_tiket)
        self.harga_per_tiket = 50000

class TiketVIP(Tiket):
    def __init__(self, jumlah_tiket):
        super().__init__(jumlah_tiket)
        self.harga_per_tiket = 75000

class TiketGold(Tiket):
    def __init__(self, jumlah_tiket):
        super().__init__(jumlah_tiket)
        self.harga_per_tiket = 100000

def main():
    jenis_tiket = input("Masukkan jenis tiket (biasa/vip/gold): ").lower()
    jumlah_tiket = int(input("Masukkan jumlah tiket: "))

    if jenis_tiket == "biasa":
        tiket = TiketBiasa(jumlah_tiket)
    elif jenis_tiket == "vip":
        tiket = TiketVIP(jumlah_tiket)
    elif jenis_tiket == "gold":
        tiket = TiketGold(jumlah_tiket)
    else:
        print("Jenis tiket tidak valid.")
        return

    total_harga = tiket.hitung_total_harga()
    print(f"Total Harga Tiket: Rp {total_harga}")

if __name__ == "__main__":
    main()