from koleksi import Koleksi

class Buku(Koleksi):
    def __init__(self, kode, judul, tahun, pengarang, penerbit):
        super().__init__(kode, judul, tahun)
        self.pengarang = pengarang
        self.penerbit = penerbit

    def tampilkan(self):
        return (
            f"Jenis : Buku\n"
            f"Kode : {self.kode}\n"
            f"Judul : {self.judul}\n"
            f"Tahun : {self.tahun}\n"
            f"Pengarang : {self.pengarang}\n"
            f"Penerbit : {self.penerbit}"
        )


from koleksi import Koleksi

class Majalah(Koleksi):
    def __init__(self, kode, judul, tahun, penerbit, edisi):
        super().__init__(kode, judul, tahun)
        self.penerbit = penerbit
        self.edisi = edisi

    def tampilkan(self):
        return (
            f"Jenis : Majalah\n"
            f"Kode : {self.kode}\n"
            f"Judul : {self.judul}\n"
            f"Tahun : {self.tahun}\n"
            f"Penerbit : {self.penerbit}\n"
            f"Edisi : {self.edisi}"
        )
