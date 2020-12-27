from fct_son import *

notes = {'DO': 264, 'RE': 297, 'MI': 330, 'FA': 352, 'SOL': 396, 'LA': 440, 'SI': 495, 'Z': 0}
durations = {'c': 0.125, 'n': 0.25, 'b': 0.5, 'r': 1}
p = "extend the duration of the previous note by 50 percent"


def in_dic(string, dic):
    for k in dic:
        if k == string:
            return True
    return False


def play(song):
    partition = open("partitions.txt", "r")
    content = partition.readlines()
    user_partition = open("user_partition.txt")
    content.append(user_partition.readline())
    for i in content:
        print(i)
    song -= 1
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
        if frequency != 0 and duration != 0 and content[song][j] != "p":
            sound(frequency, duration)
            frequency = 0
            duration = 0
    partition.close()
