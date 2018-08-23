# Importando todas funções do arquivo NumerosPrimos e colocando alias de np
import NumeroPrimo as np

# Importando todas funções do arquivo Apresentação e colocando alias de ap
import Apresentacao as ap


#Atribuindo a variavel numero uma chamada da função InserirNumero
numero = np.InserirNumero()

#Atribuindo a variavel primos uma chamada da função CalcularNumerosPrimos passando variavel numero como parametro
primos = np.CalcularNumerosPrimos(numero)

#Chamando a função ApresentarValores passando variavel primos como parametro
ap.ApresentarValoresTerminal(primos)
ap.ApresentarValoresGraficoBarras(primos)








