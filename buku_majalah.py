from koleksi import Koleksi


class Buku(Koleksi):
    def __init__(self, kode, judul, tahun, pengarang, penerbit):
        super().__init__(kode, tahun, judul, penerbit)
        self.pengarang = pengarang

    def tampilkan(self, no):
        return (
            f"{no}. Jenis : Buku\n"
            f"Kode : {self.kode}\n"
            f"Judul : {self.judul}\n"
            f"Tahun : {self.tahun}\n"
            f"Pengarang : {self.pengarang}\n"
            f"Penerbit : {self.penerbit}"
        )


class Majalah(Koleksi):
    def __init__(self, kode, judul, tahun, penerbit, edisi):
        super().__init__(kode, tahun, judul, penerbit)
        self.edisi = edisi

    def tampilkan(self, no):
        return (
            f"{no}. Jenis : Majalah\n"
            f"Kode : {self.kode}\n"
            f"Judul : {self.judul}\n"
            f"Tahun : {self.tahun}\n"
            f"Penerbit : {self.penerbit}\n"
            f"Edisi : {self.edisi}"
        )
