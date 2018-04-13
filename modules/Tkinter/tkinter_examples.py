try:
  import tkinter
except ImportError:
  import Tkinter as tkinter


# tkinter._test()
mainWindow = tkinter.Tk()
mainWindow.title("Hello world")
mainWindow.geometry('640x480+8+400')

label = tkinter.Label(mainWindow, text="Hello World")
label.pack(side='top')

leftFrame = tkinter.Frame(mainWindow)
leftFrame.pack(side='left', anchor='n', fill=tkinter.Y, expand=False)

canvas = tkinter.Canvas(leftFrame, relief='raised', borderwidth=3)
canvas.pack(side='left', anchor='n', fill=tkinter.BOTH, expand=True)

rightFrame = tkinter.Frame(mainWindow)
rightFrame.pack(side='right', anchor='n', expand=True)

button1 = tkinter.Button(rightFrame, text="Open")
button2 = tkinter.Button(rightFrame, text="Edit")
button3 = tkinter.Button(rightFrame, text="Close")
button1.pack(side='left')
button2.pack(side='left')
button3.pack(side='left')

mainWindow.mainloop()