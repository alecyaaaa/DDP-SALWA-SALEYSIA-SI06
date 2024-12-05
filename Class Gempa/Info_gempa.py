from Gempa import *

#membuat ojek gempa dengan lokasi dan skala gempa
gempa1 = gempa("Banten", 1.2)
gempa2 = gempa("Palu", 6.1)
gempa3 = gempa("Cianjur",5.6)
gempa4 = gempa("Jayapura", 3.3)
gempa5 = gempa("Garut", 4.0)

#info gempa 
print("## Gempa bumi info")
print()
gempa1.dampak() #memanggil method dampak()

print("## Gempa bumi info")
print()
gempa2.dampak() #memanggil method dampak()

print("## Gempa bumi info")
print()
gempa3.dampak() #memanggil method dampak()

print("## Gempa bumi info")
print()
gempa4.dampak() #memanggil method dampak()

print("## Gempa bumi info")
print()
gempa5.dampak() #memanggil method dampak()

