# Sistem Manajemen Perpustakaan

Aplikasi Python untuk mengelola koleksi perpustakaan yang mendukung berbagai jenis media: buku, majalah, jurnal, dan DVD film.

## Fitur Utama

- **Tambah Koleksi**: Menambahkan koleksi baru ke perpustakaan dengan berbagai tipe media
- **Tampilkan Semua Koleksi**: Menampilkan daftar lengkap semua koleksi yang tersimpan
- **Hapus Koleksi**: Menghapus koleksi dari perpustakaan berdasarkan kode
- **Keluar**: Menutup aplikasi dengan baik

## Jenis Koleksi yang Didukung

### 1. **Buku**
   - Kode
   - Judul
   - Tahun
   - Pengarang
   - Penerbit

### 2. **Majalah**
   - Kode
   - Judul
   - Tahun
   - Penerbit
   - Edisi

### 3. **Jurnal**
   - Kode
   - Judul
   - Tahun
   - Penerbit
   - Bidang Studi
   - Impact Factor

### 4. **DVD Film**
   - Kode
   - Judul
   - Tahun
   - Bidang Ilmu
   - Durasi
   - Penerbit

## Struktur File

```
KelasC_Kelompok2_PERPUSTAKAAN/
├── main.py              # File utama - menu aplikasi
├── perpustakaan.py      # Class PerpustakaanManager untuk mengelola data
├── koleksi.py           # Class abstrak Koleksi sebagai dasar semua tipe
├── buku_majalah.py      # Class Buku dan Majalah
├── jurnal_dvd.py        # Class Jurnal dan DVDFilm
└── README.md            # Dokumentasi ini
```

## Cara Menjalankan

### Persyaratan
- Python 3.6 atau lebih tinggi

### Langkah-langkah

1. Buka terminal/command prompt
2. Navigasi ke folder proyek:
   ```bash
   cd path/to/KelasC_Kelompok2_PERPUSTAKAAN
   ```
3. Jalankan aplikasi:
   ```bash
   python main.py
   ```

## Cara Penggunaan

1. **Pilih menu** dengan memasukkan angka (1-4)
2. **Tambah Koleksi (Menu 1)**:
   - Pilih tipe koleksi yang ingin ditambahkan
   - Masukkan data sesuai permintaan
   - Koleksi akan disimpan ke dalam daftar

3. **Tampilkan Semua Koleksi (Menu 2)**:
   - Menampilkan semua koleksi yang tersimpan dalam format tabel
   - Tekan Enter untuk kembali ke menu

4. **Hapus Koleksi (Menu 3)**:
   - Masukkan kode koleksi yang ingin dihapus
   - Koleksi akan dihapus dari daftar

5. **Keluar (Menu 4)**:
   - Menutup aplikasi

## Prinsip SOLID

Proyek ini menerapkan prinsip-prinsip SOLID:

- **S - Single Responsibility Principle**: Setiap class memiliki tanggung jawab tunggal
- **O - Open/Closed Principle**: Class terbuka untuk perluasan (bisa menambah tipe koleksi baru)
- **L - Liskov Substitution Principle**: Semua tipe koleksi dapat menggantikan class dasar `Koleksi`
- **I - Interface Segregation Principle**: Setiap class hanya mengimplementasikan method yang relevan
- **D - Dependency Inversion Principle**: Bergantung pada abstraksi, bukan implementasi konkret

## Kontributor

Kelas C - Kelompok 2

## Lisensi

Proyek ini dibuat untuk tujuan pembelajaran dan pengajaran.
