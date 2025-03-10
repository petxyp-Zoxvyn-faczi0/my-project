import tkinter as tk
from tkinter import ttk

def atbash_cipher_with_process(text: str, alphabet: str) -> str:
    reversed_alphabet = alphabet[::-1]
    mapping = str.maketrans(alphabet + alphabet.lower(), reversed_alphabet + reversed_alphabet.lower())
    
    process = []
    for char in text:
        if char in alphabet + alphabet.lower():
            translated_char = char.translate(mapping)
            process.append(f"{char} -> {translated_char}")
        else:
            process.append(f"{char} (no change)")
    
    encrypted_text = text.translate(mapping)
    return encrypted_text, "\n".join(process)

def open_cipher_window(language):
    if language == "EN":
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        window_title = "Шифр Атбаш"
        input_label_text = "Введите текст:"
        process_label_text = "Процесс:"
        encrypt_button_text = "Зашифровать"
        decrypt_button_text = "Дешифровать"
        result_label_text = "Результат:"
    else:
        alphabet = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
        window_title = "Шифр Атбаш"
        input_label_text = "Введите текст:"
        process_label_text = "Процесс:"
        encrypt_button_text = "Зашифровать"
        decrypt_button_text = "Дешифровать"
        result_label_text = "Результат:"
    
    def encrypt_text():
        input_text = entry.get()
        encrypted_text, process_text = atbash_cipher_with_process(input_text, alphabet)
        result_label.config(text=f"{result_label_text} {encrypted_text}")
        process_label.config(text=f"{process_label_text}\n{process_text}")
    
    def decrypt_text():
        input_text = entry.get()
        decrypted_text, process_text = atbash_cipher_with_process(input_text, alphabet)
        result_label.config(text=f"{result_label_text} {decrypted_text}")
        process_label.config(text=f"{process_label_text}\n{process_text}")
    
    root.destroy()
    cipher_window = tk.Tk()
    cipher_window.title(window_title)
    
    alphabet_label = ttk.Label(cipher_window, text=f"{alphabet}", font=("Arial", 14, "bold"))
    alphabet_label.pack()
    
    entry_label = ttk.Label(cipher_window, text=input_label_text)
    entry_label.pack()
    entry = ttk.Entry(cipher_window, width=40)
    entry.pack()
    
    encrypt_button = ttk.Button(cipher_window, text=encrypt_button_text, command=encrypt_text)
    encrypt_button.pack()
    decrypt_button = ttk.Button(cipher_window, text=decrypt_button_text, command=decrypt_text)
    decrypt_button.pack()
    
    result_label = ttk.Label(cipher_window, text=result_label_text)
    result_label.pack()
    
    process_label = ttk.Label(cipher_window, text=process_label_text, justify="left")
    process_label.pack()

def choose_language():
    global root
    root = tk.Tk()
    root.title("Выбор языка")
    
    language_var = tk.StringVar()
    
    label = ttk.Label(root, text="Выберите язык:")
    label.pack()
    
    button_en = ttk.Button(root, text="English", command=lambda: open_cipher_window("EN"))
    button_en.pack()
    
    button_ru = ttk.Button(root, text="Русский", command=lambda: open_cipher_window("RU"))
    button_ru.pack()
    
    root.mainloop()


choose_language()