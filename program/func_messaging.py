import requests
from decouple import config

# Send Message
def send_message(message):
  bot_token = config("TELEGRAM_TOKEN")
  chat_id = config("TELEGRAM_CHAT_ID")
  url = f"https://api.telegram.org/bot{"7464801782:AAHokM3Xq7cKMYiGW1yzf3ofBrzH_P56_zg"}/sendMessage?chat_id={"6936106824"}&text={message}"
  res = requests.get(url)
  if res.status_code == 200:
    return "sent"
  else:
    return "failed"
