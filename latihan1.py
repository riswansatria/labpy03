import random

n = int(input("Masukkan jumlah bilangan acak yang ingin ditampilkan: "))

count = 0

while count < n:
   
    random_number = random.random()
    
    if random_number < 0.5:
        print(f"Data ke {count} = {random_number}")
        count += 1