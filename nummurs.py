import os
os.system('cls') # attīra termināla logu pašā sākumā
print("\n") # ieliek tukšu rindiņu pirms izdrukas

#nummurs = int(input("ievadiet nummurzīmi- "))

#garums = len(nummurs)

#print(len(nummurs))

#if nummurs >= 4 and nummurs <= 7:
    #print("")
#elif punkti >=80 and punkti < 90:
    #print("Vērtējums; 9")
#elif punkti >=70 and punkti < 80:
    #print("Vērtējums: 8")
#elif punkti >=60 and punkti < 70:
    #print("Vērtējums: 7")
#else:
    #print("Vērtējums: n/v")

ievade = input("Ievadiet numura zīmi:")

numuri = ievade.split('-')

for numurs in numuri:
    numurs = numurs.split()

if len(numurs) < 4 or '-' not in numurs:
    print(f"{numurs}: Numura zīme nav derīga")
    

burti, cipari = numurs.split('-')

if len(burti) != 2 or not all(burts.isalpha() and burts in "ABCDEFGHIJKLMNOPRSTUVZ" for burts in burti.upper()):
    print(f"{numurs}: Numura zīme nav derīga.")

if not cipari.isdigit() or not (1 <= int(cipari) <=9999):
    print(f"{numurs}: Numura zīme nav derīga.")
    

print(f"{numurs}: Numura zīme ir derīga.")