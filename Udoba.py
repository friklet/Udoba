import requests
import tkinter as tk

def update():
    try:
        d = requests.get("https://wttr.in/Omsk?format=j1&lang=ru").json()['current_condition'][0]
        t, w, h = int(d['temp_C']), int(d['windspeedKmph']), int(d['humidity'])
        
        # Одежда
        if t > 30: wear = "🩳 Шорты, майка, сандалии"
        elif t > 25: wear = "🩳 Шорты, футболка, кроссовки"
        elif t > 20: wear = "👖 Джинсы, футболка, ветровка"
        elif t > 15: wear = "👖 Джинсы, кофта, лёгкая куртка"
        elif t > 10: wear = "👖 Джинсы, свитшот, куртка, ботинки"
        elif t > 5: wear = "👖 Джинсы, свитер, тёплая куртка, шарф"
        elif t > 0: wear = "🧥 Пуховик, шапка, шарф, перчатки"
        elif t > -10: wear = "🧥 Пуховик, термобельё, варежки"
        elif t > -20: wear = "🧥 Шуба, валенки, шапка, варежки"
        else: wear = "🥶 Всё самое тёплое!"
        
        # Советы
        tips = ""
        if w > 30: tips += "💨 Ветрено! "
        if h > 80: tips += "💧 Влажно! "
        if "дожд" in d['lang_ru'][0]['value']: tips += "☔ Зонт! "
        if "снег" in d['lang_ru'][0]['value']: tips += "❄ Снег! "
        
        temp_label.config(text=f"🌡 {t}°C")
        desc_label.config(text=d['lang_ru'][0]['value'])
        wear_label.config(text=wear)
        tips_label.config(text=tips)
    except:
        temp_label.config(text="❌ Ошибка!")

# Окно
win = tk.Tk()
win.title("Погода Омск")
win.geometry("280x350")
win.configure(bg="#1a1a2e")
win.resizable(False, False)

tk.Label(win, text="🌤 Омск", font=("Arial", 20, "bold"), bg="#1a1a2e", fg="#e0e0e0").pack(pady=10)

temp_label = tk.Label(win, text="--°C", font=("Arial", 32, "bold"), bg="#1a1a2e", fg="#ff6b6b")
temp_label.pack()

desc_label = tk.Label(win, text="", font=("Arial", 12), bg="#1a1a2e", fg="#aaaacc")
desc_label.pack(pady=5)

tk.Frame(win, height=1, bg="#333366").pack(fill="x", padx=30, pady=10)

wear_label = tk.Label(win, text="", font=("Arial", 11), bg="#1a1a2e", fg="#e0e0e0")
wear_label.pack(pady=10)

tips_label = tk.Label(win, text="", font=("Arial", 10), bg="#1a1a2e", fg="#ffa500")
tips_label.pack()

tk.Button(win, text="🔄 Обновить", command=update, font=("Arial", 11), 
          bg="#333366", fg="white", relief="flat", cursor="hand2").pack(pady=20)

update()
win.mainloop()