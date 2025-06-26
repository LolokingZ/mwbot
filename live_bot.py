import requests
import time
from bs4 import BeautifulSoup
from telegram import Bot

BOT_TOKEN = "7634480398:AAHvADKAg5XGB91At9bYrcY-8CmRC5SG5sA"
CHAT_ID = 1192099192
URL = "https://gamblingcounting.com/id/mega-wheel"

bot = Bot(BOT_TOKEN)

def get_latest_number():
    try:
        html = requests.get(URL).text
        soup = BeautifulSoup(html, "html.parser")
        all_balls = soup.find_all("div", class_="ball")
        numbers = [b.text.strip() for b in all_balls if b.text.strip().isdigit()]
        return int(numbers[0]) if numbers else None
    except Exception as e:
        print("Gagal ambil data:", e)
        return None

last_number = None

while True:
    number = get_latest_number()
    if number and number != last_number:
        last_number = number
        msg = f"🎯 Angka terbaru Mega Wheel: *{number}*"
        bot.send_message(chat_id=CHAT_ID, text=msg, parse_mode="Markdown")
        print("Terkirim:", msg)
    time.sleep(10)
