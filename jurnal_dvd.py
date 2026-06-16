from koleksi import Koleksi

class Jurnal(Koleksi):
    def __init__(self, kode, judul, tahun, penerbit, bidang_studi, impact_factor):
        super().__init__(kode, tahun, judul, penerbit)
        self.bidang_studi = bidang_studi
        self.impact_factor = impact_factor
    def tampilkan(self):
        return (
            f"Jenis : Jurnal\n"
            f"Kode : {self.kode}\n"
            f"Judul : {self.judul}\n"
            f"Tahun : {self.tahun}\n"
            f"Penerbit : {self.penerbit}\n"
            f"Impact Factor : {self.impact_factor}\n"
            f"Bidang Studi : {self.bidang_studi}"
        )
        
class DVDFilm(Koleksi):
    def __init__(self, kode, judul, tahun, bidang_ilmu, durasi, penerbit="Tidak Ada"):
        super().__init__(kode, tahun, judul, penerbit)
        self.bidang_ilmu = bidang_ilmu
        self.durasi = durasi
    def tampilkan(self):
        return (
            f"Jenis : DVD Film Dokumenter\n"
            f"Kode : {self.kode}\n"
            f"Judul : {self.judul}\n"
            f"Bidang Ilmu : {self.bidang_ilmu}\n"
            f"Durasi : {self.durasi}\n"
            f"Tahun : {self.tahun}"
        )