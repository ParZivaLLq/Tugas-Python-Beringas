import os

def menu():
    os.system("CLS")
    print ("     SELAMAT DATANG DI PERPUSTAKAAN PYTHON BERINGAS")
    print ("Pilih daftar menu untuk mengakses program :\n")
    print ("[1] Daftar Buku")
    print ("[2] Cari Buku")
    print ("[3] Peminjaman Buku")
    print ("[4] Pengembalian Buku")
    print ("[5] Tambah buku")
    print ("[6] Keluar")
    
    p = int(input("\nMasukkan kode menu yang ingin diakses : "))
    pilihmenu(p)

def pilihmenu(p):
    if p == 1:
        daftar_buku()
    elif p == 2:
        caridata()
    elif p == 3:
        pinjam_buku()
    elif p == 4:
        kembalikan_buku()
    elif p == 5:
        tambahdata()
    elif p == 6:
        print(" terima kasih telah mengunjungi Perpustakaan Python Beringas ")
        exit()
    else:
        print("Kode menu tidak valid!")
        input("\nTekan [Enter] untuk kembali ke menu...")
        menu()

# Fungsi-fungsi yang dipanggil dalam pilihmenu
def daftar_buku():
    import os
    os.system("CLS")
    print("\nDaftar buku yang tersedia : ")
    bukadata = open ("daftarbuku.txt","r")
    isi = bukadata.readlines()
    isi.sort()
    if len(isi) == 0:
        print("\n[Data tidak tersedia]")
    else :
        i=1
        for data_buku in isi:
            pecah = data_buku.split(",")
            print("\n" + str(i) + ".",end=" ")
            print(pecah[0] + ", " + pecah[1] + ", " + pecah[2])
            i += 1
    print("\nTekan [Enter] untuk kembali ke menu...")
    bukadata.close()
    input()
    menu()

def caridata():
    import os
    os.system("CLS")
    print("\n        Cari Buku")
    cari = input("\nMasukkan judul buku yang ingin dicari : ")
    
    if os.path.exists("daftarbuku.txt"):
        bukadata = open("daftarbuku.txt","r")
        isi = bukadata.readlines()
        bukadata.close()
        isi.sort()
        
        found = False
        for data_buku in isi:
            judul, pengarang, tahun = data_buku.replace(" ", "").split(",")
            if judul.lower() == cari.lower():
                print("\nBuku ditemukan:")
                print(f"Judul: {judul}")
                print(f"Pengarang: {pengarang}")
                print(f"Tahun: {tahun}")
                found = True
                break
        
        if not found:
            print("\nBuku Tidak Ditemukan")
    else:
        print("\nFile daftarbuku.txt tidak ditemukan")
    
    input("\nTekan [Enter] untuk kembali ke menu...")
    menu()

def pinjam_buku():
    print("\nPeminjaman Buku")
    # Tambahkan kode untuk peminjaman buku
    input("\nTekan Enter untuk kembali ke menu...")
    menu()

def kembalikan_buku():
    print("\nPengembalian Buku")
    # Tambahkan kode untuk pengembalian buku
    input("\nTekan Enter untuk kembali ke menu...")
    menu()

def tambahdata():
    import os
    os.system("CLS")
    print("\n     Tambah Buku")
    print("\nMasukkan data buku baru")
    judul = input("Judul Buku : ")
    penulis = input("Penulis Buku : ")
    tahun = input("Tahun Terbit : ")
    
    bukadata = open("daftarbuku.txt", "a")
    if bukadata:
        bukadata.write(f"{judul},{penulis},{tahun}\n")
        bukadata.close()
        print("\n[Data Buku Berhasil Ditambahkan]")
    else:
        print("\n[Terjadi kesalahan saat menyimpan data]")
        
    print("\nApakah anda ingin menambahkan buku lagi? (ya/tidak)", end=" ")
    tambahdata = input(" : ").lower()
    if tambahdata in ["ya", "oke", "yoi"]:
        tambahdata()
    else:
        print("\nTekan [Enter] untuk kembali ke menu...")
        input()
        menu()

# Memulai program
if __name__ == "__main__":
    menu()