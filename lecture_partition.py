# Projet Son: Paul Jouvenceau, Saul Delmotte, Jean Doutriaux
# Le fichier comporte plusieurs fonctions utilisé dans l'interface graphique

from fct_son import *

notes = {'DO': 264, 'RE': 297, 'MI': 330, 'FA': 352, 'SOL': 396, 'LA': 440, 'SI': 495, 'Z': 0}
durations = {'c': 0.125, 'n': 0.25, 'b': 0.5, 'r': 1}
p = "extend the duration of the previous note by 50 percent"

# cette fonction sert a verifier si un element est dans un dictionnaire
def in_dic(string, dic):
    for k in dic:
        if k == string:
            return True
    return False

# Cette fonction sert à lire la partition et la jouer
def play(song):
    partition = open("/Users/jeandtx/Documents/Projet SONN/partitions.txt", "r")
    content = partition.readlines()
    user_partition = open("user_partition.txt")
    content.append(user_partition.readline())
    song -= 1
    # On utilise un reader qui va lire lettre par lettre et se reinitialiser à chaque arguements trouvé
    reader = ""
    frequency = 0
    duration = 0
    for i in range(0, len(content[song])):
        j = i + 2
        reader += content[song][i]
        if in_dic(reader, notes):
            frequency = notes[reader]
            reader = ""
        elif in_dic(reader, durations):
            duration = durations[reader]
            reader = ""
        elif reader == " ":
            reader = ""
        if reader == "p":
            duration *= 1.5
            reader = ""
        # Quand chaque argument à été trouvé on peut appeler la fonction qui joue le son et reinitialiser ces variables
        if frequency != 0 and duration != 0 and content[song][j] != "p":
            sound(frequency, duration)
            frequency = 0
            duration = 0
    partition.close()

# Cette fonction ajoute une nouvelle melodie à la partition
def new_song():
    partition = open("/Users/jeandtx/Documents/Projet SONN/user_partition.txt", "w")
    user = input("Insert your new song: ")
    partition.write(user)
    play(27)

# Cette fonction sert à executer deux fonctions au lieu d'une quand on appuie sur un bouton de l'interface graph
def do():
    new_song()
    play(27)
