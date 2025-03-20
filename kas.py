import os
os.system('cls') # attīra termināla logu pašā sākumā
print("\n") # ieliek tukšu rindiņu pirms izdrukas



import requests
from bs4 import BeautifulSoup
from plyer import notification

url = "https://weather.com/en-IN/weather/today/l/56.95,24.11?par=google&temp=c"

def get_weather_data(url):
    try:
        r = requests.get(url, timeout=10)
        r.raise_for_status()
        return r.text
    except requests.exceptions.RequestException as e:
        print(f"Kļūda; {e}")
        return None

htmldata = get_weather_data(url)

if htmldata:
    soup = BeautifulSoup(htmldata, "html.parser")
    #print(soup. prettify())

    temp_elem = soup.find("span", {"data-testid": "TemperatureValue"})
    rain_elem = soup.find("span", {"data-testid": "PrecentageValue"})


    temperature = temp_elem.text if temp_elem else "Nav datu"
    rain = rain_elem.text if rain_elem else "Nav informācijas"

    result = f"Pašreizējā temperatūra Rīgā: {temperature}\nrain : {rain}"

    notification.notify(
        title = "Laika ziņas Rīgā",
        message = result,
        timeout = 10

    )
else:
        notification.notify(
        title = "Kļūda",
     message = "Nekas nav zināms",
        timeout = 10
        )