import requests
import asyncio
from telegram import Bot
from telegram.request import HTTPXRequest

# ТВОИ ДАННЫЕ
TOKEN = "8218029682:AAEslsX9CkshLazDq4LahrSZLkoVTHrOhKI"
API_KEY = "b6907d289e10d714a6e88b30761fae22"
CITY = "Omsk"

# ПРОКСИ ИЗ ТВОЕГО КОНФИГА (HTTP на порту 10809)
PROXY = "http://127.0.0.1:10809"

# Бот через прокси
request = HTTPXRequest(proxy_url=PROXY)
bot = Bot(token=TOKEN, request=request)

def get_weather():
    # Погода через тот же прокси
    proxies = {"http": PROXY, "https": PROXY}
    url = f"https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric&lang=ru"
    data = requests.get(url, proxies=proxies).json()
    temp = data['main']['temp']
    desc = data['weather'][0]['description']
    feels = data['main']['feels_like']
    wind = data['wind']['speed']
    return temp, desc, feels, wind

def what_to_wear(temp):
    if temp > 30:
        return "🩳 Шорты, майка, шляпа! Жара!"
    elif temp > 25:
        return "👕 Футболка, шорты/юбка"
    elif temp > 20:
        return "👖 Футболка, джинсы или шорты"
    elif temp > 15:
        return "🧥 Легкая куртка, джинсы"
    elif temp > 10:
        return "🧥 Куртка, джинсы, шапка с собой"
    elif temp > 0:
        return "🧣 Тёплая куртка, шапка, перчатки"
    elif temp > -10:
        return "🧥 Пуховик, шапка, шарф"
    elif temp > -20:
        return "🥶 Очень теплая одежда, варежки!"
    else:
        return "🥶❄️ СИЛЬНЫЙ МОРОЗ!"

async def main():
    print("✅ Бот через Xray запущен!")
    print(f"Прокси: {PROXY}")
    
    update_id = 0
    while True:
        try:
            updates = await bot.get_updates(offset=update_id + 1, timeout=10)
            for update in updates:
                update_id = update.update_id
                if update.message and update.message.text:
                    text = update.message.text.lower()
                    chat_id = update.message.chat.id
                    
                    if text in ['/start', 'погода', 'омск']:
                        temp, desc, feels, wind = get_weather()
                        msg = f"""
🌤 ПОГОДА В ОМСКЕ:
🌡 Температура: {temp}°C
📝 {desc}
🌬 Ветер: {wind} м/с
🤔 Ощущается: {feels}°C

👔 ОДЕЖДА:
{what_to_wear(temp)}
                        """
                        await bot.send_message(chat_id, msg)
                    
                    elif text == '/help':
                        await bot.send_message(chat_id, "Напиши 'погода' или 'Омск'!")
                    
                    else:
                        await bot.send_message(chat_id, "Напиши 'погода'!")
        except Exception as e:
            print(f"⚠️ Ошибка: {e}")
            await asyncio.sleep(3)

asyncio.run(main())