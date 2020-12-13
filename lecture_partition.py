"""partition = open("partitions.txt", "r")
content = partition.readlines()
for i in range(0, len(content)):
    print(content[i])
partition.close()"""

from fct_son_internet import *
from fct_son import *

notes = {'DO': 264, 'RE': 297, 'MI': 330, 'FA': 352, 'SOL': 396, 'LA': 440, 'SI': 495, 'Z': 0}
durations = {'c': 0.125, 'n': 0.25, 'b': 0.5, 'r': 1}
p = "extend the duration of the previous note by 50 percent"


def in_dic(string, dic):
    for k in dic:
        if k == string:
            return True
    return False


partition = open("partitions.txt", "r")
content = partition.readlines()
song = int(input("Which song? give the line number : ")) - 1
reader = ""
frequency = 0
duration = 0
for i in range(0, len(content[song])):
    reader += content[song][i]
    if in_dic(reader, notes):
        frequency = notes[reader]
        reader = ""
    elif in_dic(reader, durations):
        duration = durations[reader]
        reader = ""
    elif reader == " ":
        reader = ""
    elif reader == "p":
        duration *= 1.5
        reader = ""
    elif frequency != 0 and duration != 0:
        sound(frequency, duration)
        frequency = 0
        duration = 0
partition.close()
