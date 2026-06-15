from koleksi import perpustakaan

class jurnal(perpustakaan):
    def __init__(self, kode, judul, tahun, tanggal, impact_factor, penerbit, bidang_studi):
        super().__init__(kode, tahun, judul, penerbit)
        self.tanggal = tanggal
        self.impact_factor = impact_factor
        self.bidang_studi = bidang_studi

    def tampilkan(self, no):
        print(f"Koleksi nomor{no}: \n Jenis Koleksi: Jurnal \n Kode Koleksi: {self.kode} \n Judul Jurnal: {self.judul} \n Tahun terbit: {self.tahun} \n Tanggal Terbit: {self.tanggal} \n Impact Factor: {self.impact_factor} \n Bidang Studi: {self.bidang_studi} ")

class DVD(perpustakaan):
    def __init__(self, kode, judul, tahun, sutradara, penerbit):
        super().__init__(kode, tahun, judul, penerbit)
        self.sutradara = sutradara
    
    def tampilkan(self, no):
        print(f"Koleksi nomor{no}: \n Jenis Koleksi: DVD \n Kode Koleksi: {self.kode} \n Judul DVD: {self.judul} \n Tahun terbit: {self.tahun} \n Sutradara: {self.sutradara} \n Penerbit: {self.penerbit} ")
