#Importados o componente pyplot com nome plt, ele pertence a biblioteca matplotlib
from collections import Counter

from matplotlib import pyplot as plt
""""
#Vetor de  dados anos
anos = [1950, 1960, 1970, 1980, 1990, 2000, 2010]

#vetor de dados relativos vetor PIB
pib = [300.2, 543.3, 1075.9, 2862.5, 5979.6, 10289.7, 14958.3]

# crie um gráfico de linhas, anos no eixo x, gdp no eixo y
plt.plot(anos, pib, color='green', marker='o', linestyle='solid')

# adicione um título
plt.title("PIB nominal")

# adicione um rótulo ao eixo y
plt.ylabel("Bilhões de US$")

# label do eixo x
plt.xlabel("Ano")

plt.show()


#Criação de gráfico de barras

#Dados que serão adicionados ao gráfico
qtd_oscars=[4,2,0]
filmes= ['madagascar', 'Os pinguins', 'o exorcista']

#Plotagem do gráfico de barras, mostra a sequencia (range) de elementos legenda
# e dados que serão adicionados, no caso de quantidade de oscars
plt.bar(range(len(qtd_oscars)), qtd_oscars)

#titulo do gráfico
plt.title("Filmes clássicos e quantidade de oscars")

plt.ylabel("Legenda para eixo y")

#Opção de grid no gráfico
plt.grid()

# rotulagem dos filmes com nome dos filmes, centrados na barra
plt.xticks(range(len(filmes)), filmes)

plt.show()


#Historiograma

#Nesse caso serão plotadas notas,
grades = [83, 99, 91, 87, 70, 0, 15, 82, 100, 67, 73, 77, 0]

# Agrupe as notas por decil, mas coloque o 100 com o 90
histogram = Counter(min(grade // 10 * 10, 90) for grade in grades)

# Mova as barras para a direita em 5, faz o transporte do gráfico,
plt.bar([x + 5 for x in histogram.keys()],
    10, #Define largura da barra
    histogram.values()) # Atribua a altura correta a cada barra

#Define coordenadas minimas e maximas de eixo x (-1, 105) e y (0, 5)
plt.axis([-5, 105, 0, 5]) # eixo x de -5 a 105,


plt.xticks([10 * i for i in range(12)]) # Rotula o eixo x em 0, 10, ..., 100
plt.xlabel("Notas")

plt.ylabel("# Numero de estudantes")

plt.title("Distribuição das notas das provas no primeiro ano")
plt.show()


mencoes = [500, 505]
anos = [2009, 2010]

# eixo x, y, largura barra
plt.bar(anos, mencoes, 0.8)

#Cria varetinhas que representam os anos
plt.xticks(anos)

#Etiqueta eixo y
plt.ylabel("Quantidade de menções")

#Sem essa opção, eixo x ficará somente 0,1
plt.ticklabel_format(useOffset=False)

#Define onde começa e termina os eixos x e y
plt.axis([2009, 2010, 499, 510])

plt.title("Aumento enorme") #É verdade este título

plt.show() # Mostra o bonitão
"""

#Vamos ao grafico de linhas

variancia = [1,2,4,8, 16, 32, 64, 128, 256]

contrario=[]
for x in variancia:
    contrario.append(x)

erro = [x + y for x, y in zip(variancia, contrario)]
xs =[i for i in enumerate(variancia)]

#Pode-se chamar diversas vezes a plotagem para se ter diversas séries na mesma plotagem

plt.plot(xs, variancia, 'g-', label='variancia') #Cria linha verde, por isso g-

plt.show()
