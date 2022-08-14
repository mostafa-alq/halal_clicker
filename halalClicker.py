from tkinter import *

#Counter function
count = 0
rank = ""
def click():
  global count
  count+=1
  thawab.configure(text=f"Thawab: {count}")
  if count == 10:
    rank.configure(text=f"Newb Muslim")
  elif count == 25:
    rank.configure(text=f"Inpet Muslim")
  elif count == 50:
    rank.configure(text=f"Unskilled Muslim")
  elif count == 75:
    rank.configure(text=f"Mediocre Muslim")
  elif count == 100:
    rank.configure(text=f"Initiated Muslim")
  elif count == 250:
    rank.configure(text=f"Dedicated Muslim")
  elif count == 500:
    rank.configure(text=f"Skilled Muslim")
  elif count == 750:
    rank.configure(text=f"Remarkable Muslim")
  elif count == 1000:
    rank.configure(text=f"JANNAH FOR YOU BROTHER")

#Initialising the window
root = Tk()
root.title("Halal Clicker")
# root.attributes("fullscreen",True)
root.iconbitmap("kaaba2.ico")
photo=PhotoImage(file="kaaba.png")

#Thawab button
button = Button(root,
 text="Click for thawab!!!",
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

#Achievement label
rank = Label(root,text="Foetus Muslim")
rank.pack()

root.mainloop()