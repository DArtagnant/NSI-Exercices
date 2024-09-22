import os
from random import randint

def get_random_word(path):
    #On part du principe que le fichier ne peut pas être entièrement chargé en mémoire
    size = os.path.getsize(path)
    with open(path, 'rb') as file: # Ouvrir en binaire est plus rapide (32.5s vs 47.0s sur 10**6 lancements)
        file.seek(
            randint(0, size)
        )
        file.readline()
        word = file.readline().decode().strip()
        if word == "": #Arrive lorsque l'on tombe sur la dernière ligne
            file.seek(0)
            return file.readline().decode().strip()
        else:
            return word


if __name__ == "__main__":
    from pendu_v2 import run as run_pendu
    WORDS_PATH = "./words/fr.txt"
    word = get_random_word(WORDS_PATH)
    run_pendu(word)