# Projet Son: Paul Jouvanceau, Saul Delmotte, Jean Doutriaux
"""Fichier comportant la fonction qui produit les sons"""

from time import sleep
import numpy as np
import simpleaudio as sa


def sound(freq, duration):
    """La fonction prend comme argument la frequence de son et sa durée et le joue"""
    # gettimesteps for each sample , "duration" is note duration in sec on ds
    sample_rate = 44100
    t = np.linspace(0, duration, int(duration * sample_rate), False)
    # generates in ewave tone
    tone = np.sin(freq * t * 2 * np.pi)
    # normalize to 24−bit range
    if freq != 0:
        tone *= 8388607 / np.max(np.abs(tone))
    # convert to 32−bit data
    tone = tone.astype(np.int32)
    # convert from 32−bit to 24−bit by building a new byte buffer,
    # skipping every fourth bit
    # note: this also works for 2−channel audio
    i = 0
    byte_array = []
    for b in tone.tobytes():
        if i % 4 != 3:
            byte_array.append(b)
        i += 1
    audio = bytearray(byte_array)
    # start playback
    play_obj = sa.play_buffer(audio, 1, 3, sample_rate)
    # wait for playback to finish before exiting
    play_obj.wait_done()
