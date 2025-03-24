import tkinter as tk
import os

# Ana pencere oluştur
root = tk.Tk()
root.title("To-Do List Uygulaması")
root.geometry("400x500")

# Görev listesi için liste kutusu
listbox_tasks = tk.Listbox(root, width=50, height=15)
listbox_tasks.pack(pady=10)

# Görev ekleme fonksiyonu
def add_task():
    task = entry_task.get()
    if task:
        listbox_tasks.insert(tk.END, task)
        entry_task.delete(0, tk.END)

# Görev silme fonksiyonu
def delete_task():
    try:
        selected_task_index = listbox_tasks.curselection()[0]
        listbox_tasks.delete(selected_task_index)
    except IndexError:
        pass

# Görevi tamamlandı olarak işaretleme fonksiyonu
def complete_task():
    try:
        selected_task_index = listbox_tasks.curselection()[0]
        task_text = listbox_tasks.get(selected_task_index)

        if task_text.startswith("✔ "):
            listbox_tasks.delete(selected_task_index)
            listbox_tasks.insert(selected_task_index, task_text[2:])
        else:
            listbox_tasks.delete(selected_task_index)
            listbox_tasks.insert(selected_task_index, "✔ " + task_text)
    except IndexError:
        pass

# Görevleri dosyaya kaydetme fonksiyonu
def save_tasks():
    with open("tasks.txt", "w", encoding="utf-8") as file:
        tasks = listbox_tasks.get(0, tk.END)
        for task in tasks:
            file.write(task + "\n")

# Görevleri açılışta yükleme fonksiyonu
def load_tasks():
    if os.path.exists("tasks.txt"):
        with open("tasks.txt", "r", encoding="utf-8") as file:
            tasks = file.readlines()
            for task in tasks:
                listbox_tasks.insert(tk.END, task.strip())

# Kullanıcı arayüzü bileşenleri
entry_task = tk.Entry(root, width=40)
entry_task.pack(pady=5)

btn_add = tk.Button(root, text="Görev Ekle", command=add_task)
btn_add.pack(pady=5)

btn_delete = tk.Button(root, text="Seçili Görevi Sil", command=delete_task)
btn_delete.pack(pady=5)

btn_complete = tk.Button(root, text="Tamamlandı Olarak İşaretle", command=complete_task)
btn_complete.pack(pady=5)

btn_save = tk.Button(root, text="Görevleri Kaydet", command=save_tasks)
btn_save.pack(pady=5)

# Uygulama açıldığında görevleri yükle
load_tasks()

# Pencereyi çalıştır
root.mainloop()