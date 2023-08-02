'''1) Desenvolver um programa que pergunte ao usuário o seu nome completo e seu sexo. Em seguida, o programa
deve apresentar os dados anteriormente informados.'''

a = input("Qual e seu nome completo?")

b = input("Qual e o seu genero?")

print("bem vindo",a,"do genero",b,"!")















'''10) Fazer um algoritmo que efetue o cálculo do valor de uma prestação em atraso, utilizando a fórmula prestação	=	
valor	+	(valor	x	(taxa	:	100)	x	tempo	em	dias)'''


valor = float(input("qual e o valor normal da prestçâos?"))
taxa = float(input("qual e valor da taxa de juros?"))
tempo = float(input("quantos dias de atraso?"))

prestacao = valor + (valor *( taxa / 100) * tempo)

print("o valor da prestaçâo em r$",prestacao)

