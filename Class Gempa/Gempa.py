class gempa:
    #konstruktor inisialisasi atribut
    def __init__(self, lokasi, skala):
        self.lokasi = lokasi 
        self.skala = skala

    #method penentu skala gempa
    def dampak(self):
        #logika/statement
        if self.skala < 2 :
            print("Gempa tidak berasa")
        elif 2 <= self.skala <= 4:
            print("Gempa berdampak bangunan retak")
        elif 4 <= self.skala <=6:
            print("Gempa berdampak bangunan roboh")
        elif 6 > self.skala:
            print("Gempa berdampak bangunan roboh dan berpotensi tsunami")

        #menampilkan lokasi dan skala gempa
        print(f"Lokasi Gempa: {self.lokasi}")
        print(f"Skala Gempa: {self.skala}")