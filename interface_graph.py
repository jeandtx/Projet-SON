from tkinter import *
from lecture_partition import *
from functools import partial


def function():
    print("work")


# remplacer la fonction par le script de lecture partition en le mettant en fonction


# parameters window
window = Tk()
window.title("Projet Son")
window.geometry('1080x750')
window.minsize(750, 500)
window.iconbitmap('logo.ico')
window.config(background='#ABEBC6')

# titre(texte)
welcome = Label(window, text="Choisissez votre morceau", font=('', 40), bg='#ABEBC6', fg='#21618C', pady=40)
welcome.pack(side=TOP)

# boites
morceaux = Frame(window, bg='#ABEBC6')
gauche = Frame(morceaux, bg='#ABEBC6')
droite = Frame(morceaux, bg='#ABEBC6')

# boutons
joyeux_anniversaire = Button(gauche, text="Joyeux anniversaire", font=('', 20), bg='#ABEBC6', fg='#145A32',
                             command=partial(play, 2))
joyeux_anniversaire.pack(fill=X, pady=10)
au_clair_de_la_lune = Button(gauche, text="Au clair de la lune", font=('', 20), bg='#ABEBC6', fg='#145A32',
                             command=partial(play, 4))
au_clair_de_la_lune.pack(fill=X, pady=10)
vive_le_vent = Button(gauche, text="Vive le vent", font=('', 20), bg='#ABEBC6', fg='#145A32', command=partial(play, 6))
vive_le_vent.pack(fill=X, pady=10)
frere_jacques = Button(gauche, text="Frères Jacques", font=('', 20), bg='#ABEBC6', fg='#145A32',
                       command=partial(play, 8))
frere_jacques.pack(fill=X, pady=10)
la_claire_fontaine = Button(gauche, text="À la claire fontaine", font=('', 20), bg='#ABEBC6', fg='#145A32',
                            command=partial(play, 10))
la_claire_fontaine.pack(fill=X, pady=10)
au_feu_les_pompiers = Button(gauche, text="Au feu les pompiers", font=('', 20), bg='#ABEBC6', fg='#145A32',
                             command=partial(play, 12))
au_feu_les_pompiers.pack(fill=X, pady=10)
fais_dodo = Button(droite, text="Fait dodo cola mon p'tit frère", font=('', 20), bg='#ABEBC6', fg='#145A32',
                   command=partial(play, 14))
fais_dodo.pack(fill=X, pady=10)
une_souris_vert = Button(droite, text="Une souris verte", font=('', 20), bg='#ABEBC6', fg='#145A32',
                         command=partial(play, 16))
une_souris_vert.pack(fill=X, pady=10)
a_vous_dirais_je_maman = Button(droite, text="À vous dirais-je Maman", font=('', 20), bg='#ABEBC6', fg='#145A32',
                                command=partial(play, 18))
a_vous_dirais_je_maman.pack(fill=X, pady=10)
le_bon_roi = Button(droite, text="Le bon roi Dagobert", font=('', 20), bg='#ABEBC6', fg='#145A32',
                    command=partial(play, 20))
le_bon_roi.pack(fill=X, pady=10)
bateau_sur_eau = Button(droite, text="Bâteau sur l'eau", font=('', 20), bg='#ABEBC6', fg='#145A32',
                        command=partial(play, 22))
bateau_sur_eau.pack(fill=X, pady=10)
la_mere_michel = Button(droite, text="C'est la mère Michel", font=('', 20), bg='#ABEBC6', fg='#145A32',
                        command=partial(play, 24))
la_mere_michel.pack(fill=X, pady=10)

# image
w = 500
h = 500
image = PhotoImage(file='note.png')
canvas = Canvas(morceaux, width=w, height=h, bg='#ABEBC6', bd=0, highlightthickness=0)
canvas.create_image(w / 2, h / 2, image=image)

morceaux.pack(expand=YES)
gauche.pack(side=LEFT)
canvas.pack(side=LEFT)
droite.pack(side=RIGHT)

# dernier bouton pour creer un morceau
bas = Frame(window, bg='#ABEBC6')
nvx_morceau = Button(bas, text="Créer une nouvelle partition", font=('', 15), bg='#ABEBC6', fg='#145A32',
                     command=do)
nvx_morceau.pack(fill=X)
bas.pack(expand=YES)

# display window
window.mainloop()
