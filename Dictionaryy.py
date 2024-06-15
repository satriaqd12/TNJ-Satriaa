Profile_1 = {
    "name": "Satria", #key: Balue
    "Is_male": True,
    "age": 14,
    "Hobbies": ["Gaming", "Travel"]
}

print(Profile_1["name"]) #Dictionary_Name[Key]
print("Umur ", Profile_1["name"], ":", Profile_1["age"])

Profile_Karyawan = {
    "Nama": "Olivia",
    "Perkerjaan": "Desainer"
}
print(Profile_Karyawan)
Profile_Karyawan["Perkerjaan"] = "Mentor"
print(Profile_Karyawan)
Profile_Karyawan["instansi"] = "Technonatura Jogja"
print(Profile_Karyawan) 

Profile_Karyawan.pop("Nama")#Penghapus data
print(Profile_Karyawan)

buku = {}
Judul = "laskar Pelangi"
Penulis = "Budi"
Tahun = 2024

buku["judul"] = Judul
buku["Penulis"] = Penulis
buku["Tahun"] = Tahun
print(buku)