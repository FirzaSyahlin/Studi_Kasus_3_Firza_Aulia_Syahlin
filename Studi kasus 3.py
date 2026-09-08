daftar_buku = ("Sejarah", "Matematika", "IPA", "IPS", "Pendidikan Pancasila")
pinjaman = []

print("DAFTAR BUKU PERPUSTAKAAN FT")
for buku in daftar_buku:
    print(buku)

while True:
    pilihan = input("Masukkan judul buku yang ingin dipinjam: ")

    if pilihan.lower() == "selesai":
        break

    if pilihan in daftar_buku:
        pinjaman.append(pilihan)
        print("Buku berhasil dipinjam")
    else:
        print("Buku tidak tersedia")

print("DAFTAR PINJAMAN")
for buku in pinjaman:
    print(buku)

if pinjaman:
    hapus = input("Masukkan judul buku yang ingin dihapus: ")

    if hapus in pinjaman:
        pinjaman.remove(hapus)
        print("Buku berhasil dihapus")

print("BUKU YANG DIPINJAM")
for buku in pinjaman:
    print(buku)