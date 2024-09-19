import tkinter as tk # gui
from organizeFiles import create_dir_structure

root = tk.Tk() 
root.title("file organizer")
root.geometry("500x450")

def show_input():
    user_input = entry.get() # store the text entered by user in entry widget to user_input
    
    print("user input: ", user_input)
    create_dir_structure(user_input)

label = tk.Label(root, text = "Enter folder address: ")
label.pack(pady=10)
# creating a entry widget. single line text input field.
entry = tk.Entry(root,width=80)
entry.pack(pady=5)
button = tk.Button(root,text="submit", command=show_input)
button.pack(pady=10)

root.mainloop()

# design a file organizer gui app 

# next class how to create executable


