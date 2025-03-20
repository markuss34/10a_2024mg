import os
os.system('cls') 
print("\n") 

import pandas

df = pandas.read_csv("dopings.csv", sep=";", dtype=str)

def aizliegtas_vielas (df):
    return df[df["Aizliegtas vielas sacensībās"] == "Jā"][["Vielas _nosaukums", ""]]
