import requests
import time

TOKEN = "7600881735:AAGu0emM0hUoLcvhigZ7mby6PbSaSgvtV0Q"
CHAT_ID = "-4853395195"
CHECK_URL = "https://www.tesla.com/tr_tr/inventory/new/my"

def send_message(msg):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    data = {"chat_id": CHAT_ID, "text": msg}
    try:
        requests.post(url, data=data)
    except:
        pass

def check_inventory():
    r = requests.get(CHECK_URL)
    if "Aradığınız Tesla'yı göremiyor musunuz?" not in r.text:
        send_message("🚨 Yeni Model Y stoğu tespit edildi! Tesla sitesine göz at: " + CHECK_URL)

while True:
    check_inventory()
    time.sleep(60)
