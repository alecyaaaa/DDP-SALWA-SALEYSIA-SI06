#SOAL NOMOR 1
angka = int(input('Masukan bilangan bulat: '))
genap = 'bilangan genap'
ganjil = 'bilangan ganjil'

if angka % 2 == 0:
    print(genap)
elif angka % 2 != 0:
    print(ganjil)
else:
    print('Input tidak valid')

print()
print('===========================')
print()

#SOAL NOMOR 2
nilaiujian = int(input('Masukan nilai ujian: '))

if nilaiujian >= 75:
    print('Lulus')
else: 
    print('Tidak Lulus')

print()
print('=====================')
print()

#SOAL NOMOR 3
usia = int(input('Masukan usia anda: '))

if usia >= 18:
    print('Dewasa')
elif usia < 17 and usia > 13:
    print('Remaja')
else: 
    print('Anak-anak')

print()
print('===================')
print()

#SOAL NOMOR 4
statusAnggota = input('Masukan Status Anggota:')

if statusAnggota == 'gold' or statusAnggota == 'silver': 
    print('Selamat anda mendapatkan diskon')
elif statusAnggota == 'bronze':
    print('Maaf anda tidak mendapatkan diskon')
else:
    print('Input tidak valid')

print()
print('=====================')
print()

#SOAL NOMOR 5
jumlahpembelian = int(input('Masukan jumlah pembelian:'))
hargaItem = 1000
hargadiskon = hargaItem * jumlahpembelian * (10/10)
hargatotal = hargaItem * jumlahpembelian 
total = hargatotal - hargadiskon
totaltanpadiskon = hargaItem * jumlahpembelian

print(f'Anda mendapat diskon 10%, harga per item {hargaItem} jadi total harga yang harus dibayar adalah {total}') if jumlahpembelian > 100 else print(f'harga per item {hargaItem}, jadi total yang harus dibayar adalah {hargatotal}')