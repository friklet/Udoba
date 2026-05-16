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
        
        # Одежда с учётом ветра и влажности
        if t > 30:
            wear = "🩳 Шорты\n👕 Майка/футболка\n🩴 Сандалии\n🧢 Кепка/шляпа"
        elif t > 25:
            wear = "🩳 Шорты\n👕 Футболка\n👟 Кроссовки\n🕶 Очки"
        elif t > 20:
            wear = "👖 Джинсы/шорты\n👕 Футболка/рубашка\n👟 Кроссовки\n🧥 Ветровка с собой"
        elif t > 15:
            wear = "👖 Джинсы/брюки\n👕 Футболка\n🧥 Лёгкая куртка\n👟 Кроссовки"
        elif t > 10:
            wear = "👖 Джинсы\n👕 Кофта/свитшот\n🧥 Куртка\n👟 Кроссовки/ботинки"
        elif t > 5:
            wear = "👖 Джинсы\n👕 Свитер/толстовка\n🧥 Тёплая куртка\n👞 Ботинки\n🧣 Шарф"
        elif t > 0:
            wear = "👖 Тёплые штаны\n👕 Свитер\n🧥 Пуховик\n👢 Ботинки\n🧣 Шапка, шарф\n🧤 Перчатки"
        elif t > -10:
            wear = "👖 Утеплённые штаны\n👕 Термобельё\n👕 Свитер\n🧥 Пуховик\n👢 Зимние ботинки\n🧣 Шапка, шарф\n🧤 Варежки"
        elif t > -20:
            wear = "👖 Зимние штаны\n👕 Термобельё\n👕 Тёплый свитер\n🧥 Шуба/пуховик\n👢 Унты/валенки\n🧣 Шапка, шарф\n🧤 Тёплые варежки"
        else:
            wear = "🥶 ВСЁ САМОЕ ТЁПЛОЕ!\n👕 Два свитера\n🧥 Шуба/пуховик\n👢 Валенки\n🧣 Шапка, шарф\n🧤 Меховые рукавицы"
        
        # Добавляем советы по погоде
        tips = ""
        if w > 30:
            tips += "\n💨 ВЕТЕР! Застегнись!"
        if h > 80:
            tips += "\n💧 Влажно - возьми зонт!"
        if "дожд" in desc.lower():
            tips += "\n☔ Зонт обязательно!"
        if "снег" in desc.lower():
            tips += "\n❄ Снег - обувь непромокаемая!"
        
        label.config(text=f"🌡 {temp}°C | 💨 {wind} км/ч | 💧 {h}%\n📝 {desc}\n\n👔 ЧТО НАДЕТЬ:\n{wear}{tips}")
        
    except:
        label.config(text="❌ Ошибка загрузки!")

win = tk.Tk()
win.title("Погода Омск")
win.geometry("350x450")
win.configure(bg="#2c3e50")

tk.Label(win, text="🌤 ПОГОДА В ОМСКЕ", font=("Arial", 18, "bold"), 
         bg="#2c3e50", fg="white").pack(pady=15)

label = tk.Label(win, text="Загрузка...", font=("Arial", 14), 
                 bg="#2c3e50", fg="white", justify="left")
label.pack(pady=20)

tk.Button(win, text="🔄 Обновить", command=update, 
          font=("Arial", 14, "bold"), bg="#3498db", fg="white", 
          width=15, height=2).pack(pady=20)

update()
win.mainloop()