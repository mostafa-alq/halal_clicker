from tkinter import *

#Counter function
count = 0
def click():
  global count
  count+=1
  thawab.configure(text=f"Thawab: {count}")

#Initialising the window
root = Tk()
root.title("Halal Clicker")
# root.attributes("fullscreen",True)
root.iconbitmap("kaaba2.ico")
photo=PhotoImage(file="kaaba.png")

#Thawab button
button = Button(root,
 text="Click for thawab",
 command=click,
 font=("Comic Sans MS", 30),
 fg="black",
 bg="#BDEBED",
 activebackground="#D4F4F5",
 activeforeground="black",
 image=photo,
 compound="top",
 cursor="heart")
button.pack()


#Thawab counter
thawab = Label(root,text="Thawab = 0")
thawab.pack()

root.mainloop()