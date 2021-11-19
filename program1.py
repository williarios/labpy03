jumlahBulan = 8
danaAwal = int(100000000)
totalLaba = 0
jumlahUntung = 0
laba = 0
for i in range(jumlahBulan):
    if(i>0 and i<2):
        laba = danaAwal*0
    elif(i>1 and i<4):
        laba = danaAwal*0.01
    elif(i>3 and i<7):
        laba = danaAwal*0.05
    elif(i>6 and i<9):
        laba = danaAwal*0.02
        
    jumlahUntung = jumlahUntung + laba
    totalLaba = jumlahUntung
    
    print("Laba bulan ke-", i+1, "sebesar: ", laba)
        
print("Total laba sebesar: ",totalLaba)
