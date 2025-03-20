import os
os.system('cls') 
print("\n") 


#1.uzdevums

#produkti = {
    #"Briseles kāposti": 4,4 g/100 g,
    #"Seleriju saknes": 4,2 g/100 g,
    #"Brokoļi": 3,0 g/100 g,
    #"Ziedkāposti": 2,9 g/100 g,
   #"Burkāni": 2,9 g/100 g,
    #"Sarkanās bietes": 2,5 g/100 g,
    #"Salāti": 1,8 g/100 g,
    #"Upenes": 6,8 g/100 g,
    #"Avenes": 5,0 g/100 g,
    #"Zemenes": 4,0 g/100 g,
    #"Jāņogas": 2,5 g/100 g,
    #"Āboli": 2,3 g/100 g,
    #"Apelsīni": 2,2 g/100 g,
   # "Plūmes": 1,7 g/100 g
#}


#produkts = int(input("Ievadiet produkta nosaukumu- "))
#if produkts in produkti:
    #print(f"Balastvielu daudzums ir {produkts} {produkti}.")

#2.uzdevums
# vārds = input("Ievadiet vārdu: ")
# patskani = "aeiouAEIOU"
# rezultāts = ""
# for letter in vārds:
#     if letter not in patskani:
#         rezultāts += letter

# print("Saīsināts vārds", rezultāts)

#3.uzdevums

cena = 90

summa = 0

nauda=[5,10,20,50]

while summa<cena:

    ievadita_moneta = int(input("Ievieto monētu 5, 10 , 20 vai 50 centi: "))

    if ievadita_moneta in nauda:

        summa += ievadita_moneta

        print(f"Pašlaik ievietotā summa: {summa} centi.")

    else: print("Nederīga moneta. Lūdzu ievadiet 5, 10, 20, 50 centus.")

atlikums = summa - cena

if atlikums > 0:

    print(f"Jāizdod {atlikums} centi.")


#4.uzdevums