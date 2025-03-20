import os
os.system('cls') # attīra termināla logu pašā sākumā
print("\n")# ieliek tukšu rindiņu pirms izdrukas

dyear = int(input("Enter a year: "))
if (dyear % 4 == 0 and dyear % 100 != 0) or (dyear % 400 == 0):
    print(dyear, " garais gads")
else:
    print(dyear, "nav garais gads")