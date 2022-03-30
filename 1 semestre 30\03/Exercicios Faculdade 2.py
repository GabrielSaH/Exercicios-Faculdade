from time import asctime

#   1. Unidades de tempo.
questao = input("qual questao voce gostaria de acessar?")

if questao == "1" or questao == "todas":
    dias = (((int(input("[Digite apenas o numero de dias:]")) * 24) * 60) * 60)
    horas = ((int(input("[Digite apenas o numero de horas:]")) * 60) * 60)
    minutos = (int(input("[Digite apenas o numero de minutos:]")) * 60)
    print(f'da um total de {((((int(input("[Digite apenas o numero de segundos:]"))) + dias) + horas) + minutos)} segundos')

#   2. Unidades de tempo (novamente).
if questao == "2" or questao == "todas":
    segundos = int(input("quantos segundos?"))
    dias = segundos // 86_400
    segundos = segundos % 86_400
    horas = segundos // 3_600
    segundos = segundos % 3_600
    minutos = segundos // 60
    segundos = segundos % 60
    print (f'{dias}:{horas}:{minutos}:{segundos}')

#   3. Tempo atual.
if questao == "3" or questao == "todas":
    print(f'a data de hoje é {asctime()}')


#   4. Ordenação de 3 inteiros.
if questao == "4" or questao == "todas":
    numeros = []
    for x in range (3):
        numeros.append(float(input("qual o valor?")))
