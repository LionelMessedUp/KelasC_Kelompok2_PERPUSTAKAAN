class Perpustakaan:    # Class untuk mengelola data perpustakaan
    def __init__(self):
        self.daftar = []
    
    def tambah(self, koleksi_baru):
        self.daftar.append(koleksi_baru)
        return True

    def ambil_semua(self):
        return self.daftar

    def hapus(self, kode):
        for i, koleksi in enumerate(self.daftar):
            if koleksi.kode == kode:
                self.daftar.pop(i)
                return True
        return False
