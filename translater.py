from tkinter import *
from tkinter import ttk, messagebox
from deep_translator import GoogleTranslator

def translate_text():
    text = text_input.get("1.0", "end-1c")
    source_language = source_language_var.get()
    target_language = target_language_var.get()
    
    if not text:
        messagebox.showwarning("Input Error", "Please enter text to translate.")
        return
    
    try:
        translated_text = GoogleTranslator(source=source_language, target=target_language).translate(text)
        result_label.config(text=translated_text)
        status_label.config(text="Translation successful", fg="green")
    except Exception as e:
        messagebox.showerror("Translation Error", str(e))
        status_label.config(text="Translation failed", fg="red")

def clear_text():
    text_input.delete("1.0", END)
    result_label.config(text="")
    status_label.config(text="Cleared", fg="blue")

root = Tk()
root.title("Google Translator")
root.geometry("1080x600")
root.resizable(False, False)
root.configure(background="white")

# Title label
title_label = Label(root, text="Google Translator", font=("Arial", 24, "bold"), bg="white")
title_label.pack(pady=10)

# Frame for input and options
frame = Frame(root, bg="white")
frame.pack(pady=10)

# Text input with scrollbar
text_input_frame = Frame(frame, bg="white")
text_input_frame.pack(side=LEFT, padx=10)
text_input_scrollbar = Scrollbar(text_input_frame)
text_input_scrollbar.pack(side=RIGHT, fill=Y)
text_input = Text(text_input_frame, height=10, width=50, yscrollcommand=text_input_scrollbar.set)
text_input.pack()
text_input_scrollbar.config(command=text_input.yview)

# Source language selection
source_language_var = StringVar(value='en')  # Default source language is English
source_language_label = Label(frame, text="Select Source Language:", bg="white")
source_language_label.pack(pady=5)
source_language_dropdown = ttk.Combobox(frame, textvariable=source_language_var)
source_language_dropdown['values'] = ['en', 'es', 'fr', 'de', 'zh-CN', 'ja', 'hi']  # Add more languages as needed
source_language_dropdown.pack(pady=5)

# Target language selection
target_language_var = StringVar(value='hi')  # Default target language is Hindi
target_language_label = Label(frame, text="Select Target Language:", bg="white")
target_language_label.pack(pady=5)
target_language_dropdown = ttk.Combobox(frame, textvariable=target_language_var)
target_language_dropdown['values'] = ['en', 'es', 'fr', 'de', 'zh-CN', 'ja', 'hi']  # Add more languages as needed
target_language_dropdown.pack(pady=5)

# Translate button
translate_button = Button(frame, text="Translate", command=translate_text)
translate_button.pack(pady=10)

# Clear button
clear_button = Button(frame, text="Clear", command=clear_text)
clear_button.pack(pady=10)

# Result label
result_label = Label(root, text="", bg="white", wraplength=500, font=("Arial", 12))
result_label.pack(pady=10)

# Status bar
status_label = Label(root, text="", bg="white", font=("Arial", 10))
status_label.pack(pady=5)

root.mainloop()