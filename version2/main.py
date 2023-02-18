import tkinter as tk

#Create a tk window
root = tk.Tk()

#Give the area of the window
root.geometry("1280x685")

#Add a title
root.title("Filter.io")

#Set App Icon
root.iconbitmap(r'C:\Users\tashi\Documents\Project\filterio.ico')

frame1 = tk.Frame(master=root, width=320, height=685, bg="#404040")
frame1.pack(fill=tk.BOTH, side=tk.LEFT)
frame1.pack_propagate(False)

frame2 = tk.Frame(master=root, width=800, bg="#262626")
frame2.pack(fill=tk.BOTH, side=tk.LEFT)
frame2.pack_propagate(False)

frame3 = tk.Frame(master=root, width=160, bg="#404040")
frame3.pack(fill=tk.BOTH, side=tk.LEFT)
frame3.pack_propagate(False)

label1 = tk.Label(master=frame2, text="Filter.io", font=("Abadi", 30), bg="#262626", fg="white")
label1.pack(pady=30)

# Ask for the image
label2 = tk.Label(master=frame1, text="Enter Image Path:", font=("Arial", 11), bg="#404040", fg="white")
label2.pack(padx=20, pady=(30, 1), anchor="w")

file_path = tk.Entry(frame1)
image_file = file_path.get()
image = Image.open(fp, mode='r', formats=None)

file_path.pack(padx=20, pady=3)
file_path.configure(width=50)

#Buttons

# Create blur button
blur = tk.Button(frame3, text="Blur", font=('Arial', 11))
blur.grid(row=0, column=0, padx=22, pady=(100, 5))

# Create grayscale button
grayscale = tk.Button(frame3, text="Grayscale", font=('Arial', 11))
grayscale.grid(row=1, column=0, padx=22, pady=(5, 5))

# Create reflect button
reflect = tk.Button(frame3, text="Reflect", font=('Arial', 11))
reflect.grid(row=2, column=0, padx=22, pady=(5, 5))

# Create contour button
contour = tk.Button(frame3, text="Contour", font=('Arial', 11))
contour.grid(row=3, column=0, padx=22, pady=(5, 5))

# Create emboss button
emboss = tk.Button(frame3, text="Emboss", font=('Arial', 11))
emboss.grid(row=4, column=0, padx=22, pady=(5, 5))

# Create sharpen button
sharpen = tk.Button(frame3, text="Sharpen", font=('Arial', 11))
sharpen.grid(row=5, column=0, padx=22, pady=(5, 5))

# Create smoothen button
smoothen = tk.Button(frame3, text="Smoothen", font=('Arial', 11))
smoothen.grid(row=6, column=0, padx=22, pady=(5, 5))

# Create reset button
reset = tk.Button(frame3, text="RESET", font=('Arial', 11))
reset.grid(row=7, column=0, padx=22, pady=(100, 5))

# change them all to the same length
blur.configure(width=12)
grayscale.configure(width=12)
reflect.configure(width=12)
contour.configure(width=12)
emboss.configure(width=12)
sharpen.configure(width=12)
smoothen.configure(width=12)
reset.configure(width=12)

root.resizable(False, False)
root.mainloop()