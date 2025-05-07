import requests
from flask import Flask, request

app = Flask(__name__)

TELEGRAM_BOT_TOKEN = "7981671598:AAHGQxtOEUWiQBmkrFSVTYarQ57Ki2tHCEQ"
TELEGRAM_CHAT_ID = "-1002564437647"

@app.route('/', methods=['POST'])
def alert():
    data = request.data.decode('utf-8')
    message = f"📊 TradingView Alert:\n{data}"
    send_telegram_message(message)
    return 'ok'

def send_telegram_message(msg):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {"chat_id": TELEGRAM_CHAT_ID, "text": msg}
    requests.post(url, json=payload)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
