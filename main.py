import requests
from datetime import datetime
from bs4 import BeautifulSoup
from bot import send_telegram_message

url = "https://www.cgeonline.com.ar/informacion/apertura-de-citas.html"

response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")

    rows = soup.find_all("tr")
    for row in rows:

        columns = row.find_all("td")
        if (
            columns
            and "pasaportesrenovación" in columns[0].get_text(strip=True).lower()
        ):
            third_col = columns[2].get_text(strip=True)
            if third_col != "fecha por confirmar":
                send_telegram_message(f"Fecha: {third_col}")
            else:
                print(f"No hay fechas disponibles al {datetime.today()}")
            break
else:
    print(f"Error al acceder a la página: {response.status_code}")
