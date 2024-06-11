#===================================================================================================================
from os import system
nama = []
nim = []
prodi = []
hadir = []
tugas = []
uts = []
uas = []
akhir = []

def judul():
    print ("==========================")
    print ("# PROGRAM DATA MAHASISWA #")
    print ("==========================")
    
def menu():
    judul()
    print("==========================")
    print("# 1. INPUT DATA          #")
    print("# 2. MENAMPILKAN DATA    #")
    print("# 3. NILAI RATA-RATA     #")
    print("# 4. NILAI TERTINGGI     #")
    print("# 5. NILAI TERENDAH      #")
    print("==========================")

    pilihan = int(input("Pilih menu: "))
    if pilihan == 1:
        input_mhs()
    elif pilihan == 2:
        tampilkan_data()
        menu()
    elif pilihan == 3:
        nilai_rata_rata()
        menu()
    elif pilihan == 4:
        nilai_tertinggi()
        menu()
    elif pilihan == 5:
        nilai_terendah()
        menu()
   

def input_mhs():
    i_nama = input("NAMA : ")
    nama.append(i_nama)
    
    i_nim = input("NIM : ")
    nim.append (i_nim)
    
    i_prodi = input("PRODI : ")
    prodi.append(i_prodi)
    
    i_hadir = float(input ("JUMLAH HADIR : "))
    t_hadir = ((i_hadir/16)*20/100)*100
    hadir.append(t_hadir)
    
    i_tugas = float(input("NILAI TUGAS : "))
    t_tugas = i_tugas*(25/100)
    tugas.append(t_tugas)
    
    i_uts = float(input("NILAI UTS : "))
    t_uts = i_uts*(25/100)
    uts.append(t_uts)
    
    i_uas = float(input ("NILAI UAS: "))
    t_uas = i_uas*(30/100)
    uas.append(t_uas)
    
    total_nilai = t_hadir + t_tugas + t_uts + t_uas
    akhir.append(total_nilai)
    print ("DATA TERSIMPAN")
    menu()
    
def tampilkan_data():
    judul()
    print("Data Mahasiswa:")
    for i in range(len(nama)):
        print("Nama   :", nama[i])
        print("NIM    :", nim[i])
        print("Prodi  :", prodi[i])
        print("Hadir  :", hadir[i])
        print("Tugas  :", tugas[i])
        print("UTS    :", uts[i])
        print("UAS    :", uas[i])
        print("Akhir  :", akhir[i])
        print("==========================")

def nilai_rata_rata():
    total_nilai = sum(akhir)
    rata_rata = total_nilai / len(akhir)
    print("Nilai Rata-rata: {:.2f}".format(rata_rata))

def nilai_tertinggi():
    max_nilai = max(akhir)
    index_max = akhir.index(max_nilai)
    print("Nilai Tertinggi:")
    print("Nama   :", nama[index_max])
    print("NIM    :", nim[index_max])
    print("Prodi  :", prodi[index_max])
    print("Hadir  :", hadir[index_max])
    print("Tugas  :", tugas[index_max])
    print("UTS    :", uts[index_max])
    print("UAS    :", uas[index_max])
    print("Akhir  :", akhir[index_max])
    
def nilai_terendah():
    min_nilai = min(akhir)
    index_min = akhir.index(min_nilai)
    print("Nilai Terendah:")
    print("Nama   :", nama[index_min])
    print("NIM    :", nim[index_min])
    print("Prodi  :", prodi[index_min])
    print("Hadir  :", hadir[index_min])
    print("Tugas  :", tugas[index_min])
    print("UTS    :", uts[index_min])
    print("UAS    :", uas[index_min])
    print("Akhir  :", akhir[index_min])

#=====================================================================================




inventaris = []


def tambah_barang(nama, kode, jumlah):
    barang = {
        'nama': nama,
        'kode': kode,
        'jumlah': jumlah
    }
    inventaris.append(barang)
    print(f"Barang '{nama}' berhasil ditambahkan.")


def tampilkan_semua_barang():
    if not inventaris:
        print("Tidak ada barang dalam inventaris.")
    else:
        for barang in inventaris:
            print(f"Nama: {barang['nama']}, Kode: {barang['kode']}, Jumlah: {barang['jumlah']}")


def cari_barang_berdasarkan_kode(kode):
    for barang in inventaris:
        if barang['kode'] == kode:
            print(f"Barang ditemukan: Nama: {barang['nama']}, Kode: {barang['kode']}, Jumlah: {barang['jumlah']}")
            return
    print(f"Barang dengan kode '{kode}' tidak ditemukan.")


def hapus_barang_berdasarkan_kode(kode):
    for barang in inventaris:
        if barang['kode'] == kode:
            inventaris.remove(barang)
            print(f"Barang dengan kode '{kode}' berhasil dihapus.")
            return
    print(f"Barang dengan kode '{kode}' tidak ditemukan.")


