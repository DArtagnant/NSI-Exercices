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

#
t.right(90)
t.forward(15)
t.up()

#
t.right(90)
t.down()
t.circle(20)
t.left(90)
t.up()
t.forward(40)

#
t.down()
t.right(40)
t.forward(45)
t.backward(45)
t.left(40)

#
t.left(40)
t.forward(45)
t.backward(45)
t.right(40)

#
t.forward(60)

#
t.right(40)
t.forward(45)
t.backward(45)
t.left(40)

#
t.left(40)
t.forward(45)


input()