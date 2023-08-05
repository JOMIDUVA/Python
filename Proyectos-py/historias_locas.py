#Concatenar cadenas de caracteres.
#Supongamos que queremos crear una cadena que diga:
#Aprende a programar con ________________.

# organizacion ="FreeCodeCamp"

# print("Aprende a programar con " + organizacion)
# print("Aprende a programar con {}" .format(organizacion))
# print(f"Aprende a programar con {organizacion}") # f-string

#Mad Libs (Historias Locas)

adj = input("Adjetivo: ")
verbo1 = input("verbo1: ")
verbo2 = input("verbo2: ")
sustantivo_plural = input("Sustantivo (plural): ")


madlib = f"¡Programar es tan {adj}! Siempre me emociona porque me encanta {verbo1} problemas. ¡Aprende a {verbo2} con FreeCodeCamp y alcanza tus {sustantivo_plural}!"

print(madlib)