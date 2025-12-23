import tkinter as tk
from tkinter import messagebox
import Task_Code


def submit_form():
    
    name = name_entry.get()
    email = email_entry.get()
    cnic = cnic_entry.get()
    messagebox.showinfo("Form Submitted", f"Name: {name}\nCnic: {cnic}\nEmail: {email}")
    
    Task_Code.Deluge_function(name, cnic, email)

# Create the main window
root = tk.Tk()
root.title("Mastermind Input Form")
root.geometry("300x200")


# Name label and entry
tk.Label(root, text="Student Name").grid(row=0, column=0, padx=10, pady=5, sticky="e")
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1, padx=10, pady=5)

# CNIC label and entry
tk.Label(root, text="Student CNIC").grid(row=1, column=0, padx=10, pady=5, sticky="e")
cnic_entry = tk.Entry(root)
cnic_entry.grid(row=1, column=1, padx=10, pady=5)

# Email label and entry
tk.Label(root, text="Email").grid(row=2, column=0, padx=10, pady=5, sticky="e")
email_entry = tk.Entry(root)
email_entry.grid(row=2, column=1, padx=10, pady=5)


# Submit button
submit_btn = tk.Button(root, text="Submit", command=submit_form)
submit_btn.grid(row=3, column=0, columnspan=2, pady=10)

# Run the application
root.mainloop()