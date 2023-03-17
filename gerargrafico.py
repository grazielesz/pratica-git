import numpy as np
import matplotlib.pyplot as plt
from leitorarquivo import LeitorArquivo


def main():
    leitor = LeitorArquivo('data.txt')
    valores = leitor.getValores()
    print(valores)
    plt.ylabel('Valores de entrada')
    plt.xlabel('Amostragem')
    plt.title('Gráfico de linhas')
    i = 0
    for serie in valores:
       plt.plot(serielabel='Série ' + str(i))   
       i += 1
    plt.legend(loc='upper left')
    plt.show()
main()