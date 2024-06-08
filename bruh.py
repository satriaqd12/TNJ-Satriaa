inventaris = ["Printer", "Laptop", "Scanner", "Monitor"]
print(inventaris)

item_baru = "Keyboard"
inventaris.append(item_baru)
print(inventaris)

karyawan = ["Andi", "Budi", "Citra", "Dewi"]
print(karyawan)

karyawan_baru = "Eka"
karyawan.append(karyawan_baru)
print(karyawan)

harga_produk = [50000, 150000, 25000, 75000]
print(harga_produk)
harga_baru = 100000
harga_produk.append(harga_baru)
print(harga_produk)

inventaris.remove("Scanner")
print(inventaris)

karyawan.remove("Budi")
print(karyawan)

print(len(inventaris))
print(len(karyawan))

Level_7 = ["Akhdan", "Syauqi", "Alghar", "Zaki"]
Level_8 = ["Athar", "satria", "Alfath", "agha", "Banyu"]
Level_9 = ["Mas yafi", "Mas Ata"]

Suku_tekno = Level_7 + Level_8 + Level_9
print(Suku_tekno)