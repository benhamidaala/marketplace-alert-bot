import os
import time
import requests

# بوت تتبع الإعلانات - Marketplace Alert Bot
BOT_TOKEN = os.environ.get("BOT_TOKEN")
CHAT_ID = os.environ.get("CHAT_ID")

def send_telegram_message(message):
    if not BOT_TOKEN or not CHAT_ID:
        print("Telegram token or chat ID is missing!")
        return
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_icon": "🔔",
        "chat_id": CHAT_ID,
        "text": message,
        "parse_mode": "HTML"
    }
    try:
        response = requests.post(url, json=payload)
        return response.json()
    except Exception as e:
        print(f"Error sending message: {e}")

if __name__ == "__main__":
    print("Bot is running...")
    send_telegram_message("🤖 تم تشغيل بوت تتبع الإعلانات بنجاح!")
