usuarios = [["chanchito", 4],
            ["Felipe", 1],
            ["pulga", 5]]


# nombres = []
# for usuario in usuarios:
#     nombres.append(usuario[0])
# print(nombres)

# nombres = [expresion for item in items]
# map!
# nombres = [usuario[0] for usuario in usuarios]

# filtrar - filter
# nombres = [usuario for usuario in usuarios if usuario[1] > 2]
# filtrar y transformar
# nombres = [usuario[1] for usuario in usuarios if usuario[1] > 2]

# nombres = list(map(lambda usuario: usuario[0], usuarios))
menosUsuarios = list(filter(lambda usuario: usuario[1] > 2, usuarios))
print(menosUsuarios)
