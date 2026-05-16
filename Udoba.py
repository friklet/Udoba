import requests
import asyncio
from telegram import Bot

# ТВОИ ДАННЫЕ
TOKEN = "8218029682:AAEslsX9CkshLazDq4LahrSZLkoVTHrOhKI"
API_KEY = "b6907d289e10d714a6e88b30761fae22"  # бесплатный ключ OpenWeatherMap
CITY = "Omsk"

# Запускаем бота
bot = Bot(token=TOKEN)

# Получаем погоду
def get_weather():
    url = f"https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric&lang=ru"
    data = requests.get(url).json()
    
    temp = data['main']['temp']  # температура
    desc = data['weather'][0]['description']  # описание (ясно, дождь)
    feels = data['main']['feels_like']  # ощущается как
    wind = data['wind']['speed']  # ветер
    
    return temp, desc, feels, wind

# Подбираем одежду
def what_to_wear(temp):
    if temp > 30:
        return "🩳 Шорты, майка, шляпа! Очень жарко!"
    elif temp > 25:
        return "👕 Футболка, шорты/юбка, кепка"
    elif temp > 20:
        return "👖 Футболка, джинсы или шорты"
    elif temp > 15:
        return "🧥 Легкая куртка, джинсы, кроссовки"
    elif temp > 10:
        return "🧥 Куртка, джинсы, шапка с собой"
    elif temp > 0:
        return "🧣 Тёплая куртка, шапка, перчатки"
    elif temp > -10:
        return "🧥 Пуховик, шапка, шарф, перчатки"
    elif temp > -20:
        return "🥶 Очень теплая одежда, варежки!"
    else:
        return "🥶❄️ СИЛЬНЫЙ МОРОЗ! Шуба, валенки, всё тёплое!"

# Главная функция
async def main():
    print("Бот запущен! Жду команды...")
    
    # Получаем последние сообщения
    update_id = 0
    
    while True:
        updates = await bot.get_updates(offset=update_id + 1)
        
        for update in updates:
            update_id = update.update_id
            
            if update.message and update.message.text:
                text = update.message.text.lower()
                chat_id = update.message.chat.id
                
                if text in ['/start', 'погода', 'омск']:
                    try:
                        temp, desc, feels, wind = get_weather()
                        
                        # Сообщение
                        msg = f"""
🌤 ПОГОДА В ОМСКЕ:
🌡 Температура: {temp}°C
📝 {desc}
🌬 Ветер: {wind} м/с
🤔 Ощущается как: {feels}°C

👔 ЧТО НАДЕТЬ:
{what_to_wear(temp)}
                        """
                        await bot.send_message(chat_id, msg)
                        
                    except:
                        await bot.send_message(chat_id, "❌ Ошибка! Попробуй позже")
                
                elif text == '/help':
                    await bot.send_message(chat_id, "Напиши 'погода' или 'Омск' чтобы узнать погоду!")
                
                else:
                    await bot.send_message(chat_id, "Напиши 'погода' чтобы узнать!")

# Запуск
asyncio.run(main())