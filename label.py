#!/usr/bin/env python3

'''
An example of a Label with wrapping at 200 pixels and a left-justification of
the layout.
'''

import tkinter

class Window(tkinter.Tk):
    def __init__(self):
        tkinter.Tk.__init__(self)
        self.title("Label")
        self.geometry("200x200")

        label = tkinter.Label(text="This is an example of a Label widget within a Window container.")
        label.config(justify=tkinter.LEFT)
        label.config(wrap=200)
        label.pack(fill=tkinter.BOTH, expand=1)

if __name__ == "__main__":
    application = Window()
    application.mainloop()
