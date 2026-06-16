from abc import ABC, abstractmethod

class Koleksi(ABC):
    """Class dasar/abstrak untuk semua koleksi perpustakaan"""
    def __init__(self, kode_koleksi, tahun_terbit, judul, penerbit):
        self.kode_koleksi = kode_koleksi
        self.tahun_terbit = tahun_terbit
        self.judul = judul
        self.penerbit = penerbit
 
    def _cetak_data_umun(self):
        print(f" kode koleksi : {self.kode_koleksi}")
        print(f" tahun terbit : {self.tahun_terbit}")
        print(f" judul        : {self.judul}")
        print(f" penerbit     : {self.penerbit}")
    
    @abstractmethod
    def tampil_info(self):
        pass
