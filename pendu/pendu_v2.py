import turtle as t

def draw_pendu():
    fenetre = t.Screen()
    fenetre.setup(width=400, height=400, startx=-1, starty=0)
    t.title("Jeu de pendu")
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
    yield
    t.right(90)
    t.forward(15)
    t.up()
    yield
    t.right(90)
    t.down()
    t.circle(20)
    t.left(90)
    t.up()
    t.forward(40)
    yield
    t.down()
    t.right(40)
    t.forward(45)
    t.backward(45)
    t.left(40)
    yield
    t.left(40)
    t.forward(45)
    t.backward(45)
    t.right(40)
    yield
    t.forward(60)
    yield
    t.right(40)
    t.forward(45)
    t.backward(45)
    t.left(40)
    yield
    t.left(40)
    t.forward(45)

def hide_word(word, letter_found):
    return "".join((
        letter if letter in letter_found else '.'
        for letter in word
    ))

def ask_letter():
    while True:
        try_letter = input("Lettre : ")
        if len(try_letter) == 1:
            return try_letter
        else:
            print("Réessayons")

def run(word, drawer=draw_pendu):
    pendu = drawer()
    next(pendu)
    letters_found = {word[0]}
    while True:
        print(hide_word(word, letters_found))
        try_letter = ask_letter()
        letters_found.add(try_letter)
        if try_letter not in word:
            try: next(pendu)
            except StopIteration:
                print("Vous avez perdu !")
                return None
        if letters_found.issuperset(word):
            print("Bravo !")
            return None



if __name__ == "__main__":
    run("independance")
    input()