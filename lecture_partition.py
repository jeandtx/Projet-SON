# Projet Son: Paul Jouvanceau, Saul Delmotte, Jean Doutriaux
# Le fichier comporte plusieurs fonctions utilisées dans l'interface graphique

from fct_son import *

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

# Cette fonction sert à lire la partition et la jouer en reverse
def inverse(song):
    partition = open("partitions.txt", "r")
    content = partition.readlines()
    user_partition = open("user_partition.txt")
    content.append(user_partition.readline())
    song -= 1
    song_notes = content[song].split()
    song_notes.reverse()
    p_tag = False
    for note_tag in song_notes:
        if note_tag == 'p':
            p_tag = True
            continue
        note = note_tag[:-1]
        dtag = note_tag[-1]
        frequency = frequencies[note]
        duration = durations[dtag]
        if p_tag:
            duration *= 1.5
            p_tag = False
        print(note_tag, frequency, duration)
        sound(frequency, duration)
    partition.close()


# Cette fonction ajoute une nouvelle melodie à la partition
def new_song():
    partition = open("user_partition.txt", "w")
    user = input("Insert your new song: ")
    partition.write(user)
    play(27)


# Cette fonction sert à executer deux fonctions au lieu d'une quand on appuie sur un bouton de l'interface graph
def do():
    new_song()
    play(27)
