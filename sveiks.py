print ("Sveiks, labo skolēn!")
print("hello, \"friend\"")
print("Markuss",    "Pastars", sep='?????')
name = input("Kā tevi sauc? ")

name = name.strip().title()

pirmais, otrais = name.split(" ")


print("Sveiks,", pirmais)
print(f"Sveiks, {name}")