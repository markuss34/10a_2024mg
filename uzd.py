import os
os.system('cls')
print("\n") 


#1. uzdevums
# tekst = input("Ievadiet tekstu: ")

# with open("text.txt", 'w', encoding="utf8") as ieraksts:
#     ieraksts.write(tekst)

#2. uzdevums
# with open ("data (2).txt", 'r', encoding="utf8") as data:
#     x = len(data.readlines())
#     print(x)


#3.uzdevums
txt = input("Ievadiet vārdu: ").upper()
count=0
with open("vardi.txt", 'r', encoding="utf8") as data:
    lines = data.readlines()
    for row in lines:
        if row.find(txt) != -1:
            count+=1
    
print(count)

