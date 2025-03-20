import os
os.system('cls')
print("\n") 

#1.uzdevums

#teksts = input("Ieraksti kaut kādu tekstu:")
#print(teksts[-5:])

#2.uzdevums

#skaitlis = input("ievadiet skaitli: ")
#x = skaitlis
#for x in range(20):
    #if x %3 == 0:
       # continue
    #print(x)
    #if x ==20:
        #break


 #3.uzdevums
# x = int(input("Ievadi skaitli:"))

# n = [

#     x,
#     x-1,
#     x-2,
#     x-3,
#     x-4,
#     x-5,
#     x-6,
#     x-7,
#     x-8,
#     x-9,
#     x-10,

# ]

# for i in n:

#     print(i)


 #4.uzdevums
vardnica = {"Anna": 20, "Jānis": 22, "Ilze": 19, "Patriks": 16, "Arnolds": 22}

x = input("Ievadiet kādu vārdu: Anna, Jānis, Ilze, Patriks vai Arnolds: ")

print(vardnica.get (x))

#5uzd