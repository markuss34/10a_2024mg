import os
os.system('cls') # attīra termināla logu pašā sākumā
print("\n") # ieliek tukšu rindiņu pirms izdrukas

def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

gradi = int(input("grādi - ?"))
print(f"{gradi}°C = {CtoF(gradi):.2f}°F")
