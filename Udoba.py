import requests
import tkinter as tk

def update():
    try:
        url = "https://wttr.in/Omsk?format=j1&lang=ru"
        data = requests.get(url).json()
        
        temp = data['current_condition'][0]['temp_C']
        desc = data['current_condition'][0]['lang_ru'][0]['value']
        wind = data['current_condition'][0]['windspeedKmph']
        humidity = data['current_condition'][0]['humidity']
        
        t = int(temp)
        w = int(wind)
        h = int(humidity)
        
        # Одежда
        if t > 30:
            wear = "🩳 Шорты\n👕 Майка\n🩴 Сандалии\n🧢 Кепка"
        elif t > 25:
            wear = "🩳 Шорты\n👕 Футболка\n👟 Кроссовки\n🕶 Очки"
        elif t > 20:
            wear = "👖 Джинсы\n👕 Футболка\n👟 Кроссовки\n🧥 Ветровка"
        elif t > 15:
            wear = "👖 Джинсы\n👕 Кофта\n🧥 Лёгкая куртка\n👟 Кроссовки"
        elif t > 10:
            wear = "👖 Джинсы\n👕 Свитшот\n🧥 Куртка\n👞 Ботинки"
        elif t > 5:
            wear = "👖 Джинсы\n👕 Свитер\n🧥 Тёплая куртка\n👞 Ботинки\n🧣 Шарф"
        elif t > 0:
            wear = "👖 Тёплые штаны\n👕 Свитер\n🧥 Пуховик\n👢 Ботинки\n🧣 Шапка, шарф\n🧤 Перчатки"
        elif t > -10:
            wear = "👖 Утеплённые штаны\n👕 Термобельё\n👕 Свитер\n🧥 Пуховик\n👢 Зимние ботинки\n🧣 Шапка, шарф\n🧤 Варежки"
        elif t > -20:
            wear = "👖 Зимние штаны\n👕 Термобельё\n👕 Свитер\n🧥 Шуба\n👢 Валенки\n🧣 Шапка, шарф\n🧤 Варежки"
        else:
            wear = "🥶 ВСЁ ТЁПЛОЕ!\n👕 Два свитера\n🧥 Шуба\n👢 Валенки\n🧣 Шапка\n🧤 Рукавицы"
        
        # Советы
        tips = ""
        if w > 30: tips += "💨 Ветрено! Застегнись\n"
        if h > 80: tips += "💧 Влажно! Зонт\n"
        if "дожд" in desc.lower(): tips += "☔ Дождь! Зонт\n"
        if "снег" in desc.lower(): tips += "❄ Снег! Непромокаемая обувь\n"
        
        # Обновляем текст
        weather_info.config(text=f"🌡 {temp}°C")
        desc_info.config(text=f"📝 {desc}")
        wind_info.config(text=f"💨 {wind} км/ч")
        hum_info.config(text=f"💧 {h}%")
        wear_info.config(text=wear)
        if tips:
            tips_info.config(text=tips.strip())
        else:
            tips_info.config(text="")
            
    except:
        weather_info.config(text="❌ Ошибка!")

# ОКНО
win = tk.Tk()
win.title("Погода Омск")
win.geometry("320x500")
win.configure(bg="#1a1a2e")
win.resizable(False, False)

# ЗАГОЛОВОК
tk.Label(win, text="🌤 Омск", font=("Arial", 22, "bold"), 
         bg="#1a1a2e", fg="#e0e0e0").pack(pady=15)

# ЛИНИЯ-РАЗДЕЛИТЕЛЬ
tk.Frame(win, height=1, bg="#333366").pack(fill="x", padx=40)

# ПОГОДА (в ряд)
weather_frame = tk.Frame(win, bg="#1a1a2e")
weather_frame.pack(pady=15)

weather_info = tk.Label(weather_frame, text="--°C", font=("Arial", 36, "bold"), 
                         bg="#1a1a2e", fg="#ff6b6b")
weather_info.pack()

desc_info = tk.Label(win, text="", font=("Arial", 13), 
                      bg="#1a1a2e", fg="#aaaacc")
desc_info.pack()

# ДЕТАЛИ (ветер, влажность)
details_frame = tk.Frame(win, bg="#1a1a2e")
details_frame.pack(pady=10)

wind_info = tk.Label(details_frame, text="", font=("Arial", 11), 
                      bg="#1a1a2e", fg="#8a8aaa")
wind_info.pack(side="left", padx=15)

hum_info = tk.Label(details_frame, text="", font=("Arial", 11), 
                     bg="#1a1a2e", fg="#8a8aaa")
hum_info.pack(side="left", padx=15)

# ЛИНИЯ
tk.Frame(win, height=1, bg="#333366").pack(fill="x", padx=40, pady=10)

# ОДЕЖДА
tk.Label(win, text="👔 Что надеть", font=("Arial", 14, "bold"), 
         bg="#1a1a2e", fg="#4ecdc4").pack(pady=5)

wear_info = tk.Label(win, text="", font=("Arial", 12), 
                      bg="#1a1a2e", fg="#e0e0e0")
wear_info.pack(pady=5)

# СОВЕТЫ
tips_info = tk.Label(win, text="", font=("Arial", 11), 
                      bg="#1a1a2e", fg="#ffa500")
tips_info.pack(pady=5)

# КНОПКА
tk.Button(win, text="🔄 Обновить", command=update, 
          font=("Arial", 12), bg="#333366", fg="#e0e0e0", 
          activebackground="#444488", activeforeground="white",
          relief="flat", width=12, height=1, cursor="hand2").pack(pady=20)

# ЗАПУСК
update()
win.mainloop()