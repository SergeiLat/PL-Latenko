import tkinter as tk
from tkinter import ttk, messagebox, filedialog

# Главное окно
window = tk.Tk()
window.title("Латенко С. О.")
window.geometry("500x400")

# Вкладки
notebook = ttk.Notebook(window)
notebook.pack(expand=True, fill="both", padx=10, pady=10)

# 1. Калькулятор
frame_calc = ttk.Frame(notebook)
notebook.add(frame_calc, text="Калькулятор")

# Поля ввода
entry1 = ttk.Entry(frame_calc, width=10)
entry2 = ttk.Entry(frame_calc, width=10)
entry1.grid(row=0, column=0, padx=5, pady=20)
entry2.grid(row=0, column=2, padx=5, pady=20)

# Выпадающий список операций
operation = ttk.Combobox(frame_calc, values=["+", "-", "*", "/"], width=5)
operation.current(0)
operation.grid(row=0, column=1, padx=5)

# Результат
result_label = ttk.Label(frame_calc, text="Результат: ")
result_label.grid(row=1, column=0, columnspan=3, pady=10)

def calculate():
    try:
        a = float(entry1.get())
        b = float(entry2.get())
        op = operation.get()
        if op == "+":
            res = a + b
        elif op == "-":
            res = a - b
        elif op == "*":
            res = a * b
        elif op == "/":
            if b != 0:
                res = a / b
            else:
                res = "Ошибка: деление на 0"
        result_label.config(text=f"Результат: {res}")
    except ValueError:
        result_label.config(text="Ошибка: введите числа")

btn_calc = ttk.Button(frame_calc, text="Вычислить", command=calculate)
btn_calc.grid(row=2, column=0, columnspan=3, pady=10)

# 2. Чекбоксы
frame_check = ttk.Frame(notebook)
notebook.add(frame_check, text="Выбор")

var1 = tk.BooleanVar()
var2 = tk.BooleanVar()
var3 = tk.BooleanVar()

check1 = ttk.Checkbutton(frame_check, text="Первый", variable=var1)
check2 = ttk.Checkbutton(frame_check, text="Второй", variable=var2)
check3 = ttk.Checkbutton(frame_check, text="Третий", variable=var3)

check1.pack(pady=5)
check2.pack(pady=5)
check3.pack(pady=5)

def show_choice():
    if var1.get() & var2.get() & var3.get():
        messagebox.showinfo("Выбор", "Вы выбрали все варианты")
    elif var3.get() & var1.get():
        messagebox.showinfo("Выбор", "Вы выбрали первый и третий варианты")
    elif var3.get() & var2.get():
        messagebox.showinfo("Выбор", "Вы выбрали второй и третий варианты")
    elif var1.get() & var2.get():
        messagebox.showinfo("Выбор", "Вы выбрали первый и второй варианты")
    elif var1.get():
        messagebox.showinfo("Выбор", "Вы выбрали первый вариант")
    elif var2.get():
        messagebox.showinfo("Выбор", "Вы выбрали второй вариант")
    elif var3.get():
        messagebox.showinfo("Выбор", "Вы выбрали третий вариант")
    else:
        messagebox.showinfo("Выбор", "Вы ничего не выбрали")

btn_choice = ttk.Button(frame_check, text="Показать выбор", command=show_choice)
btn_choice.pack(pady=10)

# 3. Работа с текстом
frame_text = ttk.Frame(notebook)
notebook.add(frame_text, text="Текст")

text_area = tk.Text(frame_text, wrap="word")
text_area.pack(expand=True, fill="both", padx=10, pady=10)

def load_text():
    file_path = filedialog.askopenfilename(
        title="Выберите текстовый файл",
        filetypes=[("Текстовые файлы", "*.txt"), ("Все файлы", "*.*")]
    )
    if file_path:
        with open(file_path, "r") as f:
            content = f.read()
            text_area.delete("1.0", tk.END)
            text_area.insert(tk.END, content)

# Меню
menu_bar = tk.Menu(window)
window.config(menu=menu_bar)

file_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Файл", menu=file_menu)
file_menu.add_command(label="Загрузить текст", command=load_text)
file_menu.add_separator()
file_menu.add_command(label="Выход", command=window.quit)

window.mainloop()
