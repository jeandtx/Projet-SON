import wave
import math
import binascii
def son(frequence, temps):
    NomFichier = 'son.wav'
    Monson = wave.open(NomFichier,'w') # instanciation de l'objet Monson
    nbCanal = 1    # stéreo
    nbOctet = 1    # taille d'un échantillon : 1 octet = 8 bits
    fech = 44100   # fréquence d'échantillonnage

    frequenceG = frequence
    frequenceD = frequence
    niveauG = 1
    niveauD = 1
    duree = temps

    nbEchantillon = int(duree*fech)
    parametres = (nbCanal,nbOctet,fech,nbEchantillon,'NONE','not compressed')# tuple
    Monson.setparams(parametres)    # création de l'en-tête (44 octets)

    # niveau max dans l'onde positive : +1 -> 255 (0xFF)
    # niveau max dans l'onde négative : -1 ->   0 (0x00)
    # niveau sonore nul :                0 -> 127.5 (0x80 en valeur arrondi)

    amplitudeG = 127.5*niveauG
    amplitudeD = 127.5*niveauD

    for i in range(0,nbEchantillon):
        # canal gauche
        # 127.5 + 0.5 pour arrondir à l'entier le plus proche
        valG = wave.struct.pack('B',int(128.0 + amplitudeG*math.sin(2.0*math.pi*frequenceG*i/fech)))
        # canal droit
        valD = wave.struct.pack('B',int(128.0 + amplitudeD*math.sin(2.0*math.pi*frequenceD*i/fech)))
        Monson.writeframes(valG + valD) # écriture frame

    Monson.close()

    import pygame
    pygame.mixer.init()
    pygame.mixer.Sound("son.wav").play(0, 0, 25)
    while pygame.mixer.get_busy():
        # lecture en cours
        pass

rebig = "jdbnv"
