import os
os.system('cls') # attīra termināla logu pašā sākumā
print("\n") # ieliek tukšu rindiņu pirms izdrukas

# import pandas
# from datetime import datetime
# import ctypes

# # Ielasa datus no CSV
# df = pandas.read_csv("saraksts.csv", sep=";", dtype=str)

# # Pieprasa lietotājam ievadīt datumu
# input_date = input("Ievadiet datumu (DD.MM): ")

# # Ja ievadīts datums ir derīgs (piemēram, 27.02), veic datuma apstrādi
# try:
#     datetime.strptime(input_date, "%d.%m")
# except ValueError:
#     print("Nepieņemams datuma formāts. Lūdzu, ievadiet datumu formātā DD.MM.")
#     exit()

# # Saīsina "Dzimšanas datums" kolonu līdz tikai dienai un mēnesim
# df["Dzimšanas datums"] = df["Dzimšanas datums"].str[:5]

# # Filtrē skolēnus ar ievadīto dzimšanas dienu
# bd_skoleni = df[df["Dzimšanas datums"] == input_date]

# # Ja ir atrasti skolēni ar dzimšanas dienu, veido ziņu
# if not bd_skoleni.empty:
#     teksts = f"Sveicam dzimšanas dienā {input_date}!!!\n\n"
#     for _, row in bd_skoleni.iterrows():
#         teksts += f"{row['Vārds'].upper()}\n{row['Klase'].upper()}\n{row['Deklarētā adrese'].upper()}\n\n"
# else:
#     teksts = f"Nav neviena dzimšanas diena {input_date}!!!"

# # Parāda ziņojumu logā
# ctypes.windll.user32.MessageBoxW(0, teksts.strip(), "svinam", 1)


import pandas
from datetime import datetime, timedelta
import ctypes

# Ielasa datus no CSV
df = pandas.read_csv("saraksts.csv", sep=";", dtype=str)

# Iegūst šodienas un rītdienas datumus formātā DD.MM
today = datetime.today().strftime("%d.%m")
tomorrow = (datetime.today() + timedelta(days=1)).strftime("%d.%m")

# Saīsina "Dzimšanas datums" kolonu līdz tikai dienai un mēnesim
df["Dzimšanas datums"] = df["Dzimšanas datums"].str[:5]

# Filtrē skolēnus ar dzimšanas dienu šodien vai rīt
bd_today = df[df["Dzimšanas datums"] == today]
bd_tomorrow = df[df["Dzimšanas datums"] == tomorrow]

# Veido ziņu
if not bd_today.empty or not bd_tomorrow.empty:
    teksts = "Šodienas un rītdienas dzimšanas dienas!!!\n\n"
    
    if not bd_today.empty:
        teksts += f"Šodien, {today}:\n"
        for _, row in bd_today.iterrows():
            teksts += f"{row['Vārds'].upper()}\n{row['Klase'].upper()}\n{row['Deklarētā adrese'].upper()}\n\n"
    
    if not bd_tomorrow.empty:
        teksts += f"Rīt, {tomorrow}:\n"
        for _, row in bd_tomorrow.iterrows():
            teksts += f"{row['Vārds'].upper()}\n{row['Klase'].upper()}\n{row['Deklarētā adrese'].upper()}\n\n"
else:
    teksts = "Nav neviena dzimšanas diena šodien vai rīt!!!"

# Parāda ziņojumu logā
ctypes.windll.user32.MessageBoxW(0, teksts.strip(), "svinam", 1)
