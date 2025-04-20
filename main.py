import tkinter as tk
from tkinter import scrolledtext
import sqlite3
from statistics import mean

def load_user_data():
    try:
        conn = sqlite3.connect('user_data.db')
        cursor = conn.cursor()
        cursor.execute("SELECT id, name, age, email FROM users")
        data = cursor.fetchall()
        conn.close()
        return data
    except sqlite3.Error as e:
        return None

def display_analysis(data, text_area):
    text_area.delete(1.0, tk.END)
    
    if not data:
        text_area.insert(tk.END, "No data found or error occurred.\n")
        return
    
    total_users = len(data)
    average_age = mean([row[2] for row in data]) if data else 0
    
    text_area.insert(tk.END, f"User Data Analysis\n{'-'*30}\n")
    text_area.insert(tk.END, f"Total Users: {total_users}\n")
    text_area.insert(tk.END, f"Average Age: {average_age:.1f}\n\n")
    
    text_area.insert(tk.END, "User Details:\n")
    for row in data:
        text_area.insert(tk.END, f"ID: {row[0]}, Name: {row[1]}, Age: {row[2]}, Email: {row[3]}\n")

root = tk.Tk()
root.title("User Data Analysis")
root.geometry("1000x750")

text_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=80, height=30, font=("Arial", 12))
text_area.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

user_data = load_user_data()
display_analysis(user_data, text_area)

root.mainloop()