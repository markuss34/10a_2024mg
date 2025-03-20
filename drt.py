import os
os.system('cls') 
print("\n") 


import pandas as pd





file_path = "dopings.csv" 

df = pd.read_csv(file_path)





def aizliegtas_sac(df):

    return df[df["Aizliegts sacensību laikā"] == "Jā"]




def aizliegtas_arpus(df):

    return df[df["Aizliegts ārpus sacensībām"] == "Jā"]





def meklet_vielu(df, nosaukums):

    return df[df["medicine_name"].str.contains(nosaukums, case=False, na=False)]





def aizliegtas_sportam(df, sports):

    return df[df["Sporta veidi, kuros aizliegts sacensību laikā"].str.contains(sports, case=False, na=False)]





print("Aizliegtas sacensību laikā:")

print(aizliegtas_sac(df).head())



print("\nAizliegtas ārpus sacensībām:")

print(aizliegtas_arpus(df).head())



print("\nMeklēšanas piemērs ('Physioneal'):")

print(meklet_vielu(df, "Physioneal"))



print("\nPārbaude sportam 'riteņbraukšana':")

print(aizliegtas_sportam(df, "riteņbraukšana"))

