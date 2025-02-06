import tkinter
from tkinter import *
from tkinter import messagebox, filedialog
from textblob import TextBlob
import pyttsx3
import language_tool_python

root = Tk()
root.title("Spelling and Grammar Checker")
root.geometry("700x600")
root.configure(background="#dae6f6")

engine = pyttsx3.init()
tool = language_tool_python.LanguageTool('en-US')

def check_spelling_and_grammar():
    text = text_input.get("1.0", "end-1c")
    if not text:
        messagebox.showwarning("Input Error", "Please enter text to check spelling and grammar.")
        return
    
    # Spelling correction
    a = TextBlob(text)
    corrected_text = str(a.correct())
    
    # Grammar correction
    matches = tool.check(corrected_text)
    corrected_text = language_tool_python.utils.correct(corrected_text, matches)
    
    cs = Label(root, text="Corrected text is:", font=("poppins", 20), bg="#dae6f6", fg="#364971")
    cs.place(x=100, y=250)
    spell.config(text=corrected_text)

def clear_text():
    text_input.delete("1.0", END)
    spell.config(text="")

def copy_to_clipboard():
    corrected_text = spell.cget("text")
    if corrected_text:
        root.clipboard_clear()
        root.clipboard_append(corrected_text)
        root.update()
        messagebox.showinfo("Copied", "Corrected text copied to clipboard!")

def save_to_file():
    corrected_text = spell.cget("text")
    if corrected_text:
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
        if file_path:
            with open(file_path, "w") as file:
                file.write(corrected_text)
            messagebox.showinfo("Success", "File saved successfully!")

def read_aloud():
    corrected_text = spell.cget("text")
    if corrected_text:
        engine.say(corrected_text)
        engine.runAndWait()

heading = Label(root, text="Spelling and Grammar Checker", font=("Trebuchet MS", 30, "bold"), bg="#dae6f6", fg="#364971")
heading.pack(pady=(50, 0))

text_input = Text(root, height=10, width=50, font=("poppins", 15), bg="white", border=2)
text_input.pack(pady=10)
text_input.focus()

button_frame = Frame(root, bg="#dae6f6")
button_frame.pack(pady=10)

check_button = Button(button_frame, text="Check", font=("arial", 20, "bold"), fg="white", bg="red", command=check_spelling_and_grammar)
check_button.grid(row=0, column=0, padx=10)

clear_button = Button(button_frame, text="Clear", font=("arial", 20, "bold"), fg="white", bg="blue", command=clear_text)
clear_button.grid(row=0, column=1, padx=10)

copy_button = Button(button_frame, text="Copy", font=("arial", 20, "bold"), fg="white", bg="green", command=copy_to_clipboard)
copy_button.grid(row=0, column=2, padx=10)

save_button = Button(button_frame, text="Save", font=("arial", 20, "bold"), fg="white", bg="purple", command=save_to_file)
save_button.grid(row=0, column=3, padx=10)

read_button = Button(button_frame, text="Read Aloud", font=("arial", 20, "bold"), fg="white", bg="orange", command=read_aloud)
read_button.grid(row=0, column=4, padx=10)

spell = Label(root, font=("poppins", 20), bg="#dae6f6", fg="#364971", wraplength=600, justify=LEFT)
spell.place(x=100, y=300)

root.mainloop()