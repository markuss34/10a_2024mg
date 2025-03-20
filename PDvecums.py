import os
os.system('cls') # attīra termināla logu pašā sākumā
print("\n") # ieliek tukšu rindiņu pirms izdrukas

vecums = int(input("Vecums: "))

if vecums >= 0 and vecums <= 7:
    print("Biļetes cena: bez maksas")
elif vecums >=7 and vecums < 18:
    print("Biļetes cena: 5 eiro")
elif vecums >=18 and vecums < 65:
    print("Biļetes cena: 10 eiro")
elif vecums >=65:
    print("Bi.letes cena: 3 eiro")
else:
    print("Vērtējums: n/v")