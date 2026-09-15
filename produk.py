produk = {
    "nama": "Laptop ASUS",
    "harga": 8500000,
    "stok": 12
}

while True:
    print("MENU PENGELOLAAN DATA PRODUK")
    print("1 Tampilkan Data Produk")
    print("2 Tambah Data Kategori")
    print("3 Ubah Data Harga")
    print("4 Hapus Data Kategori")
    print("5 Keluar")
    pilihan = input("Pilih menu (1-5): ")
    if pilihan == "1":
        print("Data Produk:")
        print(produk)
        print("Nama:", produk["nama"])
        print("Harga:", produk["harga"])
        print("Stok:", produk["stok"])
        if "kategori" in produk:
            print("Kategori:", produk["kategori"])
    elif pilihan == "2":
        kategori = input("Masukkan nama kategori: ")
        produk["kategori"] = kategori
        print("Setelah Add Kategori:")
        print(produk)
    elif pilihan == "3":
        harga_baru = int(input("Masukkan harga baru: "))
        produk.update({"harga": harga_baru})
        print("Setelah Update Harga:")
        print(produk)
    elif pilihan == "4":
        if "kategori" in produk:
            produk.pop("kategori")
            print("Setelah Delete Kategori:")
            print(produk)
        else:
            print("Kategori tidak ditemukan")
    elif pilihan == "5":
        print("Terima kasih, program selesai")
        break
    else:
        print("Pilihan menu tidak valid")
