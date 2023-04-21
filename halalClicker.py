from tkinter import *
from playsound import playsound
import pygame
import random

with open("ranks.txt", "r") as f:
  data = [l.strip() for l in f]

with open("colours.txt", "r") as g:
  data2 = [j.strip() for j in g]

#Counter function
pointer = 0
count = 0
rank = ""
def click():
  global count
  global pointer
  count+=1
  thawab.configure(text=f"Thawab: {count}")
  if count % 10 == 0:
    rank.configure(text=data[pointer])
    pointer += 1
  if len(data) <= pointer:
    rank.configure(text=f"JANNAH FOR YOU BROTHER MASHALLAH")
    thawab.configure(text=f"JANNAH FOR YOU BROTHER MASHALLAH") 
    sicktitle.configure(text=f"JANNAH FOR YOU BROTHER MASHALLAH")
    playButton.configure(text=f"JANNAH FOR YOU BROTHER MASHALLAH")
    pauseButton.configure(text=f"JANNAH FOR YOU BROTHER MASHALLAH")
    stopButton.configure(text=f"JANNAH FOR YOU BROTHER MASHALLAH")
    thawabButton.configure(text=f"JANNAH FOR YOU BROTHER MASHALLAH")
    

#Initialising the window
root = Tk()
root.title("Halal Clicker")
# root.attributes("fullscreen",True)
root.iconbitmap("kaaba2.ico")
photo=PhotoImage(file="kaaba.png")
bgcolour = data2[random.randint(0,len(data2)-1)]
root.configure(background=bgcolour)

#Epic title
sicktitle = Label(root, text="VERY GOOD OFFICIAL HALAL CLICKER PATENT PENDING (do not steal or jahanam awaits you)", font=("Bahnschrift", 10),bg=bgcolour, width=92)
sicktitle.pack()

#Thawab button
thawabButton = Button(root,text="Click for thawab!!!",command=click,font=("Bahnschrift", 30),image=photo,bg="#BDEBED", activebackground="#BDEBED",compound="top",cursor="heart",width=640)
thawabButton.pack()


#Thawab counter
thawab = Label(root,text="Thawab = 0",font=("Bahnschrift", 20),fg="black", bg=bgcolour, width=43)
thawab.pack()

#Achievement label
rank = Label(root,text="Foetus Muslim",font=("Bahnschrift", 20),fg="black", bg=bgcolour, width=43)
rank.pack()

space = Label(root,text="",font=("Bahnschrift", 20),fg="black", bg=bgcolour, width=43)
space.pack()

#Music
musicTitle = Label(root,text="[BEAUTIFUL NASHEED MASHALLAH]",font=("Bahnschrift", 20),fg="black", bg=bgcolour, width=43)
musicTitle.pack()

pygame.mixer.init()
musicTracker = 0
def playSound():
  pygame.mixer.music.load("sound.mp3")
  pygame.mixer.music.play()

def pauseSound():
  global musicTracker
  if musicTracker % 2 == 0:
    pygame.mixer.music.pause()
  else:
    pygame.mixer.music.unpause()
  musicTracker += 1
  
def stopSound():
  global musicTracker
  pygame.mixer.music.stop()
  musicTracker += 1

playButton = Button(root,text="Play",font=("Bahnschrift", 20),fg="black",bg=bgcolour,activebackground=bgcolour, command=playSound, width=25)
playButton.pack()

pauseButton = Button(root,text="Pause",font=("Bahnschrift", 20),fg="black",bg=bgcolour,activebackground=bgcolour, command=pauseSound, width=25)
pauseButton.pack()

stopButton = Button(root,text="Stop",font=("Bahnschrift", 20),fg="black",bg=bgcolour,activebackground=bgcolour,command=stopSound, width=25)
stopButton.pack()

space2 = Label(root,text="",font=("Bahnschrift", 20),fg="black", bg=bgcolour, width=43)
space2.pack()

root.mainloop()