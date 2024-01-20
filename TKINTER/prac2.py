from tkinter import *
 
root=Tk()
#width X hieght
root.geometry('455x244')

photo=PhotoImage(file='bike.png')

#creating label
labal=Label(image=photo)
labal.pack()
root.mainloop()