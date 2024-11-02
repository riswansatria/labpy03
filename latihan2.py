modal_awal = 100_000_000

keuntungan_bulanan = [0, 0, 0.01, 0.01, 0.05, 0.05, 0.05, 0.03]

total_keuntungan = 0
modal_sekarang = modal_awal

print("Keuntungan tiap bulan:")
for bulan in range(8):
    laba_bulan_ini = modal_sekarang * keuntungan_bulanan[bulan]
    total_keuntungan += laba_bulan_ini
    modal_sekarang += laba_bulan_ini
    print(f"Bulan {bulan + 1}:Rp{laba_bulan_ini:.2f}")

print(f"\nTotal keuntungan selama 8 bulan: Rp{total_keuntungan:.2f}")