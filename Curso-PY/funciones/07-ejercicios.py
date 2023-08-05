def no_space(texto):
    nuevo_texto = ""      # funcion que elima espacios en blanco
    for char in texto:
        if char != " ":
            nuevo_texto += char
    return nuevo_texto


def reverse(texto):
    texto_al_reves = ""
    for char in texto:
        texto_al_reves = char + texto_al_reves
    return texto_al_reves


def es_palindromo(texto):
    texto = no_space(texto)
    texto_al_reves = reverse(texto)
    return texto.lower() == texto_al_reves.lower()


print(es_palindromo("Amo la paloma"))
print(es_palindromo("hola mundo"))


# print("Abba", es_palindromo("Abba"))
# print("Reconocer", es_palindromo("Reconocer"))
# print("Amo la paloma", es_palindromo("Amo la paloma"))

# 1.Eliminar los espacios en blanco
# 2.Tome un texto - reverse
# for e interar