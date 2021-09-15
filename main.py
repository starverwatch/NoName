# Import module
from tkinter import *

# Create object
root = Tk()

# Adjust size
root.geometry("400x400")

# Add image file
bg = PhotoImage(file="sword.png")

# Show image using label
label1 = Label(root, image=bg)
label1.place(x=0, y=0)

# Execute tkinter
root.mainloop()