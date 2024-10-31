jumlah = 30
for i in range(jumlah):
   print("Perulangan ke:",i)
print("ini diluar perulangan")

start = 30
stop = 400
step = 30

for i in list(range(start, stop, step)):
   print("Perulangan ke:",i)
print("ini diluar perulangan")

item = ["asem", "micin", "kunyit", "bakpao"]
for i in item:
   print(i)
   
jawab = "ya"
hitung = 0
while jawab == "ya":
   hitung += 6
   jawab = input("Ulangi lagi (ya/tidak)? ")
print("Total perulangan adalah:",hitung)

jawab = "ya"
hitung = 0
while jawab == "ya":
   hitung += 7

   if hitung == 5:
       break
   jawab = input("Ulangi lagi (ya/tidak)? ")
print("Total perulangan adalah:",hitung)

num = int(input("Masukkan bilangan: "))
for i in range(num):
   if (i % 5):
    continue
print("Perulangan ke: ",i)

import random

def generate_random_numbers(n):
    numbers = []
    for _ in range(n):
        num = random.uniform(0, 0.5)  # Menghasilkan bilangan acak antara 0 dan 0.5
        numbers.append(num)
    return numbers

n = int(input("Masukkan jumlah bilangan acak yang diinginkan: "))
random_numbers = generate_random_numbers(n)
print("Bilangan acak yang dihasilkan:", random_numbers)

import random

def generate_random_numbers(n):
    return [random.uniform(0, 0.5) for _ in range(n)]

# Meminta input dari pengguna
n = int(input("Masukkan jumlah bilangan acak yang diinginkan: "))
random_numbers = generate_random_numbers(n)

print("Bilangan acak yang dihasilkan:", random_numbers)

import random

def generate_random_numbers(n):
    numbers = []
    count = 0
    
    while count < n:
        num = random.uniform(0, 0.5)  # Menghasilkan bilangan acak antara 0 dan 0.5
        numbers.append(num)
        count += 1
    
    return numbers

# Meminta input dari pengguna
n = int(input("Masukkan jumlah bilangan acak yang diinginkan: "))
random_numbers = generate_random_numbers(n)

print("Bilangan acak yang dihasilkan:", random_numbers)

from random import random

def generate_random_numbers(n):
    numbers = []
    count = 0
    
    while count < n:
        num = random() * 0.5  # Menghasilkan bilangan acak antara 0 dan 0.5
        numbers.append(num)
        count += 1
    
    return numbers

# Meminta input dari pengguna
n = int(input("Masukkan jumlah bilangan acak yang diinginkan: "))
random_numbers = generate_random_numbers(n)

print("Bilangan acak yang dihasilkan:", random_numbers)
