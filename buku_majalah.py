class Buku(Koleksi):
    def __init__(self, kode, judul, tahun,
                 pengarang, penerbit):
        super().__init__(kode, judul, tahun)
        self.pengarang = pengarang
        self.penerbit = penerbit

    def tampilkan(self):
        print("\n=== DATA BUKU ===")
        print("Kode       :", self.kode)
        print("Judul      :", self.judul)
        print("Tahun      :", self.tahun)
        print("Pengarang  :", self.pengarang)
        print("Penerbit   :", self.penerbit)


class Majalah(Koleksi):
    def __init__(self, kode, judul, tahun,
                 penerbit, edisi):
        super().__init__(kode, judul, tahun)
        self.penerbit = penerbit
        self.edisi = edisi

    def tampilkan(self):
        print("\n=== DATA MAJALAH ===")
        print("Kode       :", self.kode)
        print("Judul      :", self.judul)
        print("Tahun      :", self.tahun)
        print("Penerbit   :", self.penerbit)
        print("Edisi      :", self.edisi)
