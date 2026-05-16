import requests
import tkinter as tk

API_KEY = "b6907d289e10d714a6e88b30761fae22"

def update():
    data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q=Omsk&appid={API_KEY}&units=metric&lang=ru").json()
    temp = data['main']['temp']
    
    if temp > 25: wear = "🩳 Шорты, майка"
    elif temp > 15: wear = "👖 Джинсы, футболка"
    elif temp > 5: wear = "🧥 Куртка, джинсы"
    elif temp > -10: wear = "🧣 Шапка, пуховик"
    else: wear = "🥶 Всё тёплое!"
    
    label.config(text=f"🌡 {temp}°C\n{data['weather'][0]['description']}\n\n👔 {wear}")

win = tk.Tk()
win.title("Погода Омск")
win.geometry("300x300")

label = tk.Label(win, text="Загрузка...", font=("Arial", 18))
label.pack(expand=True)

tk.Button(win, text="🔄 Обновить", command=update, font=("Arial", 14)).pack(pady=20)

update()
win.mainloop()