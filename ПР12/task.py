import tkinter as tk
from tkinter import messagebox
import requests
import json

def get_repo_info():
    repo_name = entry.get().strip()
    if not repo_name:
        messagebox.showerror("Ошибка", "Введите имя репозитория!")
        return

    try:
        # Запрос к GitHub API
        url = f"https://api.github.com/users/{repo_name}"
        response = requests.get(url)
        
        if response.status_code != 200:
            messagebox.showerror("Ошибка", f"Не удалось получить данные: {response.status_code}")
            return

        data = response.json()

        # Извлечение полей
        result = {
            'company': data.get('company'),
            'created_at': data.get('created_at'),
            'email': data.get('email'),
            'id': data.get('id'),
            'name': data.get('name'),
            'url': data.get('url')
        }

        # Запись в файл
        with open("result.txt", "w") as f:
            f.write(json.dumps(result, indent=4, ensure_ascii=False))

        messagebox.showinfo("Успех", "Данные сохранены в result.txt")

    except Exception as e:
        messagebox.showerror("Ошибка", str(e))

window = tk.Tk()
window.title("Информация о репозитории")
window.geometry("300x100")

tk.Label(window, text="Введите имя репозитория").pack(pady=5)

entry = tk.Entry(window, width=40)
entry.pack(pady=5)

btn = tk.Button(window, text="Получить данные", command=get_repo_info)
btn.pack(pady=10)

window.mainloop()
