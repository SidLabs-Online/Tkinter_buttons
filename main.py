import tkinter as tk
from tkinter import ttk
from tkinter import *
from PIL import Image, ImageTk

# root window
root = tk.Tk()
root.geometry('600x600')
root.resizable(False, False)
root.title('Gun Interface')




# exit button
fire_button = ttk.Button(
    root,
    text='Fire',
    command=lambda: root.quit()
)

turn_button = ttk.Button(
    root,
    text='Turn',
    command=lambda: root.quit()
)

fire_button.pack(
    ipadx=5,
    ipady=5,
    expand=True
)

turn_button.pack(
    ipadx=10,
    ipady=10,
    expand=True
)


# Add the image file
bg = ImageTk.PhotoImage(file="img1.png")

# Create a canvas
canvas = Canvas(root,width= 400, height= 400)
canvas.pack(fill= "both", expand=True)

# Display image
canvas.create_image(1,3, image=bg, anchor="nw")


root.mainloop()