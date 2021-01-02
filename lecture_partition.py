# Projet Son: Paul Jouvanceau, Saul Delmotte, Jean Doutriaux
# Le fichier comporte plusieurs fonctions utilisées dans l'interface graphique

from fct_son import *
from tkinter import *

frequencies = {'DO': 264, 'RE': 297, 'MI': 330, 'FA': 352, 'SOL': 396, 'LA': 440, 'SI': 495, 'Z': 0}
durations = {'c': 0.125, 'n': 0.25, 'b': 0.5, 'r': 1}


# Cette fonction sert à lire la partition et la jouer
def play(song):
    partition = open("partitions.txt", "r")
    content = partition.readlines()
    user_partition = open("user_partition.txt")
    content.append(user_partition.readline())
    song -= 1
    song_notes = content[song].split()
    for i in range(len(song_notes)):
        if song_notes[i] == 'p':
            continue
        note = song_notes[i][:-1]
        dtag = song_notes[i][-1]
        frequency = frequencies[note]
        duration = durations[dtag]
        j = i + 1
        if j < len(song_notes) and song_notes[j] == "p":
            duration *= 1.5
        # to debug: print(song_notes[j], frequency, duration)
        sound(frequency, duration)
    partition.close()


# Cette fonction ajoute une nouvelle melodie à la partition
def new_song():
    partition = open("user_partition.txt", "w")
    instructions = Tk()
    instructions.title("Create your partition")
    instructions.geometry("600x300")
    rules = Label(instructions, text="Write each notes in capital letters followed by the duration in small seperate "
                                     "all by a space. \nSilence are Z and for durations put the first letter of the "
                                     "silence's name (ex: croche = c) \n And on ONE line !")
    rules.pack(expand=YES)
    text = Text(instructions, height=2)
    text.pack(expand=YES)

    def getTextInput():
        result = text.get("1.0", "end")
        partition.write(result)
        instructions.destroy()

    enter = Button(instructions, text="Enter", command=getTextInput)
    enter.pack(expand=YES)
    instructions.mainloop()


# Cette fonction sert à executer deux fonctions au lieu d'une quand on appuie sur un bouton de l'interface graph
def do():
    new_song()
    play(27)
