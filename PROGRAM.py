from tkinter import *
from tkinter import filedialog

class MyMenuDemo:
    def __init__(self,root):
        # Create a menubar
        self.menubar = Menu(root)
        # Attach the menubar to the root window
        root.config(menu=self.menubar)
        # create file menu
        self.filemenu = Menu(root,tearoff=0)
        # Create menu items in file menu
        self.filemenu.add_command(label="New", command=self.donothing)
        self.filemenu.add_command(label="Open" , command=self.open_file)
        self.filemenu.add_command(label="Save", command=self.save_file)
        # Add a horizontal line as separator
        self.filemenu.add_separator()
        # Create another menu item below the separator
        self.filemenu.add_command(label="Exit", command=root.destroy)
        # add the file menu with a name "File" to the menubar
        self.menubar.add_cascade(label="File", menu=self.filemenu)
        # Create edit menu
        self.editmenu = Menu(root, tearoff=0)
        # Create menu items in edit menu
        self.editmenu.add_command(label="Cut", command=self.donothing)
        self.editmenu.add_command(label="Copy", command=self.donothing)
        self.editmenu.add_command(label="Paste", command=self.donothing)

        # add the edit menu with a name "Edit" to the menubar
        self.menubar.add_cascade(label="Edit", menu=self.editmenu)

    def donothing(self):
        pass

# Method for opening a file and display its contents in a text box
    def open_file(self):
        # Open a file dialog box and accept the file name
        self.filename = filedialog.askopenfilename(parent=root, title="Select a file",filetypes=(("Pythonfiles",".py"),("All files",".")))
        #if cancel button is not clicked in the dialog box
        if self.filename != None:
            # open the file in read mode
            f = open(self.filename,'r')
            # read the content of the file
            contents = f.read()
            # Create a text box and add it to root window
            self.t = Text(root,width=80, height=20, wrap=WORD)

            self.t.pack()
            # insert the file contents in the textbox
            self.t.insert(1.0,contents)
            # Close the file
            f.close()


# Method to save a file that is already in the text box
    def save_file(self):
        # Open a file dialog box and type a file name
        self.filename = filedialog.asksaveasfile(parent=root, defaultextention=".txt")
        # if cancel button is not Clicked in the dialog box

        if self.filename != None:
            # Open the file in read mode
            f = open(self.filename, 'w')
            # get the contents of the text box
            contents = str(self.t.get(1.0, END))
            # store the file contents into the file
            f.write(contents)
            # Close the file
            f.close()

# Create root window
root = Tk()
# title for the root window
root.title("A Menu example")
# Create object to our class
obj = MyMenuDemo(root)
# define the size of the root window
root.geometry("600x350")
# handle any events
root.mainloop()