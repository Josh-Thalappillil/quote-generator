import requests
import tkinter as ttk
import ttkbootstrap as ttk

api_URL = "https://api.quotable.io/random"

def fetch_quote():
    response = requests.get(api_URL)
    data = response.json()
    quote = data["content"]
    author = data["author"]
    tags = data["tags"]

    
    return quote, author, tags

def update_quote():
    quote, author, tags = fetch_quote()
    tags_str = ', '.join(tags)
    quote_label.config(text=quote)
    author_label.config(text=f"~ {author}")
    tags_label.config(text=f"Category: {tags_str}")


root = ttk.Window(themename="pulse")
root.title("Quote Generator")
root.geometry("800x350")

frame = ttk.Frame(root)
frame.pack(padx = 30, pady = 40)

quote_label = ttk.Label(frame, text="", font=("Helvetica", 16), wraplength = 650)
quote_label.pack()

author_label = ttk.Label(frame, text="", font=("Helvetica", 12, "bold"))
author_label.pack(pady = 10)

tags_label = ttk.Label(frame, text="", font=("Helvetica", 12)) 
tags_label.pack(pady = 10)

style = ttk.Style()
style.configure("TButton", font=("Helvetica", 12))
ttk.Button(frame, text="Get Quote", style="TButton", command = update_quote).pack(pady = 20)
root.mainloop()




