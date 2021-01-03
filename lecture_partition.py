# Projet Son: Paul Jouvanceau, Saul Delmotte, Jean Doutriaux
""" Le fichier comporte plusieurs fonctions utilisées dans l'interface graphique"""

from fct_son import sound
from tkinter import *

frequencies = {'DO': 264, 'RE': 297, 'MI': 330, 'FA': 352, 'SOL': 396, 'LA': 440, 'SI': 495, 'Z': 0}
durations = {'c': 0.125, 'n': 0.25, 'b': 0.5, 'r': 1}


def read_partition(song):
    """Lecture des fichiers partition"""
    partition = open("partitions.txt", "r")
    content = partition.readlines()
    partition.close()
    partition = open("user_partition.txt")
    content += partition.readlines()
    partition.close()
    song -= 1
    return content[song].split()


def play(song):
    """Cette fonction sert à lire la partition et la jouer"""
    song_notes = read_partition(song)
    for i,note_tag in enumerate(song_notes):
        if note_tag == 'p':
            continue
        note = note_tag[:-1]
        dtag = note_tag[-1]
        if note not in frequencies or dtag not in durations:
            print("Attention la note %s est invalide", note_tag)
            continue
        frequency = frequencies[note]
        duration = durations[dtag]
        j = i + 1
        if j < len(song_notes) and song_notes[j] == "p":
            duration *= 1.5
        # to debug: print(note_tag, frequency, duration)
        sound(frequency, duration)


def inverse(song):
    """Cette fonction sert à lire la partition et la jouer en reverse"""
    song_notes = read_partition(song)
    song_notes.reverse()
    p_tag = False
    for note_tag in song_notes:
        if note_tag == 'p':
            p_tag = True
            continue
        note = note_tag[:-1]
        dtag = note_tag[-1]
        if note not in frequencies or dtag not in durations:
            print("Attention la note %s est invalide", note_tag)
            continue
        frequency = frequencies[note]
        duration = durations[dtag]
        if p_tag:
            duration *= 1.5
            p_tag = False
        print(note_tag, frequency, duration)
        sound(frequency, duration)


def new_song():
    """Cette fonction ajoute une nouvelle melodie à la partition"""
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
        partition = open("user_partition.txt", "w")
        partition.write(result)
        partition.close()
        play(27)
        instructions.destroy()

    enter = Button(instructions, text="Enter", command=getTextInput)
    enter.pack(expand=YES)
    instructions.mainloop()
