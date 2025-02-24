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
    "@tgbirzga", "@traffic001", "@birzha_reklamy2", "@reklama_birja1",
    "@sharksalepr", "@trafik_chat", "@arbitraj_daddyaff", "@reklam_birzha",
    "@birzha_chat69", "@w2_chat", "@tgm_adm", "@advertising_exchange_1",
    "@work_online_today", "@top_ads_freelance", "@channel_market1",
    "@arbitragetrafficchat", "@tg_land_all", "@reklama_exchange",
    "@buy_sell_tiktok", "@zalivi_trafika", "@trafik_prodam_kuplyu",
    "@byrzha_reklamy2", "@birzha_reklamy9", "@byrzha_reklami2",
    "@birzha_reklami3", "@birzha_reklamy22", "@birzha_reklami7",
    "@saletraff", "@channel_market1", "@top_ads_freelance", "https://t.me/Birzha_trafika", "@work_online_today", "@trafik_chat"
]

# Новое сообщение
message_text = """🚨ВНИМАНИЕ🚨
Заливаем 🔥ТОПОВЫЙ ТРАФИК🔥

🔵Мы работаем с любой тематикой и аудиторией — наша экосистема справится с любым запросом.
➡️У нас гибкий выбор МЦА и ЖЦА.
💸Цены — от 0.05$ до 0.4$ за подписчика.
⚡️Живая и качественная аудитория, без ботов и мусора.
✅ Много положительных отзывов и последние офферы в наличии!

✈️Заказ: @nakamuraboost
🏦Оплата любым удобным способом!
"""

async def send_messages():
    async with TelegramClient("session_name", api_id, api_hash) as client:
        await client.start(phone_number)
        print("✅ Бот запущен. Начинаю отправку сообщений...")

        while True:
            for chat in chat_usernames:
                try:
                    await client.send_message(chat, message_text)
                    print(f"✅ Сообщение отправлено в {chat}")
                    await asyncio.sleep(5)  # Пауза между отправками
                except Exception as e:
                    print(f"❌ Ошибка при отправке в {chat}: {e}")

            print("⏳ Жду 5 минут перед следующей отправкой...")
            await asyncio.sleep(300)  # Ждать 5 минут

app = Flask(__name__)

@app.route('/')
def index():
    return "Бот запущен!"

def run_bot():
    asyncio.run(send_messages())

if __name__ == "__main__":
    threading.Thread(target=run_bot).start()  # Запускаем бота в отдельном потоке
    app.run(host='0.0.0.0', port=5000)  # Укажите порт, который вам нужен
