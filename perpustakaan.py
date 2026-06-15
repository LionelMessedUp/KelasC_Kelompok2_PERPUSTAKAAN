from buku_majalah import buku, majalah
from jurnal_dvd import jurnal, DVD

class PerpustakaanManager:
    """Class untuk mengelola perpustakaan"""
    def __init__(self):
        self.daftar = []
    
    def tambah(self):
        print("pilih jenis koleksi yang ingin ditambahkan:\n1. Buku\n2. Majalah\n3. Jurnal\n4. DVD")
        pilihan = input("pilih menu: ")
        if pilihan == "1":
            kode = input("masukkan kode koleksi: ")
            judul = input("masukkan judul buku: ")
            tahun = int(input("masukkan tahun terbit: "))
            pengarang = input("masukkan nama pengarang: ")
            penerbit = input("masukkan nama penerbit: ")
            koleksi_buku = buku(kode, judul, tahun, pengarang, penerbit)
            self.daftar.append(koleksi_buku)
        elif pilihan == "2":
            kode = input("masukkan kode koleksi: ")
            judul = input("masukkan judul majalah: ")
            tahun = int(input("masukkan tahun terbit: "))
            edisi = input("masukkan edisi majalah: ")
            penerbit = input("masukkan nama penerbit: ")
            koleksi_majalah = majalah(kode, judul, tahun, edisi, penerbit)
            self.daftar.append(koleksi_majalah)
        elif pilihan == "3":
            kode = input("masukkan kode koleksi: ")
            judul = input("masukkan judul jurnal: ")
            tahun = int(input("masukkan tahun terbit: "))
            tanggal = input("masukkan tanggal terbit: ")
            impact_factor = float(input("masukkan impact factor jurnal: "))
            penerbit = input("masukkan nama penerbit: ")
            bidang_studi = input("masukkan bidang studi jurnal: ")
            koleksi_jurnal = jurnal(kode, judul, tahun, tanggal, impact_factor, penerbit, bidang_studi)
            self.daftar.append(koleksi_jurnal)
        elif pilihan == "4":
            kode = input("masukkan kode koleksi: ")
            judul = input("masukkan judul DVD: ")
            tahun = int(input("masukkan tahun terbit: "))
            sutradara = input("masukkan nama sutradara: ")
            penerbit = input("masukkan nama penerbit: ")
            koleksi_dvd = DVD(kode, judul, tahun, sutradara, penerbit)
            self.daftar.append(koleksi_dvd)
        else:
            print("pilihan tidak valid")
    
    def tampilkan(self):
        if len(self.daftar) == 0:
            print("belum ada koleksi yang ditambahkan")
        else:
            for i, koleksi in enumerate(self.daftar, start=1):
                koleksi.tampilkan(i)
    
    def hapus(self):
        kode = input("masukkan kode koleksi yang ingin dihapus: ")
        for i, koleksi in enumerate(self.daftar):
            if koleksi.kode == kode:
                self.daftar.pop(i)
                print("Koleksi berhasil dihapus")
                return
        print("Koleksi tidak ditemukan")
