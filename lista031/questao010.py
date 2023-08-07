'''10) Fazer um algoritmo que efetue o cálculo do valor de uma prestação em atraso, utilizando a fórmula prestação	=
valor	+	(valor	x	(taxa	:	100)	x	tempo	em	dias)'''


valor = float(input("qual e o valor normal da prestçâos?"))
taxa = float(input("qual e valor da taxa de juros?"))
tempo = float(input("quantos dias de atraso?"))

prestacao = valor + (valor *( taxa / 100) * tempo)

print("o valor da prestaçâo em r$",prestacao)