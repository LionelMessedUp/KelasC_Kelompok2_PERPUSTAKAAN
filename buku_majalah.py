from koleksi import perpustakaan

class buku(perpustakaan):
    def __init__(self, kode, judul, tahun, pengarang, penerbit):
        super().__init__(kode, tahun, judul, penerbit)
        self.pengarang = pengarang
    
    def tampilkan(self, no):
        print(f"Koleksi nomor{no}: \n Jenis Koleksi: Buku \n Kode Koleksi: {self.kode} \n Judul Buku: {self.judul} \n Tahun terbit: {self.tahun} \n Pengarang: {self.pengarang} \n Penerbit: {self.penerbit} ")

class majalah(perpustakaan):
    def __init__(self, kode, judul, tahun, edisi, penerbit):
        super().__init__(kode, tahun, judul, penerbit)
        self.edisi = edisi
    
    def tampilkan(self, no):
        print(f"Koleksi nomor{no}: \n Jenis Koleksi: Majalah \n Kode Koleksi: {self.kode} \n Judul Majalah: {self.judul} \n Tahun terbit: {self.tahun} \n Edisi: {self.edisi} ")
