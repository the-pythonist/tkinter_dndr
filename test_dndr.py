import tkinter_dndr
import tkinter

window = tkinter.Tk()

button = tkinter.Button(text = "Test Widget")

button.place(x=10,y=10,width=20,height=20)

dndr_button = tkinter_dndr.DragDropResizeWidget(but)
dndr_button.make_draggable_and_resizable() # if you want the widget to be both draggable and resizable
dndr_button.make_draggable() # if you want the widget to only have drag and drop support
dndr_button.make_resizable() # if you want the widget to only be resizable

window.mainloop()

