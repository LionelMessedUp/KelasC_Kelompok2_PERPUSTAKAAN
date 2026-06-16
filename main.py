from perpustakaan import PerpustakaanManager
perpus = PerpustakaanManager()

while True:
    print("===== MENU PERPUSTAKAAN =====")
    print("1. Tambah Koleksi")
    print("2. Tampilkan Semua Koleksi")
    print("3. Hapus Koleksi")
    print("4. Keluar")

    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        perpus.tambah() 
        input("Tekan Enter untuk kembali ke menu...")
    elif pilihan == "2":
        perpus.tampilkan()
        input("Tekan Enter untuk kembali ke menu...")  
    elif pilihan == "3":
        perpus.hapus()
        input("Tekan Enter untuk kembali ke menu...")
    elif pilihan == "4":
        print("Program selesai. Terima kasih!")
        break   
    else:
        print("Pilihan tidak valid. Silakan pilih menu yang tersedia.")
