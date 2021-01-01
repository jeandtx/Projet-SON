# Projet Son: Paul Jouvenceau, Saul Delmotte, Jean Doutriaux
# Fichier comportant la fonction qui produit les sons

from time import sleep
import numpy as np
import simpleaudio as sa


# La fonction prend comme argument la frequence de son et sa durée et le joue
def sound(freq, duration):
    # g e t t im e s t e p s f o r each sample , " d u r a t i o n " i s n o te d u r a t i o n in sec on d s
    sample_rate = 44100
    t = np.linspace(0, duration, int(duration * sample_rate), False)
    # g e n e r a t e s i n e wave tone
    tone = np.sin(freq * t * 2 * np.pi)
    # n o rm al i ze t o 24− b i t range
    if freq != 0:
        tone *= 8388607 / np.max(np.abs(tone))
    # c o n v e r t t o 32− b i t da ta
    tone = tone.astype(np.int32)
    # c o n v e r t from 32− b i t t o 24− b i t by b u i l d i n g a new b y t e b u f f e r ,
    # s k i p p i n g eve r y f o u r t h b i t
    # no te : t h i s a l s o works f o r 2−c h annel aud io
    i = 0
    byte_array = []
    for b in tone.tobytes():
        if i % 4 != 3:
            byte_array.append(b)
        i += 1
    audio = bytearray(byte_array)
    print(audio)
    # s t a r t pl a y b a c k
    play_obj = sa.play_buffer(audio, 1, 3, sample_rate)
    # w a i t f o r pl a y b a c k t o f i n i s h b e f o r e e x i t i n g
    play_obj.wait_done()
