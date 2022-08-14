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

photo=PhotoImage(file="kaaba.png")

button = Button(window,
 text = "Click for thawab.",
 command=click,
 font=("Comic Sans", 30),
 fg="#00FF00",
 bg="black",
 activebackground="black",
 activeforeground="#00FF00",
 state=ACTIVE,
 image=photo,
 compound="top")
button.pack()

window.mainloop()



