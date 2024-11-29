import math 

def l_persegi(sisi):
    luas = sisi * sisi
    keliling = sisi*sisi*sisi*sisi
    print(f'Luas persegi {sisi} * {sisi} = {luas}')
    print(f'Keliling persegi adalah {keliling}')
def l_persegipanjang(panjang, lebar):
    luaspsgpnjg = panjang * lebar
    print(f'Luas persegi panjang {panjang} * {lebar} = {luaspsgpnjg}')
def l_segitiga(alas, tinggi):
    luassgt = 1/2 * alas * tinggi 
    print(f'Luas Segitiga {1/2} * {alas} * {tinggi} = {luassgt}')
def l_belahketupat(d1, d2):
    luasblhktpt = 1/2 * d1 * d2
    print(f'Luas belah ketupat {1/2} * {d1} * {d2} = {luasblhktpt}')
def l_layanglayang(d1, d2):
    luaslyng = 1/2 * d1 * d2
    print(f'Luas layang layang {1/2} * {d1} * {d2} = {luaslyng}')

def l_balok(panjang, lebar, tinggi):
    luasbalok = 2 * (panjang*lebar) + (panjang*tinggi) + (lebar*tinggi)
    print(f'Luas balok adalah {luasbalok}')
def l_kubus(sisi):
    luaskubus = 6 * (sisi*sisi)
    print(f'Luas Kubus adalah {luaskubus}')
def l_tabung(jari2, tinggi):
    luastabung = 2 * 22/7 * (jari2 + tinggi)
    print(f'Luas Tabung adalah {luastabung}')
def l_limassegiempat(sisi, sisitegak):
    luaslimassgempt = (sisi*sisi) + (4*sisitegak)
    print(f'Luas Limas Segiempat adalah {luaslimassgempt}')
def l_primasegitiga(luasalas, sisitegak):
    luasprismasgt = (2*luasalas) + (3*sisitegak)
    print(f'Luas Prisma Segitiga Adalah {luasprismasgt}')