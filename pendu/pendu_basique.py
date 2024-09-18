# -*- coding: utf-8 -*-

import turtle as t

fenetre = t.Screen()
fenetre.setup(width=400, height=400, startx=-1, starty=0)
t.title("Jeu de pendu")

# Dessiner la potence
t.up()
t.goto(0,0)
t.forward(10)
t.down()
t.forward(100)
t.backward(50)
t.left(90)
t.forward(170)
t.right(90)
t.forward(70)

mot = "independance"
essai = 7
nb_lettres = 1
dejadonnee = ""

while essai >= 1 and len(mot) != nb_lettres:
    hided_word = mot[0]
    for letter in mot[1:]:
        if letter in dejadonnee:
            hided_word += letter
        else:
            hided_word += '.'
    
    print(f"encore {essai} essais")
    print(hided_word)
    try_letter = input("Lettre ? ").lower()
    if (try_letter in mot) and (try_letter not in dejadonnee):
        nb_lettres += mot.count(try_letter)
    else:
        essai -= 1
        if essai == 6:
            t.right(90)
            t.forward(15)
            t.up()
        elif essai == 5:
            t.right(90)
            t.down()
            t.circle(20)
            t.left(90)
            t.up()
            t.forward(40)
        elif essai == 4:
            t.down()
            t.right(40)
            t.forward(45)
            t.backward(45)
            t.left(40)
        elif essai == 3:
            t.left(40)
            t.forward(45)
            t.backward(45)
            t.right(40)
        elif essai == 2:
            t.forward(60)
        elif essai == 1:
            t.right(40)
            t.forward(45)
            t.backward(45)
            t.left(40)
        elif essai == 0:
            t.left(40)
            t.forward(45)
    
    dejadonnee += try_letter

if len(mot) == nb_lettres:
    print("BRAVO !")
else:
    print("PERDU")
input()