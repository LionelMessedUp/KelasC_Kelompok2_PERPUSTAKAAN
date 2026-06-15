from koleksi import perpustakaan, abstractmethod

class Jurnal(Koleksi):
    def __init__(self, kode, judul, tahun, penerbit, bidang_studi, impact_factor):
        super().__init__(kode, judul, tahun, penerbit)
        self.bidang_studi = bidang_studi
        self.impact_factor = impact_factor
        
    def tampilkan_info(self):
        print(f"Jenis        : Jurnal")
        print(f"Kode Koleksi : {self.kode}")
        print(f"Judul        : {self.judul}")
        print(f"Thn Terbit   : {self.tahun}")
        print(f"Penerbit     : {self.penerbit}")
        print(f"Impact Factor: {self.impact_factor}")
        print(f"Bidang Studi : {self.bidang_studi}")
        
class DVDFilm(Koleksi):
    def __init__(self, kode, judul, tahun, bidang_ilmu, durasi, penerbit="Tidak Ada"):
        super().__init__(kode, judul, tahun, penerbit)
        self.bidang_ilmu = bidang_ilmu
        self.durasi = durasi

    def tampilkan_info(self):
        print(f"Jenis        : DVD Film Dokumenter")
        print(f"Kode Koleksi : {self.kode}")
        print(f"Judul        : {self.judul}")
        print(f"Bidang Ilmu  : {self.bidang_ilmu}")
        print(f"Durasi       : {self.durasi}")
        print(f"Tahun        : {self.tahun}")