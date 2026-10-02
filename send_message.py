import requests

TOKEN = "8973762379:AAGwEuCF7vWWqRrgED8gJW-4NCv4RDoCb1Q"
CHAT_ID = "-1004455970098"
MESSAGE = "📰 خبر جدید بزارید آزاد"

url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

response = requests.post(url, data={
    "chat_id": CHAT_ID,
    "text": MESSAGE
})

print(response.status_code)
print(response.text)
