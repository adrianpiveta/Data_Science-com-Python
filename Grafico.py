#Antes intalamos na venv com o pyhton -m pip install matplotlib
from matplotlib import pyplot as plt
from collections import Counter


"""
Grafico de linha
years = [2000, 2010, 2011, 2018, 2022, 2026]
gdp = [300.2, 543.2, 1075.4, 2843, 564.0, 665.7]


plt.plot(years, gdp, color='red', marker='o', linestyle='solid')
plt.title("PIB NOminal")
plt.ylabel("Bilhoes de dolares")
plt.show()
"""

"""
Grafico de barras 

filmes = ['Iti a coisa', 'Madagascar', 'A era do gelo']
numero_oscars = [3, 0, 9]
plt.bar(range(len(filmes)), numero_oscars)

plt.title("Filmes favoritos")
plt.ylabel("Numero de Oscars")
plt.xticks(range(len(filmes)), filmes)
plt.show()
"""

"""
Cria distribuição das notas
from collections import Counter
#grades = [6,89, 58,44, 55, 66, 88, 5, 69, 10, 15 ,15, 13]
grades = [11, 95, 91, 87, 70, 0, 15, 82, 10, 67, 73, 77, 0]
#Agrupamento de notas por Decil, 100 é colocado com o 90
histogram = Counter(min(grade // 10 * 10, 90) for grade in grades)
plt.bar([x+5 for x in histogram.keys()], #Mova a barra para direita em 5
histogram.values(), ##atribuicao de altura de cada barra
10, #Atribuido valor 10 a cada barra
edgecolor=(0,0,0)) #Cor preta na borda da barra
plt.axis([-5, 105, 0, 5]) #Eixo x de -5 a 105, eixo y de 0 a 5
plt.xticks([10 * i for i in range(11)]) #Rotula x de 10 em 10, de 0.. 100
plt.xlabel("Decile")
plt.ylabel("# of Students")
plt.title("Distribuicao de notas do 1º exame")
plt.show()
"""

"""
# Adulteração no eixo Y
mencoes = [500, 505]
anos = [2021, 2022]
plt.bar(anos, mencoes, 0.8)
plt.xticks(anos)#grafico em barras dos anos
plt.ylabel("#Numero de vezes que eu ouvi sobre ciencia de dados")
plt.ticklabel_format(useOffset=False)
plt.axis([2019, 2023, 499, 507]) #Eixo y plotado com o "zero" em 499
plt.title("Veja este 'gigante' crescimento")
plt.show()
"""


#Grafico de linhas
variancia = [1, 2, 4, 8, 16, 32, 64, 128, 256]
inverso = [256, 128, 64, 32, 16, 8, 4, 2, 1]
erro_total = [x+y for x, y in zip(variancia, inverso)]
xs = [i for i in enumerate(variancia)]
#podemos plotar varias camadas com plt.plot
plt.plot(xs, variancia, 'g-', label='variancia') #Linha verde solida
plt.plot(xs, inverso, 'r-.', label='Inverso') #Linha vermelha de pontos tracejado
plt.plot(xs, erro_total, 'b:', label='Erro total') # Linha pontilhada azul

plt.legend(loc=9)#Legenda
plt.xlabel("Complexidade de modelo")
plt.xticks([])
plt.title("A varianca")
plt.show()

