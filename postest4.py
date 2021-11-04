#List Baju
barang = {
    'crewneck' : 80000,
    'hoodie'   : 90000,
    'levis'    : 75000,
    'kemeja'   : 120000
}

#Fungsi-fuungsi
def list_menu():
    barang
    for key, value in barang.items():
        print(key, ':', value)

def tambah():
    input_baru = input('masukan key: ')
    in_baru = int(input('Masukan Value: '))
    barang[input_baru] = in_baru

def update():
    input_baru = input('Update key: ')
    in_baru = int(input('Update Value: '))
    barang[input_baru] = in_baru

def delete():
    del barang [input('apa yang mau dihapus: ')]

#fungsi program utama(CRUD)
def main_menu():
    while True:
        print('menu')
        print('1. List menu\n2. Tambahkan\n3. Update\n4. Hapus\n 5.exit')
        choice = input('Masukan pilihan: ')
        if choice == '1':
            list_menu()
            print('\nTekan [Enter] untuk kembali')
            input()
        elif choice == '2':
            tambah()
            print('\nTekan [Enter] untuk kembali')
            input()
        elif choice == '3':
            update()
            print('\nTekan [Enter] untuk kembali')
            input()
        elif choice == '4':
            delete()
            print('\nTekan [Enter] untuk kembali')
            input()
        elif choice == '5':
            print('Anda telah keluar')
            break

def kasir():
    barang
    for key, value in barang.items ():
        print (key,":", value)
    pilih = barang [input("masukkan barang yang anda inginkan")]
    jumlah= int(input("Masukan jumlah baju yang dibeli: "))
    Total=pilih * jumlah 
    haripembelian =input('Masukan hari pembelian: ')
    if haripembelian == 'senin':
        Total=int(Total-0.1*Total)
        print('-Diskon 10 %-')
    elif haripembelian == 'rabu':
        Total=int(Total-0.25*Total)
        print('-Diskon 25 %-')
    else:
        print('Maaf,tidak dapat diskon')
    
    print("Total Harga = ", "Rp.",Total)
    Bayar=int(input("Jumlah Nominal Uang = Rp. ", ))
    Kembalian= (Bayar-Total)
    print("Uang Kembalian = ", "Rp.",Kembalian)
    pilihan=input("Apakah anda ingin order kembali Ya/Tidak= ")
    pilihan="tidak"
    print('Terima Kasih Telah Berbelanja di Lapak genjie')
while True : 
    print('selamat datang')
    print('1. database')
    print('2. kasir')
    x = input('masukkan pilihan')
    if x == "1" :
        main_menu ()
    elif x == "2" :
        kasir()   