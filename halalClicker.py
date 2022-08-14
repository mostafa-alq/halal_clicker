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
  elif count == 20:
    rank.configure(text=f"Inpet Muslim")
  elif count == 30:
    rank.configure(text=f"Weak Muslim")
  elif count == 40:
    rank.configure(text=f"Unskilled Muslim")
  elif count == 50:
    rank.configure(text=f"Mediocre Muslim")
  elif count == 60:
    rank.configure(text=f"Initiated Muslim")
  elif count == 70:
    rank.configure(text=f"Dedicated Muslim")
  elif count == 80:
    rank.configure(text=f"Skilled Muslim")
  elif count == 90:
    rank.configure(text=f"Remarkable Muslim")
  elif count == 100:
    rank.configure(text=f"JANNAH FOR YOU BROTHER MASHALLAH")
    thawab.configure(text=f"JANNAH FOR YOU BROTHER MASHALLAH") 
    sicktitle.configure(text=f"JANNAH FOR YOU BROTHER MASHALLAH")

#Initialising the window
root = Tk()
root.title("Halal Clicker")
# root.attributes("fullscreen",True)
root.iconbitmap("kaaba2.ico")
photo=PhotoImage(file="kaaba.png")

#Epic title
sicktitle = Label(root, text="VERY GOOD OFFICIAL HALAL CLICKER PATENT PENDING (do not steal or jahanam awaits you)", font=("Comic Sans MS", 10),bg="tan", width=80)
sicktitle.pack()

#Thawab button
button = Button(root,
 text="Click for thawab!!!",
 command=click,
 font=("Comic Sans MS", 30),
 image=photo,
 bg="#BDEBED",
 activebackground="#BDEBED",
 compound="top",
 cursor="heart",
 width=640)
button.pack()


#Thawab counter
thawab = Label(root,text="Thawab = 0",font=("Comic Sans MS", 20),fg="black", bg="tan", width=40)
thawab.pack()

#Achievement label
rank = Label(root,text="Foetus Muslim",font=("Comic Sans MS", 20),fg="black", bg="tan", width=40)
rank.pack()
root.mainloop()