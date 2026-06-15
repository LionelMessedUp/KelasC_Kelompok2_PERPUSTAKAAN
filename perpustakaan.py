class PerpustakaanManager:             # class untuk mengelola data perpustakaan
    def __init__(self):
        self.daftar = []                # menampung semua objek koleksi
    
    def tambah(self, koleksi_baru):
        self.daftar.append(koleksi_baru)          # menerima objek koleksi yg sudah jadi dari main.py, lalu menyimpannya
        return True

    def ambil_semua(self):                  # mengembalikan isi list daftar koleksi
        return self.daftar

    def hapus(self, kode):                  # mencari objek berdasarkan kode, menghapusnya, dan mengembalikan status sukses
        for i, koleksi in enumerate(self.daftar):
            if koleksi.kode == kode:
                self.daftar.pop(i)
                return True            # jika berhasil dihapus
        return False             #jika kode tidak ditemukan
