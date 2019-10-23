import os
import tkinter as tk

#begining of the window
root= tk.Tk()

#this creates an area for the labes and button to go in
canvas1 = tk.Canvas(root, width = 350, height = 400, bg = 'lightsteelblue2', relief = 'raised')
canvas1.pack()

# this is the label
label1 = tk.Label(root, text='Hello Kelly Girls,''\n''Ready to be Awesome?''\n''Click the button!', bg = 'lightsteelblue2',font=('helvetica', 20))

#This adds the label to the canvas
canvas1.create_window(175, 80, window=label1)


#now to try and configure the button to go somewhere
def button ():

    #begining of the window
    window= tk.Tk()

    #this creates an area for the labes and button to go in
    canvas2 = tk.Canvas(window, width = 350, height = 250, bg = 'lightsteelblue2', relief = 'raised')
    canvas2.pack()

    # this is the label
    label2 = tk.Label(window, text='Hello Kelly Girls,''\n''You are Awesome!!', bg = 'lightsteelblue2',font=('helvetica', 20))

    #This adds the label to the canvas
    canvas2.create_window(175, 80, window=label2)

    #end of window
    window.mainloop()


# here is the button   
but1 = tk.Button(text='      The Awesome Button    ', command = button, bg='green', fg='white', font=('helvetica', 12, 'bold' ))
but1.pack()

#this adds the button to the canvas
canvas1.create_window(175, 180, window=but1)

#end of window
root.mainloop()


