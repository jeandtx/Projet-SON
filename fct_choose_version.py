from tkinter import *
from functools import partial
from lecture_partition import *


def play_version(n):
    small_window = Tk()
    small_window.title("Which version ?")
    small_window.geometry('200x100')
    small_window.config(background='#ABEBC6')

    nrml = Button(small_window, text="Jouer le morceau normalement", command=partial(play, n))
    nrml.pack()
    inv = Button(small_window, text="Jouer le morceau inverser", command=partial(inverse, n))
    inv.pack(fill=X)
    small_window.mainloop()
