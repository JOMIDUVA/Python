from matplotlib import pyplot as plt
import numpy as np
from matplotlib import pyplot as plt
import matplotlib.pyplot as plt

años = ["2011", "2012", "2013", "2014", "2015",
        "2016", "2017", "2018", "2019", "2020"]
nivel1 = np.random.rand(10) * 100
# nivel2 = np.random.rand(10) * 200 + 100
# nivel3 = np.random.rand(10) * 300 + 200
# nivel4 = np.random.rand(10) * 400 + 300
# nivel5 = np.random.rand(10) * 500 + 400

# # Introducir series de datos con color, marcador, etiqueta y estilo
# plt.bar(años, nivel1, width=1/5)
# plt.bar(años, nivel1, width=1/5)
# plt.bar(años, nivel1, width=1/5)
# plt.bar(años, nivel1, width=1/5)
# plt.bar(años, nivel1, width=1/5)


plt.plot(años, nivel1, label="Nivel 1",
         color="purple", marker="<", linestyle="-")
# plt.plot(años, nivel2, label="Nivel 2",
#         color="red", marker="*", linestyle="--")
# plt.plot(años, nivel3, label="Nivel 3",
#         color="blue", marker="^", linestyle=":")
# plt.plot(años, nivel4, label="Nivel 4",
#         color="black", marker=".", linestyle="-.")
# plt.plot(años, nivel5, label="Nivel 5",
#         color="green", marker="+", linestyle="")


# # Activar leyendas
# plt.legend()
# # Titulo de Grafica
# plt.title("Examen de Certificacion")
# # Etiquetas de los ejes
# plt.xlabel("Años que se han realizado el examen")
# plt.ylabel("Puntaje")

# # Personalizar eje de puntaje de 0 a 1000 en incrementos de 50
# plt.yticks(np.arange(0, 1001, 50))

# # Activar cuadricula
# plt.grid()
# # Activar marcas menores
# plt.minorticks_on()

plt.show()
