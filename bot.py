import os
import requests

CHAT_IDS = os.environ.get("TELEGRAM_CHAT_IDS").split(",")

TELEGRAM_API_TOKEN = os.environ.get("TELEGRAM_API_TOKEN")


def send_telegram_message(message: str):
    for id in CHAT_IDS:
        print(id)
        url = f"https://api.telegram.org/bot{TELEGRAM_API_TOKEN}/sendMessage"
        response = requests.post(url, data={"chat_id": id, "text": message})
        if response.status_code == 200:
            return True
        else:
            print(
                f"Error al enviar el mensaje: {response.status_code}, {response.text}"
            )
            return False
