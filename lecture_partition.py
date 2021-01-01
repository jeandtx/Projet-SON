# Projet Son: Paul Jouvanceau, Saul Delmotte, Jean Doutriaux
""" Le fichier comporte plusieurs fonctions utilisées dans l'interface graphique"""

from fct_son import sound

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
        frequency = frequencies[note]
        duration = durations[dtag]
        if p_tag:
            duration *= 1.5
            p_tag = False
        print(note_tag, frequency, duration)
        sound(frequency, duration)


def new_song():
    """Cette fonction ajoute une nouvelle melodie à la partition"""
    partition = open("user_partition.txt", "w")
    user = input("Insert your new song: ")
    partition.write(user)
    partition.close()
    play(27)
