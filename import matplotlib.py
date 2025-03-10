import tkinter as tk

def atbash_cipher(text, lang):
    if lang == "ru":
        alphabet = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
    else: 
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    reversed_alphabet = alphabet[::-1]  
    cipher_map = str.maketrans(alphabet + alphabet.lower(), reversed_alphabet + reversed_alphabet.lower())
    return text.translate(cipher_map)

def encrypt_text():
    lang = language.get()  
    encrypted_text.set(atbash_cipher(entry.get(), lang))  

def update_language():
    lang = language.get()
    if lang == "ru":
        root.title("Мир (Атбаш)")
        encrypt_button.config(text="Шифрлау")
        encrypted_label.config(text="Шифрланған сөз:")
    else:
        root.title("Mir (Atbash)")
        encrypt_button.config(text="Encrypt")
        encrypted_label.config(text="Encrypted text:")
    
root = tk.Tk()
root.title("Мир (Атбаш)")
root.geometry("300x300")
root.resizable(False, False)
language = tk.StringVar(value="ru")
root.config(bg="#ff0080")
entry = tk.Entry(root, font=("Arial", 14), width=30)
entry.pack(pady=10)
encrypt_button = tk.Button(root, text="Шифрлау", command=encrypt_text, font=("Arial", 12))
encrypt_button.pack(pady=5)
encrypted_text = tk.StringVar(value="Шифрланған сөз:")
encrypted_label = tk.Label(root, textvariable=encrypted_text, font=("Arial", 14))
encrypted_label.pack(pady=10)
frame = tk.Frame(root)
frame.pack(pady=5)
tk.Radiobutton(frame, text="🇷🇺 Русский", variable=language, value="ru", command=update_language).pack(side="left", padx=10)
tk.Radiobutton(frame, text="en English", variable=language, value="en", command=update_language).pack(side="left", padx=10)
root.mainloop()