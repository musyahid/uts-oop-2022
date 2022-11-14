nama = input("masukkan nama : ")
nim = input("masukkan nim : ")

print("Nama : ", nama)
print("NIM : ", nim)

#Mencetak Menu
def menu():
    print ("Menu Pilihan")
    print
    print  ("1. Capucino")
    print  ("2. Teh")
    print  ("3. Keluar")

def capucino():
    print  ("Anda Memilih Capucino")
    harga = int(input("Masukkan Harga : "))
    total_harga = harga * 10 / 100
    print  ("Total Harga Setelah PPN adalah ",total_harga)
    print
    print  ("Mau cobalagi [Y/N]? ")
    back = input().upper()
    if back == "Y":
        menu()
    else:
        exit()
        
def teh():
    print  ("Anda Memilih Teh")
    harga = int(input("Masukkan Harga : "))
    total_harga = harga * 10 / 100
    print  ("Total Harga Setelah PPN adalah ",total_harga)
    print
    print  ("Mau cobalagi [Y/N]? ")
    back = input().upper()
    if back == "Y":
        menu()
    else:
        exit()

#Program MenghitungLuas
print  ("Selamat Datang di Program Menghitung Total Belanja")
print  ("-----------------------------------------------")
print
menu()
while 1:
#input
    pilih = int(input("Masukkan pilihan : "))

    if pilih == 1:
        capucino()
    elif pilih == 2:
        teh()
    elif pilih == 3:
        print("\n"*100)
        break
    else:
        print  ("Maaf pilihan yang anda masukkan tidak terdaftar")
        print  ("Cobalagi [Y/N] ? ")
        coba = input().upper()
    if coba == "Y":
        menu()
    else:
        print("\n"*100)
    break