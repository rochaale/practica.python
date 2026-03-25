import random
words = {
    "programacion": ["python", "variable", "funcion", "bucle"],
    "datos": ["cadena", "entero", "lista"],
    "general": ["programa"]
}
print("¡Bienvenido al Ahorcado!")
print()
print("Categorías disponibles:")
for categoria in words:
    print("-", categoria)
categoria = input("Elegí una categoría: ")
palabras_mezcladas = random.sample(words[categoria], len(words[categoria]))
# Varias rondas
for word in palabras_mezcladas:
    guessed = []
    attempts = 6
    score = 6
    print("\nNueva palabra!")
    while attempts > 0:
        # Mostrar progreso: letras adivinadas y guiones para las que faltan
        progress = ""
        for letter in word:
            if letter in guessed:
                progress += letter + " "
            else:
                progress += "_ "
        print(progress)
        # Verificar si el jugador ya adivinó la palabra completa
        if "_" not in progress:
            print("¡Ganaste!")
            print (f"Tu puntaje final es de: {score}")
            break
        print(f"Intentos restantes: {attempts}")
        print(f"Letras usadas: {', '.join(guessed)}")
        letter = input("Ingresá una letra: ")
        #Con la funcion not isalpha me genera false si no se ingreso un caracter corrercto.
        if len(letter) != 1 or not letter.isalpha(): 
            print("Entrada no válida")
            print()
            continue
        if letter in guessed:
            print("Ya usaste esa letra.")
        elif letter in word:
            guessed.append(letter)
            print("¡Bien! Esa letra está en la palabra.")
        else:
            guessed.append(letter)
            attempts -= 1
            score -= 1
            print("Esa letra no está en la palabra.")
        print()
    else:
        print(f"¡Perdiste! La palabra era: {word}")
        print (f"Tu puntaje final es de: {score}")
print("\nNo quedan más palabras.")