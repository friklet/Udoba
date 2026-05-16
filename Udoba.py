import requests
import tkinter as tk

API_KEY = "b6907d289e10d714a6e88b30761fae22"

def update():
    url = f"https://api.openweathermap.org/data/2.5/weather?q=Omsk,RU&appid={API_KEY}&units=metric&lang=ru"
    
    try:
        response = requests.get(url)
        data = response.json()
        
        # Проверка
        if 'main' in data:
            temp = data['main']['temp']
            desc = data['weather'][0]['description']
            
            if temp > 25: wear = "🩳 Шорты, майка"
            elif temp > 15: wear = "👖 Джинсы, футболка"
            elif temp > 5: wear = "🧥 Куртка, джинсы"
            elif temp > -10: wear = "🧣 Шапка, пуховик"
            else: wear = "🥶 Всё тёплое!"
            
            label.config(text=f"🌡 {temp}°C\n📝 {desc}\n\n👔 {wear}")
        else:
            label.config(text=f"❌ Ошибка API:\n{data.get('message', 'неизвестно')}")
    except Exception as e:
        label.config(text=f"❌ Нет интернета!\n{e}")

win = tk.Tk()
win.title("Погода Омск")
win.geometry("300x300")
win.configure(bg="#2c3e50")

title = tk.Label(win, text="🌤 Погода в Омске", font=("Arial", 16, "bold"), bg="#2c3e50", fg="white")
title.pack(pady=15)

label = tk.Label(win, text="Загрузка...", font=("Arial", 18), bg="#2c3e50", fg="white")
label.pack(expand=True)

tk.Button(win, text="🔄 Обновить", command=update, 
          font=("Arial", 14), bg="#3498db", fg="white", width=15, height=2).pack(pady=20)

update()
win.mainloop()