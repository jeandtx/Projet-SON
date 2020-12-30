from fct_son import *
from tkinter import *
from functools import partial
from lecture_partition import *

note = {'DO': 264, 'RE': 495, 'MI': 440, 'FA': 396, 'SOL': 352, 'LA': 330, 'SI': 525, 'Z': 0}
l_duration = {'c': 0.125, 'n': 0.25, 'b': 0.5, 'r': 1}
p = "extend the duration of the previous note by 50 percent"


def in_dic(string, dic):
    for k in dic:
        if k == string:
            return True
    return False


def inverse(song):
    partition = open("partitions.txt", "r")
    content = partition.readlines()
    user_partition = open("user_partition.txt")
    content.append(user_partition.readline())
    for i in content:
        print(i)
    song -= 1
    reader = ""
    frequency = 0
    duration_1 = 0
    for i in range(0, len(content[song])):
        j = i + 2
        reader += content[song][i]
        if in_dic(reader, note):
            frequency = note[reader]
            reader = ""
        elif in_dic(reader, l_duration):
            duration_1 = l_duration[reader]
            reader = ""
        elif reader == " ":
            reader = ""
        if reader == "p":
            duration_1 *= 1.5
            reader = ""
        if frequency != 0 and duration_1 != 0 and content[song][j] != "p":
            sound(frequency, duration_1)
            frequency = 0
            duration_1 = 0
    partition.close()


def markov_chaine():
    var = ""


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
