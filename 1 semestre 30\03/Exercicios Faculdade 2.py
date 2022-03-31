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
    print (f'{dias:02d}:{horas:02d}:{minutos:02d}:{segundos:02d}')

#   3. Tempo atual.
if questao == "3" or questao == "todas":
    print(f'a data de hoje é {asctime()}')


#   4. Ordenação de 3 inteiros.
if questao == "4" or questao == "todas":
    numero1 = int(input("qual o primeiro numero?"))
    numero2 = int(input("qual o segundo numero?"))
    numero3 = int(input("qual o terceiro numero?"))
    numeroMax = max(numero1,numero2,numero3)
    numeroMin = min(numero1,numero2,numero3)
    numeroMed = ((((numero1 + numero2 + numero3) - numeroMax) - numeroMin))
    print(f'a ordem de menor para maior é {numeroMin, numeroMed, numeroMax}')


#   5. Calculando o troco.
if questao == "5" or questao == "todas":
    valorAlvo = int(input("qual o valor de centavos?"))
    moedas50 = valorAlvo // 50
    valorAlvo = valorAlvo % 50
    moedas25 = valorAlvo // 25
    valorAlvo = valorAlvo % 25
    moedas10 = valorAlvo // 10
    valorAlvo = valorAlvo % 10
    moedas5 = valorAlvo // 5
    valorAlvo = valorAlvo % 5
    moedas1 = valorAlvo // 1
    print (f'da um total de {moedas50} de 50c, {moedas25} de 25c, {moedas10} de 10c, {moedas5} de 5')
    print (f'e {moedas1} de 1')


#   6. Soma dos dígitos de um inteiro.
if questao == "6" or questao == "todas":
    numeroTotal = str(input("qual o numero?"))
    numero01 = numeroTotal[0]
    numero02 = numeroTotal[1]
    numero03 = numeroTotal[2]
    numero04 = numeroTotal[3]
    numeroResultado = int(numero01) + int(numero02) + int(numero03) + int(numero04)
    print (f'o resultado da soma da {numeroResultado}')


#   7. Centena, dezena, unidade.
if questao == "7" or questao == "todas":
    numeroInicial = input('qual o numero de 3 digitos?')
    centanas = numeroInicial[0]
    dezenas = numeroInicial[1]
    unidades = numeroInicial[2]
    print(f'o numero de centenas é: {centanas} o de dezenas: {dezenas} e o de unidades: {unidades}')


#   8. Centena, dezena, unidade (novamente)
if questao == "8" or questao == "todas":
    valorInicial = int(input("qual o valor de 3 digitos?"))
    centena1 = valorInicial // 100
    dezena1 = ((valorInicial - (centena1 * 100))// 10) * 10
    unidade1 = ((((valorInicial - (centena1 * 100)) - dezena1) // 1)) * 100
    print (f'o numero {valorInicial} inverso é {centena1 + dezena1 + unidade1}')


#   9. Data invertida.
if questao == "9" or questao == "todas":
    data = int(input("qual a data? [DDMMAA]"))
    dia = data // 1000
    mes = (data - (dia * 1000)) // 100
    ano = ((data - (dia * 1000)) - (mes * 100))
    print (f'{ano}{mes}{dia}')
