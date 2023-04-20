from tkinter import *

with open("ranks.txt", "r") as f:
  data = [l.strip() for l in f]
  
print(data)

#Counter function
pointer = 0
count = 0
rank = ""
def click():
  global count
  global pointer
  count+=1
  if count % 10 == 0:
    rank.configure(text=data[pointer])
    pointer += 1
  thawab.configure(text=f"Thawab: {count}")
  if len(data) <= pointer:
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
  width=639)
button.pack()


#Thawab counter
thawab = Label(root,text="Thawab = 0",font=("Comic Sans MS", 20),fg="black", bg="tan", width=40)
thawab.pack()

#Achievement label
rank = Label(root,text="Foetus Muslim",font=("Comic Sans MS", 20),fg="black", bg="tan", width=40)
rank.pack()
root.mainloop()