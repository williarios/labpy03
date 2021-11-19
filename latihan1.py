import random

banyakNilai = int(input("Masukan Banyaknya angka: "))
a = 0
for i in range (banyakNilai):
    a = random.uniform(.0,.5)
    print("data ke ",i+1, " = ",a)
