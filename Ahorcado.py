import random

def run():

    images = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
Te quedan 5 oportunidades''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
Te quedan 4 oportunidades''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
Te quedan 3 oportunidades''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
Te quedan 2 oportunidades''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
Te queda 1 oportunidad''', '''
     +---+
     |   |
     O   |
    /|\  |
    / \  |
         |
   =========''']
    db = []

    print("\n                        ************")
    print("                        * Ahorcado *")
    print("                        ************")

    print("\n----------------------REGLAS DEL JUEGO----------------------\n\n-Puedes ecribir en mayusculas o minusculas dependiendo de la palabra.\n-Debes de eligir una palabra antes de empezar.\n-El juego terminara cuando el hombre ya este completamente dibujado.\n-Disfruta el juego :).\n")

    palabra = input("Que palabra deceas adivinar: ")
    db.append(palabra)

    word = random.choice(db)
    spaces = ["_"] * len(word)
    attemps = 0

    while True:
        for character  in spaces:
            print(character, end=" ")
        print(images[attemps])
        letter = input("Elige una letra: ")

        found = False
        for idx, character in enumerate(word):
            if character == letter:
                spaces[idx] = letter
                found = True

        if not found:
            attemps += 1

        if "_" not in spaces:
            
            print("\nLa palabra es " + palabra + "\nGanaste")
            break 
            input()

        if attemps == 6:
            
            print(images[attemps] + "\n¡¡¡AHORCADO!!!")
            print("\nLa palabra era " + palabra + "\nSuerte para la proxima.")
            break 
            input()



if __name__ == '__main__':
    run()