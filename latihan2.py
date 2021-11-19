max = 0
jumlahAngka = 0

while True:
    a = int(input("masukan angka: "))
    if(a>max):
        max = a
    if(a == 0):
        break
print("Angka Terbesar adalah ", max)
