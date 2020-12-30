from fct_son import *

note_1 = {'DO' : 264, 'RE': 495, 'MI': 440, 'FA': 396, 'SOL': 352, 'LA': 330, 'SI': 525, 'Z': 0}
duration_1 = {'c': 0.125, 'n': 0.25, 'b': 0.5, 'r': 1}
p = "extend the duration of the previous note by 50 percent"


def in_dic(string, dic):
    for k in dic:
        if k == string:
            return True
    return False


def inverse(song):
    partition = open("/Users/saul/Desktop/Projet-SON-master/partitions.txt", "r")
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
        if in_dic(reader, note_1):
            frequency = note_1[reader]
            reader = ""
        elif in_dic(reader, duration_1):
            duration = duration_1[reader]
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

inverse(24)