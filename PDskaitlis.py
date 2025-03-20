import os
os.system('cls') # attīra termināla logu pašā sākumā
print("\n") # ieliek tukšu rindiņu pirms izdrukas

x = int(input("Kāda ir skaitlis? "))


if x < 0:
    print("Negatīvs skaitlis")
if x == 0:
    print("Nulle")
if x > 0:
    print("Pozitīvs skaitlis")

if x % 2:
    print("nepāra skaitlis")
else:
    print("pāra skaitlis")
