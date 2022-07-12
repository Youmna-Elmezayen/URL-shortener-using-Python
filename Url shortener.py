import tkinter as tk
import pyshorteners
import pyperclip


def showError():
    error_label.pack()

def hideError():
    error_label.pack_forget()

def copy(url):
    pyperclip.copy(url)
    spam = pyperclip.paste()
    copied_label = tk.Label(window, text="Link copied!", font=("New", 13))
    copied_label.pack(pady=10)

def lengthen():
    try:
        hideError()
        type_big = pyshorteners.Shortener()
        long_url = type_big.tinyurl.expand(text_field.get())
        lengthened_url = tk.Label(window, text=long_url, font=("New", 13))
        lengthened_url.pack(pady=10)
        copy_btn = tk.Button(window, text="Copy URL", command= lambda: copy(long_url))
        copy_btn.pack()
    except:
        showError()

def shorten():
    try:
        hideError()
        type_tiny = pyshorteners.Shortener()
        short_url = type_tiny.tinyurl.short(text_field.get())
        shortened_url = tk.Label(window, text=short_url, font=("New", 13))
        shortened_url.pack(pady=10)
        copy_btn = tk.Button(window, text="Copy URL", command= lambda: copy(short_url))
        copy_btn.pack()
    except:
        showError()

window = tk.Tk()
window.geometry('600x400+50+50')
window.title('URL shortener')
error_label = tk.Label(window, text="Link is not in the correct format", font=("New", 10),fg="red")

title = tk.Label(window, text="URL Shortener", font=("New", 22))
title.pack()
field_title = tk.Label(window, text="Enter URL:", font=("New", 16))
field_title.place(x=20, y=90)
text_field = tk.Entry(window, width=80, border=5)
text_field.pack(padx=50, pady=50)

lengthen_url = tk.Button(window, text="Lengthen URL",command=lengthen)
lengthen_url.pack(side=tk.BOTTOM, pady = 20)
shorten_url = tk.Button(window, text="Shorten URL", command=shorten)
shorten_url.pack(side=tk.BOTTOM)
window.mainloop()