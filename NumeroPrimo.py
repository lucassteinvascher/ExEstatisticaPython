#Função para receber um numero e retornar o valor inserido
def InserirNumero():
      num = int(input('informe um numero: '))
      return num

#Função que recebe um valor e calcula os numeros primos retroativos do valor informado e retorna em forma de lista
def CalcularNumerosPrimos(numero):
      primos = []
      for i in range(1, numero + 1):
            contador = 0

            for x in range(1, i + 1):
                  if (i % x == 0):
                        contador = contador + 1

            if (contador == 2 or (contador == 1 and i == 1)):
                  primos.append(i)

      return primos

