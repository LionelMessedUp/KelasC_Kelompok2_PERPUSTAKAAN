from koleksi import perpustakaan

class buku(perpustakaan):
    def __init__(self, kode, judul, tahun, pengarang, penerbit):
        super().__init__(kode, tahun, judul, penerbit)
        self.pengarang = pengarang

    def tampilkan(self, no):
        print(f"""
Koleksi {no}:
Jenis        : Buku
Kode Koleksi : {self.kode}
Judul        : {self.judul}
Thn Terbit   : {self.tahun}
Pengarang    : {self.pengarang}
Penerbit     : {self.penerbit}
""")


class majalah(perpustakaan):
    def __init__(self, kode, judul, tahun, edisi, penerbit):
        super().__init__(kode, tahun, judul, penerbit)
        self.edisi = edisi

    def tampilkan(self, no):
        print(f"""
Koleksi {no}:
Jenis        : Majalah
Kode Koleksi : {self.kode}
Judul        : {self.judul}
Tahun Terbit : {self.tahun}
Penerbit     : {self.penerbit}
Edisi        : {self.edisi}
""")
