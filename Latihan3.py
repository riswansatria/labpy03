saldo = 1_000_000

def tampilkan_menu():
    print("\n=== Menu ATM ===")
    print("1. Cek Saldo")
    print("2. Tarik Tunai")
    print("3. Keluar")

def cek_saldo():
    print(f"Saldo Anda saat ini: Rp{saldo}")

def tarik_tunai():
    global saldo
    jumlah = int(input("Masukkan jumlah yang ingin ditarik: Rp"))
    if jumlah > saldo:
        print("Saldo tidak mencukupi.")
    else:
        saldo -= jumlah
        print(f"Anda telah menarik: Rp{jumlah}")
        print(f"Saldo Anda saat ini: Rp{saldo}")

while True:
    tampilkan_menu()
    pilihan = input("Pilih menu (1/2/3): ")
    
    if pilihan == '1':
        cek_saldo()
    elif pilihan == '2':
        tarik_tunai()
    elif pilihan == '3':
        print("Terima kasih telah menggunakan ATM kami.")
        break
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")