import requests
import tkinter as tk

def update():
    try:
        # Получаем погоду Омска с бесплатного API без ключа
        url = "https://wttr.in/Omsk?format=j1&lang=ru"
        data = requests.get(url).json()
        
        # Данные
        temp = data['current_condition'][0]['temp_C']
        desc = data['current_condition'][0]['lang_ru'][0]['value']
        feels = data['current_condition'][0]['FeelsLikeC']
        wind = data['current_condition'][0]['windspeedKmph']
        
        # Одежда
        t = int(temp)
        if t > 25: wear = "🩳 Шорты, майка"
        elif t > 15: wear = "👖 Джинсы, футболка"
        elif t > 5: wear = "🧥 Куртка, джинсы"
        elif t > -10: wear = "🧣 Шапка, пуховик"
        else: wear = "🥶 Всё тёплое!"
        
        label.config(text=f"🌡 {temp}°C\n📝 {desc}\n💨 Ветер: {wind} км/ч\n\n👔 {wear}")
    except:
        label.config(text="❌ Ошибка!")

win = tk.Tk()
win.title("Погода Омск")
win.geometry("300x300")

label = tk.Label(win, text="Загрузка...", font=("Arial", 18))
label.pack(expand=True)

tk.Button(win, text="🔄 Обновить", command=update, font=("Arial", 14)).pack(pady=20)

update()
win.mainloop()