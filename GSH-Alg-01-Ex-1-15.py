"""
Como são muitos codigos eu fiz um if para facilitar, so digitar qual exercicio voce quer testar
que ele roda certinho
o comando "todas" vai rodar todas as atividades de uma so vez
alem disso eu fiz tudo usando a interface PyCharm pois o vs code estava dando problemas no meu pc

"""
from math import log, radians, cos, sin, acos, pi, sqrt, tan

questao = input("qual questao voce gostaria de acessar?")
#   1. Endereço completo.
if questao == "1" or questao == "todas":
    print(f'-------------------------------------')
    print(f'| Nome completo:  Gabriel Sá Hences |')
    print(f'| Endereço: Rua Gaspar 82, blumenau |')
    print(f'-------------------------------------')

#   2. Saudação
if questao == "2" or questao == "todas":
    nome = (input("qual o seu nome?"))
    print(f'ola {nome}')

#   3. Área de uma sala
if questao == "3" or questao == "todas":
    larguraSala = float(input('qual a largura da sala? [Em metros]'))
    comprimentoSala = float(input('qual o comprimento da sala? [Em metros]'))
    areaSala = larguraSala * comprimentoSala
    print(f'sua sala tem {areaSala} metros quadrados')

#   4. Área de um terreno.
if questao == "4" or questao == "todas":
    larguraTerreno = float(input("qual a largura do terreno?[Em metros]"))
    comprimentoTerreno = float(input('qual o comprimento do terreno[Em metros]'))
    areaMetros = larguraTerreno * comprimentoTerreno
    areaHectares = areaMetros / 10_000
    print(f'seu terreno tem {areaHectares} Hectares')

#   5. Retorno de recicláveis.
if questao == "5" or questao == "todas":
    vasilhamesM = int(input("quantos vasilhames de um litro voce tem?"))
    vasilhamesG = int(input("quanto vasilhames de mais de um litro voce tem?"))
    vasilhameMLucro = vasilhamesM * 0.10
    vasilhameGLucro = vasilhamesG * 0.25
    total = '%.2f' % round(vasilhameGLucro + vasilhameMLucro, 2)
    print(f'voce recebera um total de {total} R$')

#   6. Conta do almoço
if questao == "6" or questao == "todas":
    custoSuco = float(input('qual o valor do suco?'))
    custoPrincipal = float(input('qual o valor do prato principal?'))
    custoSobremesa = float(input('qual o valor da sobremesa?'))
    total1 = custoSobremesa + custoSuco + custoPrincipal
    taxa = total1 / 10
    total2 = '%.2f' % round(total1 + taxa, 2)
    print(f'voce devera pagar um total de {total2} R$')

#   7. Soma dos n primeiros números positivos
if questao == "7" or questao == "todas":
    numeroInt = int(input('qual o numero inteiro?'))
    resultado = (numeroInt * (numeroInt + 1)) / 2
    print(f'{numeroInt} somado com todos os seus inteiros anteriores da {resultado}')

#   8. Bugigangas e quinquilharias
if questao == "8" or questao == "todas":
    qntBugigangas = int(input('qual a quantidade de bugigangas?'))
    qntQuinquilharias = int(input('qual a quantidade de quinquilharias?'))
    pesoBugigangas = qntBugigangas * 75
    pesoQuinquilharias = qntQuinquilharias * 112
    pesoTotal = pesoQuinquilharias + pesoBugigangas
    print(f'o peso total da {pesoTotal}')

#   9. Juros compostos
if questao == "9" or questao == "todas":
    dinheiroInicial = float(input('qual o valor investido inicialmente?[Apenas numeros]'))
    primeiroAno = round(dinheiroInicial * 1.12, 2)
    segundoAno = round(primeiroAno * 1.12, 2)
    terceiroAno = round(segundoAno * 1.12, 2)
    print(f'voce tera {primeiroAno} no primeiro ano, {segundoAno} no segundo e {terceiroAno} no terceiro')

#   10. Aritmética
if questao == "10" or questao == "todas":

    primeiroInteiro = int(input('qual o primeiro inteiro?'))
    segundoInteiro = int(input('qual o segundo inteiro?'))
    print(f'a soma de {primeiroInteiro} com {segundoInteiro} da {primeiroInteiro + segundoInteiro}')
    print(f'a subtraçao de {segundoInteiro} em {primeiroInteiro} da {primeiroInteiro - segundoInteiro}')
    print(f'o produto de {primeiroInteiro} por {segundoInteiro} é {primeiroInteiro * segundoInteiro}')
    print(f'o quociente de {primeiroInteiro} dividido por {segundoInteiro} é {primeiroInteiro / segundoInteiro}')
    print(f'o resto de {primeiroInteiro} divido po {segundoInteiro} é {primeiroInteiro % segundoInteiro} ')
    print(f'o log de {primeiroInteiro} na base 10 é {log(primeiroInteiro, 10)}')
    print(f'{primeiroInteiro} elevado a {segundoInteiro} é {primeiroInteiro ** segundoInteiro}')

#   11. Distância entre dois pontos na terra
if questao == "11" or questao == "todas":
    lati1 = float(input('qual a latitude do primeiro ponto?[Em graus]'))
    long1 = float(input('qual a longetude do primeiro ponto[Em graus]?'))
    lati2 = float(input('qual a latitude do segundo ponto?[Em graus]'))
    long2 = float(input('qual a longetude do segundo ponto?[Em graus]'))
    lat1 = radians(lati1)
    lon1 = radians(long1)
    lat2 = radians(lati2)
    lon2 = radians(long2)
    cont1 = sin(lat1) * sin(lat2) + cos(lat1) * cos(lon2) * cos(lon1 - lon2)
    cont2 = acos(cont1)
    cont3 = 6371.01 * cont1
    print(f'a ditancia desses dois pontos é de {cont3} KM')

#   12. Área e volume
if questao == "12" or questao == "todas":
    raio = float(input('qual o valor do raio?'))
    area = pi * raio ** 2
    volume = 4 / 3 * pi * raio ** 3
    print(f'um circulo de raio {raio} tem uma area de {area}')
    print(f'uma esfera de raio {raio} tem um volume de {volume}')

#   13. Área de um triângulo
if questao == "13" or questao == "todas":
    base = float(input('qual a base do triangulo?'))
    altura = float(input('qual a altura do triangulo?'))
    areaT = base * altura / 2
    print(f'um triangulo com base {base} e altura {altura} tem como area {areaT}')

#   14. Área de um triângulo (novamente).
if questao == "14" or questao == "todas":
    alturaT1 = float(input('qual a altura do primeiro lado do traingulo?'))
    alturaT2 = float(input('qual a altura do segundo lado do traingulo?'))
    alturaT3 = float(input('qual a altura do terceiro lado do traingulo?'))
    alturaT4 = (alturaT3 + alturaT1 + alturaT2) / 2
    areaT1 = sqrt(alturaT4 * (alturaT4 - alturaT1) * (alturaT4 - alturaT2) * (alturaT4 - alturaT3))
    print(f'um triangulo com esses lados teria uma area de {areaT1}')

#   15. Área de um polígono regular.
if questao == "15" or questao == "todas":
    comprimento = float(input('qual o comprimento de um lado?'))
    numeroLados = float(input('qual o numero de lados?'))
    areaPol = (numeroLados * comprimento ** 2) / (4 * tan(pi / numeroLados))
    print(f'a area desse poligono é de {areaPol}')
