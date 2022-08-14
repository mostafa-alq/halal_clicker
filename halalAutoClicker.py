from tkinter import *


count = 0
output = ""
def click():
  global count
  count +=1


root = Tk()
root.title("Halal Clicker")
# root.attributes("fullscreen",True)
root.iconbitmap("kaaba2.ico")
photo=PhotoImage(file="kaaba.png")

output = Label(root,text="Thawab: "+str(count))
output.pack()

button = Button(root,
 text="Click for thawab",
 command=click,
 font=("Comic Sans MS", 30),
 fg="black",
 bg="#BDEBED",
 activebackground="#D4F4F5",
 activeforeground="black",
 state=ACTIVE,
 image=photo,
 compound="top",
 cursor="heart")
button.pack()



root.mainloop()



