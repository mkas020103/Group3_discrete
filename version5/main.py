from tkinter import *
from PIL import Image, ImageFilter, ImageOps, ImageTk

class GUI:
    def __init__(self):
        
        # Create a list to put all the pictures
        self.list_of_pictures = []
        
        # Create root
        self.root = Tk()
        
        # Width and height of the image (to be updated during the program start)
        self.width = 0
        self.height = 0
        
        # Initially false, since there is no picture in the right frame
        self.picture = 0
        
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
        self.grayscale = Button(self.left_frame, text="Grayscale", font=('Arial', 11), command = self.grayscale)
        self.grayscale.grid(row=1, column=0, padx=22, pady=(5, 5))

        # Create reflect button
        self.reflect = Button(self.left_frame, text="Reflect", font=('Arial', 11), command = self.reflect)
        self.reflect.grid(row=2, column=0, padx=22, pady=(5, 5))

        # Create contour button
        self.contour = Button(self.left_frame, text="Contour", font=('Arial', 11), command = self.contour)
        self.contour.grid(row=3, column=0, padx=22, pady=(5, 5))

        # Create emboss button
        self.emboss = Button(self.left_frame, text="Emboss", font=('Arial', 11), command = self.emboss)
        self.emboss.grid(row=4, column=0, padx=22, pady=(5, 5))

        # Create sharpen button
        self.sharpen = Button(self.left_frame, text="Sharpen", font=('Arial', 11), command = self.sharpen)
        self.sharpen.grid(row=5, column=0, padx=22, pady=(5, 5))

        # Create smoothen button
        self.smoothen = Button(self.left_frame, text="Smoothen", font=('Arial', 11), command = self.smoothen)
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
        
    # if the users haven't type anything yet
    def error_message(self):
        #print a warning sign to the error
        self.warning = Label(self.center_frame, text="INPUT THE IMAGE FILE PATH FIRST!", fg="red", font="Arial 20 bold", bg="#262626")
        self.warning.pack()
            
        # remove after 2 seconds
        self.root.after(2500, self.warning.destroy)
    
    # if no file is found    
    def file_not_found(self):
        #print a warning sign to the error
        self.warning = Label(self.center_frame, text="FILE NOT FOUND!", fg="red", font="Arial 20 bold", bg="#262626")
        self.warning.pack()
            
        # remove after 2 seconds
        self.root.after(2500, self.warning.destroy)
        
    # get the image file and display
    def get_image_file(self):
        try:
            # take the input in the entry
            self.file_path = self.input.get()
            
            # open image file
            self.image = Image.open(self.file_path)
            
            #take the width and height
            self.width, self.height = self.image.size
            
            # resize the image
            if self.width < 700:
                self.image = self.image.resize((self.width, self.height), Image.LANCZOS)
                self.current_image = ImageTk.PhotoImage(self.image)
            else:
                self.image = self.image.resize((int(self.width/1.2), int(self.height/1.2)), Image.LANCZOS)
                self.current_image = ImageTk.PhotoImage(self.image)
            
            # append original to list
            self.list_of_pictures.append(self.image)
            
            # display image
            self.displaying_image = Label(master=self.center_frame, image=self.current_image)
            self.displaying_image.pack()
            
            # delete the input in the entry box
            self.input.delete(0, 'end')
         
        # if there's an attribute error ping the user    
        except AttributeError:
            self.error_message()
        
        except FileNotFoundError:
            self.file_not_found()
        
            
    # blur image
    def blur(self):
        try:
            # get the last image in the list
            self.last_image = next(reversed(self.list_of_pictures))
            self.blurred = self.last_image.filter(ImageFilter.BoxBlur(4))
            
            # append the blurred photo to the list
            self.list_of_pictures.append(self.blurred)
            
            # resize if needed
            if self.width > 310:
                self.last_image = self.last_image.resize((int(self.width/3), int(self.height/3)), Image.LANCZOS)
                self.previous_blurred = ImageTk.PhotoImage(self.last_image)
                
            # if there is a picture on the right frame already
            if self.picture > 0:
                self.previous.destroy()
                
            # display the previous image to the right frame
            self.previous = Label(master=self.right_frame, image=self.previous_blurred)
            self.previous.pack()
            self.picture += 1
            
            # remove the previous image in center frame
            self.displaying_image.destroy()
            
            # display blurred image
            self.current_blurred = ImageTk.PhotoImage(self.blurred)
            self.displaying_image = Label(master=self.center_frame, image=self.current_blurred)
            self.displaying_image.pack()
            
            
        except AttributeError:
            self.error_message()
            
        except StopIteration:
            self.error_message()
            
    # grayscale image
    def grayscale(self):
        try:
            # get the last image in the list
            self.last_image = next(reversed(self.list_of_pictures))
            self.blurred = ImageOps.grayscale(self.last_image)
            
            # append the blurred photo to the list
            self.list_of_pictures.append(self.blurred)
            
            # resize if needed
            if self.width > 310:
                self.last_image = self.last_image.resize((int(self.width/3), int(self.height/3)), Image.LANCZOS)
                self.previous_blurred = ImageTk.PhotoImage(self.last_image)
                
            # if there is a picture on the right frame already
            if self.picture > 0:
                self.previous.destroy()
                
            # display the previous image to the right frame
            self.previous = Label(master=self.right_frame, image=self.previous_blurred)
            self.previous.pack()
            self.picture += 1
            
            # remove the previous image in center frame
            self.displaying_image.destroy()
            
            # display blurred image
            self.current_blurred = ImageTk.PhotoImage(self.blurred)
            self.displaying_image = Label(master=self.center_frame, image=self.current_blurred)
            self.displaying_image.pack()
            
            
        except AttributeError:
            self.error_message()
            
        except StopIteration:
            self.error_message()
            
    # reflect image
    def reflect(self):
        try:
            # get the last image in the list
            self.last_image = next(reversed(self.list_of_pictures))
            self.blurred = ImageOps.mirror(self.last_image)
            
            # append the blurred photo to the list
            self.list_of_pictures.append(self.blurred)
            
            # resize if needed
            if self.width > 310:
                self.last_image = self.last_image.resize((int(self.width/3), int(self.height/3)), Image.LANCZOS)
                self.previous_blurred = ImageTk.PhotoImage(self.last_image)
                
            # if there is a picture on the right frame already
            if self.picture > 0:
                self.previous.destroy()
                
            # display the previous image to the right frame
            self.previous = Label(master=self.right_frame, image=self.previous_blurred)
            self.previous.pack()
            self.picture += 1
            
            # remove the previous image in center frame
            self.displaying_image.destroy()
            
            # display blurred image
            self.current_blurred = ImageTk.PhotoImage(self.blurred)
            self.displaying_image = Label(master=self.center_frame, image=self.current_blurred)
            self.displaying_image.pack()
            
            
        except AttributeError:
            self.error_message()
            
        except StopIteration:
            self.error_message()
    
    # countor image
    def contour(self):
        try:
            # get the last image in the list
            self.last_image = next(reversed(self.list_of_pictures))
            self.blurred = self.last_image.filter(ImageFilter.CONTOUR)
            
            # append the blurred photo to the list
            self.list_of_pictures.append(self.blurred)
            
            # resize if needed
            if self.width > 310:
                self.last_image = self.last_image.resize((int(self.width/3), int(self.height/3)), Image.LANCZOS)
                self.previous_blurred = ImageTk.PhotoImage(self.last_image)
                
            # if there is a picture on the right frame already
            if self.picture > 0:
                self.previous.destroy()
                
            # display the previous image to the right frame
            self.previous = Label(master=self.right_frame, image=self.previous_blurred)
            self.previous.pack()
            self.picture += 1
            
            # remove the previous image in center frame
            self.displaying_image.destroy()
            
            # display blurred image
            self.current_blurred = ImageTk.PhotoImage(self.blurred)
            self.displaying_image = Label(master=self.center_frame, image=self.current_blurred)
            self.displaying_image.pack()
            
            
        except AttributeError:
            self.error_message()
            
        except StopIteration:
            self.error_message()

    # emboss image
    def emboss(self):
        try:
            # get the last image in the list
            self.last_image = next(reversed(self.list_of_pictures))
            self.blurred = self.last_image.filter(ImageFilter.CONTOUR)
            
            # append the blurred photo to the list
            self.list_of_pictures.append(self.blurred)
            
            # resize if needed
            if self.width > 310:
                self.last_image = self.last_image.resize((int(self.width/3), int(self.height/3)), Image.LANCZOS)
                self.previous_blurred = ImageTk.PhotoImage(self.last_image)
                
            # if there is a picture on the right frame already
            if self.picture > 0:
                self.previous.destroy()
                
            # display the previous image to the right frame
            self.previous = Label(master=self.right_frame, image=self.previous_blurred)
            self.previous.pack()
            self.picture += 1
            
            # remove the previous image in center frame
            self.displaying_image.destroy()
            
            # display blurred image
            self.current_blurred = ImageTk.PhotoImage(self.blurred)
            self.displaying_image = Label(master=self.center_frame, image=self.current_blurred)
            self.displaying_image.pack()
            
            
        except AttributeError:
            self.error_message()
            
        except StopIteration:
            self.error_message()
            
    # sharpen image
    def sharpen(self):
        try:
            # get the last image in the list
            self.last_image = next(reversed(self.list_of_pictures))
            self.blurred = self.last_image.filter(ImageFilter.SHARPEN)
            
            # append the blurred photo to the list
            self.list_of_pictures.append(self.blurred)
            
            # resize if needed
            if self.width > 310:
                self.last_image = self.last_image.resize((int(self.width/3), int(self.height/3)), Image.LANCZOS)
                self.previous_blurred = ImageTk.PhotoImage(self.last_image)
                
            # if there is a picture on the right frame already
            if self.picture > 0:
                self.previous.destroy()
                
            # display the previous image to the right frame
            self.previous = Label(master=self.right_frame, image=self.previous_blurred)
            self.previous.pack()
            self.picture += 1
            
            # remove the previous image in center frame
            self.displaying_image.destroy()
            
            # display blurred image
            self.current_blurred = ImageTk.PhotoImage(self.blurred)
            self.displaying_image = Label(master=self.center_frame, image=self.current_blurred)
            self.displaying_image.pack()
            
            
        except AttributeError:
            self.error_message()
            
        except StopIteration:
            self.error_message()
            
    # smoothen image
    def smoothen(self):
        try:
            # get the last image in the list
            self.last_image = next(reversed(self.list_of_pictures))
            self.blurred = self.last_image.filter(ImageFilter.SMOOTH)
            
            # append the blurred photo to the list
            self.list_of_pictures.append(self.blurred)
            
            # resize if needed
            if self.width > 310:
                self.last_image = self.last_image.resize((int(self.width/3), int(self.height/3)), Image.LANCZOS)
                self.previous_blurred = ImageTk.PhotoImage(self.last_image)
                
            # if there is a picture on the right frame already
            if self.picture > 0:
                self.previous.destroy()
                
            # display the previous image to the right frame
            self.previous = Label(master=self.right_frame, image=self.previous_blurred)
            self.previous.pack()
            self.picture += 1
            
            # remove the previous image in center frame
            self.displaying_image.destroy()
            
            # display blurred image
            self.current_blurred = ImageTk.PhotoImage(self.blurred)
            self.displaying_image = Label(master=self.center_frame, image=self.current_blurred)
            self.displaying_image.pack()
            
            
        except AttributeError:
            self.error_message()
            
        except StopIteration:
            self.error_message()

    
# Show the window      
app = GUI()
app.root.mainloop()