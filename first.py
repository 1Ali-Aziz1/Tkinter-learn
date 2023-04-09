import tkinter as tk

root = tk.Tk()

root.minsize(200, 150)
root.maxsize(800, 600)

label = tk.Label(root, text="Hello, Tkinter!")
label.pack()

def on_button_click():
    label.config(text="Button clicked!")
    
button = tk.Button(root, text="Click me!", command=on_button_click)
button.pack()

root.mainloop()
