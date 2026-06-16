from abc import ABC, abstractmethod

class Koleksi(ABC):
    """Class dasar/abstrak untuk semua koleksi perpustakaan"""
    def __init__(self, kode, tahun, judul, penerbit):
        self.kode = kode
        self.tahun = tahun
        self.judul = judul
        self.penerbit = penerbit
     
    @abstractmethod
    def tampilkan(self):
        pass
