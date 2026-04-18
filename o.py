import tkinter as tk
from tkinter import messagebox
import json
import os

def load_tasks():
    """Загружает задачи из файла tasks.json. Если файла нет или он повреждён, возвращает пустой список."""
    try:
        if os.path.exists("tasks.json"):
            with open("tasks.json", "r", encoding="utf-8") as file:
                return json.load(file)
        else:
            return []
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_tasks(task_list):
    """Сохраняет список задач в файл tasks.json с форматированием."""
    with open("tasks.json", "w", encoding="utf-8") as file:
        json.dump(task_list, file, ensure_ascii=False, indent=4)

def add_task():
    """Добавляет новую задачу в список."""
    task = entry_task.get().strip()
    if task:
        tasks.append(task)
        update_listbox()
        save_tasks(tasks)
        entry_task.delete(0, tk.END)
    else:
        messagebox.showwarning("Предупреждение", "Введите текст задачи.")

def remove_task():
    """Удаляет выбранную задачу из списка."""
    selected = task_listbox.curselection()
    if selected:
        index = selected[0]
        tasks.pop(index)
        update_listbox()
        save_tasks(tasks)
    else:
        messagebox.showwarning("Предупреждение", "Выберите задачу для удаления")

def update_listbox():
    """Обновляет отображение списка задач в Listbox."""
    task_listbox.delete(0, tk.END)
    for task in tasks:
        task_listbox.insert(tk.END, task)

# Создаём главное окно
root = tk.Tk()
root.title("Список задач")
root.geometry("400x300")
root.resizable(False, False)

# Загружаем задачи при запуске
tasks = load_tasks()

# Listbox для отображения задач
task_listbox = tk.Listbox(root, width=50, height=10, font=("Arial", 10))
task_listbox.pack(pady=10)

# Поле ввода для новой задачи
entry_task = tk.Entry(root, font=("Arial", 12), width=40)
entry_task.pack(pady=5)

# Кнопка добавления задачи
add_button = tk.Button(
    root,
    text="Добавить задачу",
    command=add_task,
    bg="#4CAF50",
    fg="white",
    font=("Arial", 10),
    width=15
)
add_button.pack(pady=5)

# Кнопка удаления выбранной задачи
remove_button = tk.Button(
    root,
    text="Удалить выбранную",
    command=remove_task,
    bg="#f44336",
    fg="white",
    font=("Arial", 10),
    width=15
)
remove_button.pack(pady=5)

# Обновляем Listbox при запуске (показываем загруженные задачи)
update_listbox()

# Запускаем главный цикл обработки событий
root.mainloop()
