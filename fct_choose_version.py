"""fonction pour choix version à jouer"""
from tkinter import *
from functools import partial
from lecture_partition import play,inverse,new_song


def play_version(n):
    """Fenêtre Choix jouer le morceau normalement ou en reverse"""
    small_window = Tk()
    small_window.title("Which version ?")
    small_window.geometry('200x100')
    small_window.config(background='#ABEBC6')

    nrml = Button(small_window, text="Jouer le morceau normalement", command=partial(play, n))
    nrml.pack()
    inv = Button(small_window, text="Jouer le morceau inversé", command=partial(inverse, n))
    inv.pack(fill=X)
    small_window.mainloop()
