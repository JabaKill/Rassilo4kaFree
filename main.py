import asyncio
from telethon import TelegramClient
from flask import Flask
import threading

# Данные из my.telegram.org
api_id = 24209149
api_hash = "357ffa520f5bc72970a54ee00d883cf8"
phone_number = "+380684401813"

# Список чатов для отправки сообщений
chat_usernames = [
    # ... (твой список чатов)
]

# Новое сообщение
message_text = """🚨ВНИМАНИЕ🚨
Заливаем 🔥ТОПОВЫЙ ТРАФИК🔥
# ... (твой текст сообщения)
"""

app = Flask(__name__)

@app.route('/')
def index():
    return "Сервис работает!"

async def send_messages():
    async with TelegramClient("session_name", api_id, api_hash) as client:
        await client.start(phone_number)
        print("✅ Бот запущен. Начинаю отправку сообщений...")
        while True:
            for chat in chat_usernames:
                try:
                    await client.send_message(chat, message_text)
                    print(f"✅ Сообщение отправлено в {chat}")
                    await asyncio.sleep(5)
                except Exception as e:
                    print(f"❌ Ошибка при отправке в {chat}: {e}")
            print("⏳ Жду 5 минут перед следующей отправкой...")
            await asyncio.sleep(300)

def run_bot():
    asyncio.run(send_messages())

if __name__ == "__main__":
    bot_thread = threading.Thread(target=run_bot)
    bot_thread.start()
    app.run(host='0.0.0.0', port=5000)
