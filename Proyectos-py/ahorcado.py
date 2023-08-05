import random
import string

from palabras import palabras
from ahorcado_diagramas import vidas_diccionario_visual

def obtener_palabra_valida(palabras):
    # Seleccionar palabra al azar de la lista de palbras validas
    palabra = random.choice(palabras)

    while '-' in palabra or ' ' in palabra:
        palabra = random.choice(palabras)

    return palabra.upper()



def ahorcado():

    print("=======================================")
    print(" ¡Bienvenido(a) al juego del ahorcado! ")
    print("=======================================")

    palabra = obtener_palabra_valida(palabras)

    letras_por_adivinar = set(palabra)   # 'Python' {'P', 'y', 't', 'o', 'n'}
    letras_adivinadas = set() # No {} -> Diccionario
    abecedario = set(string.ascii_uppercase) # no contiene ñ


    vidas = 8 

    while len(letras_por_adivinar) > 0 and vidas > 0:
         # Letras adivinadas
         # ' '.join({'A', 'B', 'C', 'D'})
         print(f"Te quedan {vidas} vidas y has usado estas letras: {' '.join(letras_adivinadas)}")

         # H - L A
         # Mostrar el estado actual de las palabra
         palabra_lista = [letra if letra in letras_adivinadas else '-' for letra in palabra]
         # Mostrar estado del ahoracado
         print(vidas_diccionario_visual[vidas])
         # Mostrar las palabras separadas por un espacio
         print(f"Palabra: {' '.join(palabra_lista)}") 

         letra_usuario = input("Escoge una letra: ").upper()

         # Si la letra escogida por el usuario esta en el
         # abecedario y no esta en el conjunto de letras 
         # que ya se han escogido, se añade la letra al conjunto de letras ingresadas

         if letra_usuario in abecedario - letras_adivinadas:
            letras_adivinadas.add(letra_usuario)

             # Si letra esta en la palabra
             # quitar la letra del conjunto de letras por adivinar
             # sino esta en la palabra, quitar una vida
            if letra_usuario in letras_por_adivinar:
                letras_por_adivinar.remove(letra_usuario)
                print('')
            else:
                vidas = vidas - 1
                print(f"\nTu letra, {letra_usuario} no esta en la palabra.")
        # SI la letra escogida ya fue ingresada 
         elif letra_usuario in letras_adivinadas:
             print("\nYa escogiste esa letra. Por favor escoge una letra nueva")
         else: 
             print("\nEsta letra no es valida")
        
     # EL juego llega a esta linea cuando se adivinan todas las letras
     # de la palabra o cuando se agotan todas las vidas
    if vidas == 0:
        print(vidas_diccionario_visual[vidas])
        print(f"¡Ahorcado! Perdiste. Lo lamento mucho. La palabra era: {palabra}") 
    else:
        print(f"¡Excelente! ¡Adivinaste la palabra {palabra}!")   
    

ahorcado()


