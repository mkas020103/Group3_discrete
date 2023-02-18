from tkinter import filedialog
import os
from tkinter import *
from PIL import Image, ImageFilter, ImageOps, ImageTk, ImageEnhance
from PIL import UnidentifiedImageError


class GUI:
    def __init__(self):

        # Create a list to put all the pictures
        self.list_of_pictures = []

        # Create root
        self.root = Tk()

        # Width and height of the image (to be updated during the program start)
        self.width = 0
        self.height = 0

        # Add a title
        self.root.title("Filter.io")

        # Initially false, since there is no picture in the two frames
        self.right_picture = 0
        self.center_picture = 0

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

        # Add main label
        self.title = Label(master=self.center_frame, text="Filter.io", font=("Abadi", 30), bg="#262626", fg="white")
        self.title.pack(pady=30)

        # Create blur button
        self.blur = Button(self.left_frame, text="Blur", font=('Arial', 11), command=self.blur)
        self.blur.grid(row=0, column=0, padx=22, pady=(100, 5))

        # Create grayscale button
        self.grayscale = Button(self.left_frame, text="Grayscale", font=('Arial', 11), command=self.grayscale)
        self.grayscale.grid(row=1, column=0, padx=22, pady=(5, 5))

        # Create reflect button
        self.reflect = Button(self.left_frame, text="Reflect", font=('Arial', 11), command=self.reflect)
        self.reflect.grid(row=2, column=0, padx=22, pady=(5, 5))

        # Create contour button
        self.contour = Button(self.left_frame, text="Contour", font=('Arial', 11), command=self.contour)
        self.contour.grid(row=3, column=0, padx=22, pady=(5, 5))

        # Create emboss button
        self.emboss = Button(self.left_frame, text="Emboss", font=('Arial', 11), command=self.emboss)
        self.emboss.grid(row=4, column=0, padx=22, pady=(5, 5))

        # Create sharpen button
        self.sharpen = Button(self.left_frame, text="Sharpen", font=('Arial', 11), command=self.sharpen)
        self.sharpen.grid(row=5, column=0, padx=22, pady=(5, 5))
        
        # Create blue button
        self.blue = Button(self.left_frame, text="Blue", font=('Arial', 11), command=self.blue)
        self.blue.grid(row=7, column=0, padx=22, pady=(5, 5))

        # Create smoothen button
        self.smoothen = Button(self.left_frame, text="Smoothen", font=('Arial', 11), command=self.smoothen)
        self.smoothen.grid(row=6, column=0, padx=22, pady=(5, 5))

        # Create reset button
        self.reset = Button(self.left_frame, text="RESET", font=('Arial', 11), command=self.reset)
        self.reset.grid(row=7, column=0, padx=22, pady=(100, 5))

        # Ask user for the image
        self.instruction = Label(master=self.right_frame, text="Choose Image", font=("Arial", 11), bg="#404040",
                                 fg="white")
        self.instruction.pack(padx=20, pady=(30, 1))

        # Create a browse button
        self.browse = Button(self.right_frame, text="Browse Directory", font=('Arial', 11), command=self.get_image_file)
        self.browse.pack(padx=22, pady=10)
        self.browse.configure(width=25)

        # Previous image label
        self.previous_label = Label(master=self.right_frame, text="Previous Image", font=("Arial", 11), bg="#404040", fg="white")
        self.previous_label.pack(padx=20, pady=(15, 1))

        # Create undo button
        self.undo = Button(self.right_frame, text="Undo", font=('Arial', 11))
        self.undo.place(relx=0.5, rely=1, anchor='s', y=-150, x=-70)
        self.undo.configure(width=10)

        # Create redo button
        self.redo = Button(self.right_frame, text="Redo", font=('Arial', 11))
        self.redo.place(relx=0.5, rely=1, anchor='s', y=-150, x=70)
        self.redo.configure(width=10)

        # Create save button
        self.save = Button(self.right_frame, text="SAVE", font=('Arial', 11), bg="#247802", fg="white")
        self.save.place(relx=0.5, rely=1, anchor='s', y=-80)
        self.save.configure(width=10)

        # Create a quit button
        self.quit = Button(self.right_frame, text="QUIT", font=("Arial", 11), command=self.root.destroy, bg="#F20000", fg="white")
        self.quit.place(relx=0.5, rely=1, anchor='s', y=-40)
        self.quit.configure(width=10)

        # Change all the filter buttons to the same length
        self.blur.configure(width=12)
        self.grayscale.configure(width=12)
        self.reflect.configure(width=12)
        self.contour.configure(width=12)
        self.emboss.configure(width=12)
        self.sharpen.configure(width=12)
        self.smoothen.configure(width=12)
        self.reset.configure(width=12)
        self.blue.configure(width=12)

        # make the window not resizeable
        self.root.resizable(False, False)

        self.root.mainloop()

    # if the users haven't type anything yet
    def error_message(self):
        # print a warning sign to the error
        self.warning = Label(self.center_frame, text="INPUT AN IMAGE FILE PATH!", fg="red", font="Arial 20 bold",bg="#262626")
        self.warning.pack()

        # remove after 2 seconds
        self.root.after(2500, self.warning.destroy)

    # if no file is found
    def file_not_found(self):
        # print a warning sign to the error
        self.warning = Label(self.center_frame, text="FILE NOT FOUND!", fg="red", font="Arial 20 bold", bg="#262626")
        self.warning.pack()

        # remove after 2 seconds
        self.root.after(2500, self.warning.destroy)

    # get the image file and display
    def get_image_file(self):
        try:
            # select file from directory
            if self.center_picture == 0: # if there's no picture in the window
                
                self.directory = os.getcwd()
                self.input_directory = filedialog.askopenfilename(parent=self.root, initialdir=self.directory,
                                                            title='Please select an Image')

                # take the file path of the selected file from directory
                self.file_path = self.input_directory

                # open image file
                self.image = Image.open(self.file_path)

                # save a copy of the original image file
                self.original_image = self.image

                # take the width and height
                self.width, self.height = self.image.size # (width, height)

                # resize the image
                if self.width > self.height:
                    self.image = self.image.resize((700, int((700 * self.height) / self.width)), Image.LANCZOS)
                    self.current_image = ImageTk.PhotoImage(self.image)
                else:
                    self.image = self.image.resize((int((500 * self.width) / self.height), 500), Image.LANCZOS)
                    self.current_image = ImageTk.PhotoImage(self.image)

                # append original to list
                self.list_of_pictures.append(self.image)

                # display image
                self.displaying_image = Label(master=self.center_frame, image=self.current_image)
                self.displaying_image.pack()
                
                # there's already an image so make the variable greater than 0
                self.center_picture += 1
            else:                
                
                directory = os.getcwd()
                input_directory = filedialog.askopenfilename(parent=self.root, initialdir=directory,
                                                            title='Please select an Image')           
                
                # take the file path of the selected file from directory
                self.file_path = input_directory

                # open image file
                self.image = Image.open(self.file_path)

                # save a copy of the original image file
                self.original_image = self.image

                # take the width and height
                self.width, self.height = self.image.size

                # resize the image
                if self.width > self.height:
                    self.image = self.image.resize((700, int((700 * self.height) / self.width)), Image.LANCZOS)
                    self.current_image = ImageTk.PhotoImage(self.image)
                else:
                    self.image = self.image.resize((int((500 * self.width) / self.height), 500), Image.LANCZOS)
                    self.current_image = ImageTk.PhotoImage(self.image)
                    
                # destroy or remove the images
                self.displaying_image.destroy()
                self.list_of_pictures.clear()
                if self.right_picture > 0:
                    self.previous.destroy()

                # append original to list
                self.list_of_pictures.append(self.image)

                # display image
                self.displaying_image = Label(master=self.center_frame, image=self.current_image)
                self.displaying_image.pack()

        # if there's an attribute error ping the user
        except FileNotFoundError:
            self.file_not_found()
            
        except UnidentifiedImageError:
            self.error_message()
            
        except AttributeError:
            self.error_message()
            
    # blur image
    def blur(self):
        try:
            # get the last image in the list
            self.last_image = next(reversed(self.list_of_pictures))
            self.filter = self.last_image.filter(ImageFilter.BoxBlur(4))
            self.append_display_destroy()
        except StopIteration:
            self.error_message()

    # grayscale image
    def grayscale(self):
        try:       
            # get the last image in the list
            self.last_image = next(reversed(self.list_of_pictures))
            self.filter = ImageOps.grayscale(self.last_image)
            self.append_display_destroy()
        except StopIteration:
            self.error_message()

    # reflect image
    def reflect(self):
        try:    
            # get the last image in the list
            self.last_image = next(reversed(self.list_of_pictures))
            self.filter = ImageOps.mirror(self.last_image)
            self.append_display_destroy()
        except StopIteration:
            self.error_message()

    # countor image
    def contour(self):
        try:
            # get the last image in the list
            self.last_image = next(reversed(self.list_of_pictures))
            self.filter = self.last_image.filter(ImageFilter.CONTOUR)
            self.append_display_destroy()
        except StopIteration:
            self.error_message()

    # emboss image
    def emboss(self):
        try:
            # get the last image in the list
            self.last_image = next(reversed(self.list_of_pictures))
            self.filter = self.last_image.filter(ImageFilter.CONTOUR)
            self.append_display_destroy()
        except StopIteration:
            self.error_message()

    # sharpen image
    def sharpen(self):
        try:
            # get the last image in the list
            self.last_image = next(reversed(self.list_of_pictures))
            self.filter = self.last_image.filter(ImageFilter.SHARPEN)
            self.append_display_destroy()
        except StopIteration:
                self.error_message()


    # smoothen image
    def smoothen(self):
        try:
            # get the last image in the list
            self.last_image = next(reversed(self.list_of_pictures))
            self.filter = self.last_image.filter(ImageFilter.SMOOTH)
            self.append_display_destroy()
        except StopIteration:
            self.error_message()
            
    def blue(self):
        try:
            # get the last image in the list
            self.last_image = next(reversed(self.list_of_pictures))
            self.last_image_copy = self.last_image.copy()
            self.last_image_copy = self.last_image_copy.convert("L")
            self.temp = ImageOps.colorize(self.last_image_copy, black ="blue", white ="white")
            self.filter = self.temp.convert("RGB")
            self.append_display_destroy()
        except StopIteration:
            self.error_message()

    def append_display_destroy(self):

            # resize if needed
            if self.width > self.height:
                self.last_image = self.last_image.resize((280, int((280 * self.height) / self.width)), Image.LANCZOS)
                self.previous_filter = ImageTk.PhotoImage(self.last_image)
            else:
                self.last_image = self.last_image.resize((int((280 * self.width) / self.height), 280), Image.LANCZOS)
                self.previous_filter = ImageTk.PhotoImage(self.last_image)
                
            # append the blurred photo to the list
            self.list_of_pictures.append(self.filter)

            # if there is a picture on the right frame already
            if self.right_picture > 0:
                self.previous.destroy()

            # display the previous image to the right frame
            self.previous = Label(master=self.right_frame, image=self.previous_filter)
            self.previous.pack(pady=(15, 5))
            self.right_picture += 1

            # remove the previous image in center frame
            self.displaying_image.destroy()

            # display blurred image
            self.current_filter = ImageTk.PhotoImage(self.filter)
            self.displaying_image = Label(master=self.center_frame, image=self.current_filter)
            self.displaying_image.pack()

    # reset button
    def reset(self):
        while len(self.list_of_pictures) != 1:
            del self.list_of_pictures[-1]

        # remove displayed images
        self.previous.destroy()
        self.displaying_image.destroy()

        #copy original image
        self.image = self.original_image

        # take the width and height
        self.width, self.height = self.image.size

        # resize the image
        if self.width > self.height:
            self.image = self.image.resize((700, int((700 * self.height) / self.width)), Image.LANCZOS)
            self.current_image = ImageTk.PhotoImage(self.image)
        else:
            self.image = self.image.resize((int((500 * self.width) / self.height), 500), Image.LANCZOS)
            self.current_image = ImageTk.PhotoImage(self.image)

        # append original to list
        self.list_of_pictures.append(self.image)

        # display image
        self.displaying_image = Label(master=self.center_frame, image=self.current_image)
        self.displaying_image.pack()
        


# Show the window
app = GUI()
app.root.mainloop()