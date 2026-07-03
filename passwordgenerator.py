# Importing required modules 
import tkinter as tk
import random
import string

# Create a function to generate a passwords
def generate_password():
    try:
        pwd_lenght = int(entry.get())
        
        if pwd_lenght < 5 or pwd_lenght > 20:
            output_lbl.config(text="Password length must be between 5 and 20!")
            return
        
        safe_symbols = "!@#$%^&*()_+-=[]{}|;:,.<>?/~`"
        characters = string.ascii_letters + string.digits + safe_symbols
        password = ''.join(random.choice(characters) for _ in range(pwd_lenght))
        
        entry.delete(0, tk.END)
        entry.insert(0, password)
        output_lbl.config(text="password generated successfully!")
        
    except ValueError:
        output_lbl.config(text="Please enter a valid number!")

# Create the main window
root = tk.Tk()
root.title("Password Generator")
root.geometry("500x400")
root.config(bg="navy")

# Create a Label
lbl = tk.Label(root, text="Enter Length", font=("Arial", 16), bg="navy", fg="white")
lbl.pack(pady=10)

# Create an Entry Box
entry = tk.Entry( root, font=("Arial", 16), justify="right")
entry.insert( index=0, string= "8")
entry.pack(pady=10)

# Create an Output Label
output_lbl = tk.Label(root, text= " ", font=("Arial", 16), bg="navy", fg="white")
output_lbl.pack(pady=20)

# Create a Button
btn = tk.Button(root, text="Generate", font=("Arial", 16), bg="yellow", fg="black", command=generate_password)
btn.pack(pady=10)

# Run the main loop
root.mainloop()