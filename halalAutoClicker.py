from tkinter import *

count = 0
def click():
  global count
  count +=1
  if count == 1:
    print("You clicked me once.")
  else:
    print("You clicked me:", count,"times.")

window = Tk()
window.title("Halal Clicker")
window.iconbitmap("kaaba2.ico")
photo=PhotoImage(file="kaaba.png")

button = Button(window,
 text = "Click for thawab",
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



window.mainloop()