def main():
    while True: 
        print("=======================================")
        print("#      PROGRAM INVENTARIS BARANG      #")
        print("=======================================")
        print("# 1. TAMBAH BARANG                    #")
        print("# 2. TAMPILKAN SEMUA BARANG           #")
        print("# 3. CARI BARANG BERDSARKAN KODE      #")
        print("# 4. HAPUS BARANG BERDSARKAN KODE     #")
        print("# 5. KELUAR                           #")
        print("=======================================")

        pilihan = input("pilih menu : ")

        if pilihan == '1':
            nama = input("MASUKAN NAM BARANG : ")
            kode = input("MASUKAN KODE BARANG : ")
            jumlah = int(input("MASUKAN JUMLAH BARANG : "))
            tambah_barang(nama, kode, jumlah)
        elif pilihan == '2':
            tampilkan_semua_barang()
        elif pilihan == '3':
            kode = input("MMASUKAN KODE BARANG YANG DICARI : ")
            cari_barang_berdasarkan_kode(kode)
        elif pilihan == '4':
            kode = input("MASUKAN KODE BARANG YANG MAU DI HAPUS: ")
            hapus_barang_berdasarkan_kode(kode)
        elif pilihan == '5':
            print("TERIMA KASIH")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")


#==========================================================================================

keuangan = []

def tambah_transaksi(jenis, jumlah, keterangan):
    transaksi = {
        'jenis': jenis,
        'jumlah': jumlah,
        'keterangan': keterangan
    }
    keuangan.append(transaksi)
    print(f"TRANSAKSI '{keterangan.upper()}' BERHASIL DITAMBAHKAN.")


def tampilkan_semua_transaksi():
    if not keuangan:
        print("TIDAK ADA TRANSAKSI DALAM KEUANGAN.")
    else:
        for transaksi in keuangan:
            print(f"JENIS: {transaksi['jenis'].upper()}, JUMLAH: {transaksi['jumlah']}, KETERANGAN: {transaksi['keterangan'].upper()}")


def total_pemasukan():
    total_masuk = sum(transaksi['jumlah'] for transaksi in keuangan if transaksi['jenis'] == 'pemasukan')
    print(f"TOTAL PEMASUKAN: {total_masuk}")
    return total_masuk


def total_pengeluaran():
    total_keluar = sum(transaksi['jumlah'] for transaksi in keuangan if transaksi['jenis'] == 'pengeluaran')
    print(f"TOTAL PENGELUARAN: {total_keluar}")
    return total_keluar


def saldo_akhir():
    saldo = total_pemasukan() - total_pengeluaran()
    print(f"SALDO AKHIR: {saldo}")
    return saldo


def utama():
    while True:
        print("================================")
        print("#            E-MONEY           #")
        print("================================")
        print("# 1. TAMBAH TRANSAKSI          #")
        print("# 2. TAMPILKAN SEMUA TRANSAKSI #")
        print("# 3. HITUNG TOTAL PEMASUKAN    #")
        print("# 4. HITUNG TOTAL PENGELUARAN  #")
        print("# 5. HITUNG SALDO AKHIR        #")
        print("# 6. KELUAR                    #")
        print("================================")

        pilihan = input("PILIH MENU (1-6): ")

        if pilihan == '1':
            jenis = input("MASUKKAN JENIS TRANSAKSI (PEMASUKAN/PENGELUARAN): ")
            jumlah = float(input("MASUKKAN JUMLAH TRANSAKSI: "))
            keterangan = input("MASUKKAN KETERANGAN TRANSAKSI: ")
            tambah_transaksi(jenis, jumlah, keterangan)
        elif pilihan == '2':
            tampilkan_semua_transaksi()
        elif pilihan == '3':
            total_pemasukan()
        elif pilihan == '4':
            total_pengeluaran()
        elif pilihan == '5':
            saldo_akhir()
        elif pilihan == '6':
            print("TERIMA KASIH TELAH MENGGUNAKAN PROGRAM INI.")
            break
        else:
            print("PILIHAN TIDAK VALID. SILAKAN COBA LAGI.")



#===============================================================================================

print ("=============================================#")
print ("# 1. PROGRAM DATA MAHASISWA                  #")
print ("# 2. PROGRAM INVENTARIS BARANG               #")
print ("# 3. PROGRAM PENGELOLAAN KEUANGAN PRIBADI    #")
print ("#=============================================")

opsi = int(input("MASUKAN PILIHAN : "))

if opsi == 1:
    menu()
elif opsi == 2:
    main()
elif opsi == 3:
    utama()
else:
    print ("PILIHAN TIDAK VALID")