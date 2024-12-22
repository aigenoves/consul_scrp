import os
import requests

CHAT_ID = "254021544"
TELEGRAM_API_TOKEN = os.environ.get("TELEGRAM_API_TOKEN")


def send_telegram_message(message: str):
    print(f"API:{TELEGRAM_API_TOKEN}")
    url = f"https://api.telegram.org/bot{TELEGRAM_API_TOKEN}/sendMessage"
    response = requests.post(url, data={"chat_id": CHAT_ID, "text": message})
    if response.status_code == 200:
        return True
    else:
        return False
        # print(f"Error al enviar el mensaje: {response.status_code}, {response.text}")
