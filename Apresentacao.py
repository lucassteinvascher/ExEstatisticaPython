#importa a biblioteca para a plotagem
import matplotlib.pyplot as plt

a = [1,2,3,4,5] #cria array com os valores

#Função para apresentar valor informado por parametro no console
def ApresentarValoresTerminal(valor):
    print(valor)


def ApresentarValoresGraficoBarras(valor):
    # faz a plotagem da barra bar(x,y)
    plt.bar(valor, valor, color='blue')

    # Label do eixo Y
    plt.ylabel('Primos')

    # Label do eixo X
    plt.xlabel('Primos')

    # exibe a plotagem na tela
    plt.show()



