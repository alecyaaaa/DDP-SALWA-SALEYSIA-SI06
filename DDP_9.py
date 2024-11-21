print('-- NOMOR 1 celcius ke fahrenheit --')
def celcius_ke_fahrenheit(celcius):
    print(celcius * 9/5 + 32)

celcius_ke_fahrenheit(0)
celcius_ke_fahrenheit(100)

print('============================')

print('-- NOMOR 2 Fungsi Is_genap --')
def is_genap(genap):
    print(genap %2 == 0)

is_genap(4)
is_genap(9)

print('==========================')

print('-- NOMOR 3 Keterangan lulus dan tidak lulus --')
def skor(nilai):
    if nilai >= 80:
        print('Lulus')
    else:
        print('Gagal')

skor(80)
skor(50)

print('===========================')

print('-- NOMOR 4 Mencetak Bilangan Ganjil --')
def bil_ganjil(ganjil):
    for i in range(1, ganjil + 1):
        print(i, end=' ')

bil_ganjil(20)