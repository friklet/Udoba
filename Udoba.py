from PIL import Image, ImageFilter, ImageTk
import tkinter as tk
from tkinter import filedialog

# 1. ОКНО
win = tk.Tk()
win.title("🎨 Фотошоп")
win.geometry("700x550")

# 2. КАРТИНКИ (пустые пока)
original = None  # оригинал
working = None   # меняется

# 3. ФУНКЦИИ (всего 3!)
def open_pic():
    """Открыть файл"""
    global original, working
    path = filedialog.askopenfilename(filetypes=[("Картинки", "*.jpg *.png *.jpeg *.bmp")])
    if path:
        original = Image.open(path)
        working = original.copy()
        show()

def save_pic():
    """Сохранить"""
    global working
    path = filedialog.asksaveasfilename(defaultextension=".jpg")
    if path:
        working.save(path)
        hint.config(text="✅ Сохранено!")

def do_effect(code):
    """Применить эффект (1-размытие, 2-контур, 3-резкость, 4-тиснение, 5-Ч/Б)"""
    global working
    if working is None:
        hint.config(text="❌ Сначала открой фото!")
        return
    
    effects = {
        1: ImageFilter.BLUR,      # размытие
        2: ImageFilter.CONTOUR,   # контур
        3: ImageFilter.SHARPEN,   # резкость
        4: ImageFilter.EMBOSS,    # тиснение
        5: None                   # Ч/Б
    }
    
    if code == 5:
        working = working.convert('L')  # черно-белое
        hint.config(text="✅ Черно-белое")
    else:
        working = working.filter(effects[code])
        names = {1: "Размытие", 2: "Контур", 3: "Резкость", 4: "Тиснение"}
        hint.config(text=f"✅ {names[code]}")
    
    show()

def rotate():
    """Поворот"""
    global working
    if working:
        working = working.rotate(90, expand=True)
        hint.config(text="✅ Повернуто на 90°")
        show()

def reset():
    """Отмена всего"""
    global working
    if original:
        working = original.copy()
        hint.config(text="🔄 Сброшено!")
        show()

def show():
    """Показать картинку"""
    global working
    img = working.copy()
    img.thumbnail((450, 350))  # уменьшаем для экрана
    photo = ImageTk.PhotoImage(img)
    label.config(image=photo)
    label.image = photo  # сохраняем ссылку

# 4. КНОПКИ (просто колонка слева)
tk.Button(win, text="📂 Открыть", command=open_pic, width=14, bg="lightblue").place(x=10, y=10)
tk.Button(win, text="💾 Сохранить", command=save_pic, width=14, bg="lightgreen").place(x=10, y=50)

tk.Label(win, text="— Эффекты —").place(x=10, y=90)

tk.Button(win, text="1. Размытие", command=lambda: do_effect(1), width=14).place(x=10, y=120)
tk.Button(win, text="2. Контур", command=lambda: do_effect(2), width=14).place(x=10, y=155)
tk.Button(win, text="3. Резкость", command=lambda: do_effect(3), width=14).place(x=10, y=190)
tk.Button(win, text="4. Тиснение", command=lambda: do_effect(4), width=14).place(x=10, y=225)
tk.Button(win, text="5. Ч/Б", command=lambda: do_effect(5), width=14).place(x=10, y=260)

tk.Label(win, text="— Действия —").place(x=10, y=300)
tk.Button(win, text="↻ Поворот", command=rotate, width=14, bg="yellow").place(x=10, y=330)
tk.Button(win, text="🔄 Сброс", command=reset, width=14, bg="orange").place(x=10, y=365)

# 5. ПОДСКАЗКА
hint = tk.Label(win, text="👋 Открой фото и жми эффекты!", font=("Arial", 10), fg="gray")
hint.place(x=130, y=480)

# 6. МЕСТО ДЛЯ ФОТО
label = tk.Label(win, text="📷 Здесь будет фото", font=("Arial", 12))
label.place(x=130, y=10)

win.mainloop()