import requests
import tkinter as tk

def update():
    # Координаты Омска
    lat, lon = 54.9893, 73.3682
    
    # Простой запрос к Яндекс Погоде без ключа
    url = f"https://api.weather.yandex.ru/v2/forecast?lat={lat}&lon={lon}"
    
    try:
        data = requests.get(url).json()
        temp = data['fact']['temp']
        desc = data['fact']['condition']
        
        # Переводим описание
        conditions = {
            'clear': '☀ Ясно',
            'partly-cloudy': '⛅ Малооблачно', 
            'cloudy': '☁ Облачно',
            'overcast': '☁ Пасмурно',
            'rain': '🌧 Дождь',
            'snow': '❄ Снег'
        }
        desc_ru = conditions.get(desc, desc)
        
        # Одежда
        if temp > 25: wear = "🩳 Шорты, майка"
        elif temp > 15: wear = "👖 Джинсы, футболка" 
        elif temp > 5: wear = "🧥 Куртка, джинсы"
        elif temp > -10: wear = "🧣 Шапка, пуховик"
        else: wear = "🥶 Всё тёплое!"
        
        label.config(text=f"🌡 {temp}°C\n{desc_ru}\n\n👔 {wear}")
    except:
        label.config(text="❌ Нет данных\nПроверь интернет!")

win = tk.Tk()
win.title("Погода Омск")
win.geometry("300x300")

label = tk.Label(win, text="Загрузка...", font=("Arial", 18))
label.pack(expand=True)

tk.Button(win, text="🔄 Обновить", command=update, font=("Arial", 14)).pack(pady=20)

update()
win.mainloop()