class PerpustakaanManager:    # Class untuk mengelola data perpustakaan
    def __init__(self):
        self.daftar = []

    def tambah(self):
        from buku_majalah import Buku, Majalah
        from jurnal_dvd import Jurnal, DVDFilm

        print("Tipe koleksi: (1) Buku (2) Majalah (3) Jurnal (4) DVD")
        tipe = input("Pilih tipe koleksi: ").strip()

        if tipe == "1":
            kode = input("Kode: ")
            judul = input("Judul: ")
            tahun = input("Tahun: ")
            pengarang = input("Pengarang: ")
            penerbit = input("Penerbit: ")
            item = Buku(kode, judul, tahun, pengarang, penerbit)
        elif tipe == "2":
            kode = input("Kode: ")
            judul = input("Judul: ")
            tahun = input("Tahun: ")
            penerbit = input("Penerbit: ")
            edisi = input("Edisi: ")
            item = Majalah(kode, judul, tahun, penerbit, edisi)
        elif tipe == "3":
            kode = input("Kode: ")
            judul = input("Judul: ")
            tahun = input("Tahun: ")
            penerbit = input("Penerbit: ")
            bidang = input("Bidang Studi: ")
            impact = input("Impact Factor: ")
            item = Jurnal(kode, judul, tahun, penerbit, bidang, impact)
        elif tipe == "4":
            kode = input("Kode: ")
            judul = input("Judul: ")
            tahun = input("Tahun: ")
            bidang = input("Bidang Ilmu: ")
            durasi = input("Durasi: ")
            penerbit = input("Penerbit (kosong untuk 'Tidak Ada'): ") or "Tidak Ada"
            item = DVDFilm(kode, judul, tahun, bidang, durasi, penerbit)
        else:
            print("Pilihan tidak valid.")
            return False

        self.daftar.append(item)
        print("Koleksi berhasil ditambahkan.")
        return True

    def ambil_semua(self):
        return self.daftar

    def tampilkan(self):
        if not self.daftar:
            print("Tidak ada koleksi.")
            return

        for i, koleksi in enumerate(self.daftar, start=1):
            try:
                teks = koleksi.tampilkan(i)
            except TypeError:
                teks = koleksi.tampilkan()
            print(teks)
            print("-")

    def hapus(self):
        kode = input("Masukkan kode koleksi yang akan dihapus: ").strip()
        for i, koleksi in enumerate(self.daftar):
            if koleksi.kode == kode:
                self.daftar.pop(i)
                print("Koleksi berhasil dihapus.")
                return True
        print("Kode tidak ditemukan.")
        return False


# Backwards compatibility: older code may expect `Perpustakaan` class name
Perpustakaan = PerpustakaanManager
