try:
  import tkinter
except ImportError:
  import Tkinter as tkinter


# tkinter._test()
# mainWindow = tkinter.Tk()
# mainWindow.title("Hello world")
# mainWindow.geometry('640x480+8+400')

# label = tkinter.Label(mainWindow, text="Hello World")
# label.pack(side='top')

# leftFrame = tkinter.Frame(mainWindow)
# leftFrame.pack(side='left', anchor='n', fill=tkinter.Y, expand=False)

# canvas = tkinter.Canvas(leftFrame, relief='raised', borderwidth=3)
# canvas.pack(side='left', anchor='n', fill=tkinter.BOTH, expand=True)

# rightFrame = tkinter.Frame(mainWindow)
# rightFrame.pack(side='right', anchor='n', expand=True)

# button1 = tkinter.Button(rightFrame, text="Open")
# button2 = tkinter.Button(rightFrame, text="Edit")
# button3 = tkinter.Button(rightFrame, text="Close")
# button1.pack(side='left')
# button2.pack(side='left')
# button3.pack(side='left')

# mainWindow.mainloop()

mainWindow = tkinter.Tk()
mainWindow.title("Hello world")
mainWindow.geometry('640x480-8-200')

label = tkinter.Label(mainWindow, text="Hello World")
label.grid(row=0, column=0)

leftFrame = tkinter.Frame(mainWindow)
leftFrame.grid(row=1, column=1)

canvas = tkinter.Canvas(leftFrame, relief='raised', borderwidth=1)
canvas.grid(row=1, column=0)

rightFrame = tkinter.Frame(mainWindow)
rightFrame.grid(row=1, column=2, sticky='n')
button1 = tkinter.Button(rightFrame, text="Open")
button2 = tkinter.Button(rightFrame, text="Edit")
button3 = tkinter.Button(rightFrame, text="Close")
button1.grid(row=0, column=0)
button2.grid(row=1, column=0)
button3.grid(row=2, column=0)

mainWindow.columnconfigure(0, weight=1)
mainWindow.columnconfigure(1, weight=1)
mainWindow.grid_columnconfigure(2, weight=1)

leftFrame.config(relief='sunken', borderwidth=1)
rightFrame.config(relief='sunken', borderwidth=1)
leftFrame.grid(sticky='ns')
rightFrame.grid(sticky='new')

rightFrame.columnconfigure(0, weight=1)
button1.grid(sticky='ew')
button2.grid(sticky='ew')
button3.grid(sticky='ew')
mainWindow.mainloop()