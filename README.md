# labpy03
Nama : Riswan Satria Juniarto <p>
Nim : 312410 <p>
Kelas : TI.24.A.5 <p>
Mata kuliah : Bahasa pemrpgraman <p>
## Latihan1
Alur Algoritma Latihan1 :
 1. Mulai Program :
    - Import modul random.
    - Minta input dari pengguna untuk nilai n (jumlah bilangan acak yang ingin ditampilkan).
 2. Inisialisasi Variabel :
    - Inisialisasi variabel count dengan nilai 0 untuk menghitung jumlah bilangan acak yang sudah dihasilkan.
 3. Looping:
    - Gunakan loop while untuk terus menghasilkan bilangan acak hingga jumlah yang diinginkan tercapai (count < n).
 4. Menghasilkan Bilangan Acak:
    - Di dalam loop, gunakan random.random() untuk menghasilkan bilangan acak antara 0 dan 1.
 5. Memeriksa Bilangan Acak:
    - Periksa apakah bilangan acak yang dihasilkan kurang dari 0.5.
      > Jika ya, tambahkan nilai count dengan 1 dan cetak bilangan tersebut dengan format “Data Ke {count} = {random_number}”.
 6. Akhir Looping:
    - Ulangi langkah 4 dan 5 hingga count mencapai nilai n.
 7. Selesai:
    - Program selesai setelah menampilkan n bilangan acak yang kurang dari 0.5.
### Program python
![gambar 1](gmb1.png)
### Hasil program
![gambar 2](gmb2.png)

## Latihan2
Alur Algoritma Latihan2 :
 1. Mulai Program:
    - Inisialisasi modal awal sebesar Rp 100.000.000.
    - Buat daftar keuntungan_bulanan yang berisi persentase keuntungan untuk setiap bulan.
 2. Inisialisasi Variabel:
    - Inisialisasi total_keuntungan dengan nilai 0 untuk menyimpan total keuntungan selama 8 bulan.
 3. Looping:
    - Gunakan loop for untuk iterasi dari bulan 1 hingga bulan 8.
 4. Menghitung Keuntungan Bulanan:
    - Di dalam loop, hitung laba bulan ini dengan mengalikan modal awal dengan persentase keuntungan bulan tersebut.
    - Tambahkan laba bulan ini ke total_keuntungan.
 5. Menampilkan Keuntungan Bulanan:
    - Cetak keuntungan untuk bulan tersebut.
 6. Akhir Looping:
    - Ulangi langkah 4 dan 5 untuk setiap bulan hingga bulan ke-8.
 7. Menampilkan Total Keuntungan:
    - Setelah loop selesai, cetak total keuntungan selama 8 bulan.
 8. Selesai:
    - Program selesai.
### Program python
![gambar 3](gmb3.png)
### Hasil program
![gambar 4](gmb4.png)

## Latihan3
Alur Algoritma Latihan3 :
 1. Mulai Program:
    - Inisialisasi saldo awal sebesar Rp 1.000.000.
 2. Tampilkan Menu:
    - Tampilkan menu pilihan kepada pengguna:
      > Cek Saldo
      > Tarik Tunai
      > Keluar
 3. Meminta Input Pengguna:
    - Minta pengguna memilih opsi dari menu.
 4. Proses Pilihan Pengguna:
    - Jika Pilihan 1 (Cek Saldo):
      > Tampilkan saldo saat ini.
    - Jika Pilihan 2 (Tarik Tunai):
      > Minta pengguna memasukkan jumlah uang yang ingin ditarik.
      > Periksa apakah jumlah yang diminta lebih besar dari saldo.
        > Jika ya, tampilkan pesan “Saldo tidak mencukupi.”
        > Jika tidak, kurangi saldo dengan jumlah yang diminta dan tampilkan saldo saat ini.
    - Jika Pilihan 3 (Keluar):
      > Tampilkan pesan “Terima kasih telah menggunakan ATM kami.” dan akhiri program.
    - Jika Pilihan Tidak Valid:
      > Tampilkan pesan “Pilihan tidak valid. Silakan coba lagi.”
 5. Ulangi Proses:
    - Kembali ke langkah 2 hingga pengguna memilih untuk keluar.
### Program python
![gambar 5](gmb5.png)
### Hasil program
![gambar 6](gmb6.png)
