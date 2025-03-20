import os
os.system('cls') # attīra termināla logu pašā sākumā
print("\n") # ieliek tukšu rindiņu pirms izdrukas

punkti = int(input("Punkti: "))

if punkti >= 90 and punkti <= 100:
    print("Vērtējums: 10")
elif punkti >=80 and punkti < 90:
    print("Vērtējums; 9")
elif punkti >=70 and punkti < 80:
    print("Vērtējums: 8")
elif punkti >=60 and punkti < 70:
    print("Vērtējums: 7")
else:
    print("Vērtējums: n/v")