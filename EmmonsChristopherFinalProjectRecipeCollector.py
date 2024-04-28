#Recipe Storage Application
#This will be used to collect, edit, and enter recipes

#import program
from tkinter import *
import tkinter as tk
#from PIL import ImageTk,Image

#define
root = Tk()

#home page
class HomePage(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.master.title("Recipe Helper")

        self.label = tk.Label(self, text="Welcome to YOUR Recipe Helper!", font=("Ariel", 20))
        self.label.pack(pady=20)
        
        self.description_label = tk.Label(self, text="Use this application to add, edit, and search through your personal recipes!", font=("Helvetica", 12))
        self.description_label.pack()

        #images
        #gotta figure out PIL and why that aint working. already reinstalled wiht box ticked.
        #myimg1 = ImageTK.PhotoImage(Image.open("Final Project/Front page image strawaberry cupcake.heic"))
        
        #add button to add a new recipe
        #self.add_button = tk.Button(self, text="Add", command=self.start_application)
        #self.add_button.pack(pady=20)

        self.add_button = tk.Button(self, text="Add", command=self.start_application)
        self.add_button.pack(pady=10)

        def open_second_window(self):
            add_window = AddWindow(self)

        #search button from the main screen to search through all recipes
        self.search_button = tk.Button(self, text="Search", command=self.start_application)
        self.search_button.pack(pady=20)
        
        #exit button to leave program-working
        self.exit_button = tk.Button(self, text="Exit", command=root.quit)
        self.exit_button.pack(pady=20)
        
        self.pack()

    def start_application(self):
        # Replace this with code to navigate to another part of your application
        print("Starting application...")

        #second window 2hr 40 min in
    def open():
        top = Toplevel()
        top.title("Chocolate Cupcakes")

    btn = Button(root, text="Chocolate Cupcakes", command=open).pack()



        

def main():
    root = tk.Tk()
    app = HomePage(root)
    root.mainloop()

if __name__ == "__main__":
    main()