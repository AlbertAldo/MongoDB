import pymongo
from pymongo import MongoClient

client = MongoClient('localhost:27017')
dbServer = 'mongodb://localhost:27017'
myMongo = pymongo.MongoClient(dbServer) # Aktifin Database
dbs = myMongo.list_database_names()
# print(dbs)

kampus = myMongo['Kampus'] # Database Kampus
# kampus.command("createUser", 'andi', pwd = 'anditopsecret', roles = ["dbAdmin","readWrite"])
# kampus.command("createUser", 'budi', pwd = 'buditopsecret', roles = ["readWrite"])
print(kampus.command("usersInfo"))

dosen = kampus['Dosen'] # Collection Dosen
mahasiswa = kampus['Mahasiswa'] # Collection Mahasiswa
# list_col = kampus.list_collection_names()
# print(list_col)

datadosen = [{"nama":"Caca",
"usia":28,
"asal":"Jakarta",
"bidang":"Fisika Astrologi",
"titel":"S2",
"status":"Honorer",
"nip":"123",
"matkul":["Metrologi","Kosmologi","Kalkulus"]},

{"nama":"Dedi",
"usia":29,
"asal":"Yogyakarta",
"bidang":"Fisika Terapan",
"titel":"S3",
"status":"PNS",
"nip":"456",
"matkul":["Instrumentasi","Elektronika","Fisika Dasar"]},

{"nama":"Euis",
"usia":30,
"asal":"Bandung",
"bidang":"Fisika Teoretik",
"titel":"S1",
"status":"Honorer",
"nip":"789",
"matkul":["Fisika Dasar","Fisika Modern","Kalkulus"]}]

datamahasiswa = [{"nama":"Faza",
"usia":19,
"asal":"Aceh",
"prodi":"Fisika",
"angkatan":2017,
"nim":"123"},

{"nama":"Gilang",
"usia":20,
"asal":"Semarang",
"prodi":"Fisika",
"angkatan":2017,
"nim":"456"},

{"nama":"Hanafi",
"usia":20,
"asal":"Makassar",
"prodi":"Fisika",
"angkatan":2017,
"nim":"789"},

{"nama":"Dini",
"usia":20,
"asal":"Bekasi",
"prodi":"Fisika",
"angkatan":2017,
"nim":"004"}
    
]

"""
Menginput data dosen
"""
# x = dosen.insert_many(datadosen)
"""
Menginput data mahasiswa
"""
# y = mahasiswa.insert_many(datamahasiswa)
# print("Data Submitted")

# print(list(dosen.find()))
# print(list(mahasiswa.find()))

"""
Menghapus Faza dari Collection Mahasiswa
"""
kondisino1 = {"nama" : "Faza"}
mahasiswa.delete_one(kondisino1)
# print("Faza berhasil terhapus dari Collection Mahasiswa")
# print(list(mahasiswa.find()))

"""
Menambah Dodi ke Collection Dosen
"""
kondisino2 = {"nama":"Dodi",
"usia":27,
"asal":"Surabaya",
"bidang":"Computer Science",
"titel":"S2",
"status":"PNS",
"nip":"998",
"matkul":["Data Analysis","AI","NLP"]}
# dosen.insert_one(kondisino2)
# print("Dodi berhasil ditambahkan ke Collection Dosen")
# print(list(dosen.find()))

"""
Ubah Nama Hanafi menjadi Ahmad Hanafi dan Usia nya menjadi 22 (Mahasiswa)
"""

kondisino3 = {"nama" : "Hanafi"}
termsno3 = {"$set" : {"nama" : "Ahmad Hanafi", "usia" : 22}}
# mahasiswa.update_one(kondisino3, termsno3)
# print("Hanafi berhasil diubah jadi Ahmad Hanafi dan usianya menjadi 22 tahun")
# print(list(mahasiswa.find()))

"""
Ubah semua Prodi Mahasiswa yang berusia 20 menjadi Matematika (Mahasiswa)
"""

kondisino4 = {"usia" : 20}
termsno4 = {"$set" : {"prodi" : "Matematika"}}
# mahasiswa.update_many(kondisino4, termsno4)
# print("Berhasil mengubah seluruh prodi Mahasiswa yang berumur 20 menjadi Matematika")
# print(list(mahasiswa.find()))

"""
Ubah field asal menjadi Kota_asal (Mahasiswa)
"""

kondisino5 = {}
termsno5 = {"$rename" : {"asal" : "kota_asal"}}
# mahasiswa.update_many(kondisino5, termsno5)
# print("Berhasil mengubah seluruh property 'asal' Mahasiswa menjadi 'kota_asal' !")
# print(list(mahasiswa.find()))

