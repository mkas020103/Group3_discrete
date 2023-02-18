from tkinter import *
from PIL import Image, ImageFilter, ImageOps, ImageTk

class GUI:
    def __init__(self):
        
        # Create a list to put all the pictures
        self.list_of_pictures = []
        
        # Create root
        self.root = Tk()
        
        # Create right frame
        self.right_frame = Frame(master=self.root, width=320, height=685, bg="#404040")
        self.right_frame.pack(fill=BOTH, side=LEFT)
        self.right_frame.pack_propagate(False)
        
        # Create center frame
        self.center_frame = Frame(master=self.root, width=800, bg="#262626")
        self.center_frame.pack(fill=BOTH, side=LEFT)
        self.center_frame.pack_propagate(False)
        
        # Create left frame
        self.left_frame = Frame(master=self.root, width=160, bg="#404040")
        self.left_frame.pack(fill=BOTH, side=LEFT)
        self.left_frame.pack_propagate(False)
        
        self.title = Label(master=self.center_frame, text="Filter.io", font=("Abadi", 30), bg="#262626", fg="white")
        self.title.pack(pady=30)

        # Ask user for the image
        self.instruction = Label(master=self.right_frame, text="Enter Image Path:", font=("Arial", 11), bg="#404040", fg="white")
        self.instruction.pack(padx=20, pady=(30, 1), anchor="w")
        
        # Create an entry area for users
        self.input = Entry(self.right_frame)
        self.input.pack(padx=20, pady=3)
        self.input.configure(width=50)
        
        # Create blur button
        self.blur = Button(self.left_frame, text="Blur", font=('Arial', 11), command = self.blur)
        self.blur.grid(row=0, column=0, padx=22, pady=(100, 5))

        # Create grayscale button
        self.grayscale = Button(self.left_frame, text="Grayscale", font=('Arial', 11))
        self.grayscale.grid(row=1, column=0, padx=22, pady=(5, 5))

        # Create reflect button
        self.reflect = Button(self.left_frame, text="Reflect", font=('Arial', 11))
        self.reflect.grid(row=2, column=0, padx=22, pady=(5, 5))

        # Create contour button
        self.contour = Button(self.left_frame, text="Contour", font=('Arial', 11))
        self.contour.grid(row=3, column=0, padx=22, pady=(5, 5))

        # Create emboss button
        self.emboss = Button(self.left_frame, text="Emboss", font=('Arial', 11))
        self.emboss.grid(row=4, column=0, padx=22, pady=(5, 5))

        # Create sharpen button
        self.sharpen = Button(self.left_frame, text="Sharpen", font=('Arial', 11))
        self.sharpen.grid(row=5, column=0, padx=22, pady=(5, 5))

        # Create smoothen button
        self.smoothen = Button(self.left_frame, text="Smoothen", font=('Arial', 11))
        self.smoothen.grid(row=6, column=0, padx=22, pady=(5, 5))

        # Create reset button
        self.reset = Button(self.left_frame, text="RESET", font=('Arial', 11))
        self.reset.grid(row=7, column=0, padx=22, pady=(100, 5))
        
        # Create a quit button
        self.quit = Button(self.right_frame, text="Quit", command=self.root.destroy, bg='red')
        self.quit.place(relx=0.5, rely=1, anchor='s', y = -20)
        
        # Create an enter button
        self.enter = Button(self.right_frame, text="Enter", font=('Arial', 11), command = self.get_image_file)
        self.enter.pack(padx=22, pady=(8, 1))
        
        
        # change them all to the same length
        self.blur.configure(width=12)
        self.grayscale.configure(width=12)
        self.reflect.configure(width=12)
        self.contour.configure(width=12)
        self.emboss.configure(width=12)
        self.sharpen.configure(width=12)
        self.smoothen.configure(width=12)
        self.reset.configure(width=12)

        # make the window not resizeable
        self.root.resizable(False, False)
                
        
        self.root.mainloop()
        
    # get the image file and display
    def get_image_file(self):
        
        # take the input in the entry
        self.file_path = self.input.get()
        
        # open image file
        self.image = Image.open(self.file_path)
        
        #take the width and height
        width, height = self.image.size
        
        # resize the image
        if width < 700:
            self.image = self.image.resize((width, height), Image.LANCZOS)
            self.current_image = ImageTk.PhotoImage(self.image)
        else:
            self.image = self.image.resize((int(width/1.2), int(height/1.2)), Image.LANCZOS)
            self.current_image = ImageTk.PhotoImage(self.image)
        
        # append original to list
        self.list_of_pictures.append(self.image)
        
        # display image
        self.displaying_image = Label(master=self.center_frame, image=self.current_image)
        self.displaying_image.pack()
        
        # delete the input in the entry box
        self.input.delete(0, 'end')
        
    # blur image
    def blur(self):
        try:
            self.blurred = self.image
            self.current_image = ImageTk.PhotoImage(self.blurred)
        except AttributeError:
            self.warning = Label(self.center_frame, text="INPUT THE IMAGE FILE PATH FIRST!", fg="red", font="Arial 20 bold", bg="#262626")
            self.warning.pack()
            self.root.after(2500, self.warning.destroy)
    
# Show the window      
app = GUI()
app.root.mainloop()