import tkinter as tk
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from filters import *

      
# Create a tk window
root = tk.Tk()

# Give the area of the window
root.geometry("1200x900")

# Add title
root.title("Filter.io")

# Show users what they can do
instruction = tk.Label(root, text="Filter Image", font=('Arial', 18))
instruction.pack(padx=20, pady=20)

# Ask for the image
file_path = tk.Entry(root)
file_path.pack(padx=20, pady=20)

#create button frame
btnframe = tk.Frame(root)
btnframe.pack(side='left', padx=20)

# Create blur button
blur = tk.Button(btnframe, text='Blur', font=('Arial', 18), command= blur)
blur.grid(row=0, column=0, padx=2, pady=0)

# Create grayscale button
grayscale = tk.Button(btnframe, text='Grayscale', font=('Arial', 18), command= grayscale)
grayscale.grid(row=0, column=1, padx=2)

# Create reflect button
reflect = tk.Button(btnframe, text='Reflect', font=('Arial', 18), command= reflect)
reflect.grid(row=1, column=0, padx=2)

# Create contour button
contour = tk.Button(btnframe, text='Contour', font=('Arial', 18), command= contour)
contour.grid(row=1, column=1, padx=2)

# Create emboss button
emboss = tk.Button(btnframe, text='Emboss', font=('Arial', 18), command= emboss)
emboss.grid(row=2, column=0, padx=2)

# Create sharpen button
sharpen = tk.Button(btnframe, text='Sharpen', font=('Arial', 18), command= sharpen)
sharpen.grid(row=2, column=1, padx=2)

# Create smoothen button
smoothen = tk.Button(btnframe, text='Smoothen', font=('Arial', 18), command= smoothen)
smoothen.grid(row=3, column=0, padx=2)


# change them all to the same length
blur.configure(width=10)
grayscale.configure(width=10)
reflect.configure(width=10)
contour.configure(width=10)
emboss.configure(width=10)
sharpen.configure(width=10)
smoothen.configure(width=10)

# create a quit button 
quit = tk.Button(root, text="Quit", command=root.destroy)
quit.place(relx=0.5, rely=1, anchor='s', y = -20)

# Make the window not resizeable
root.resizable(False, False)

# Show window
root.mainloop()