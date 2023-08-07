valor1 = 8.75217
valor2 = 73932.6
valor3 = 11.349

print(f"valor 1 :{valor1:f}")

print(f"valor 1: {valor1:.2f}")
print(f"valor 2: {valor2:.2f}")
print(f"valor 3: {valor2:.2f}")

print(f"valor 2: {valor2:,.2f}")

#-------------------------------------

print(f"valor 1: {valor1:10.2f}")
print(f"valor 2: {valor2:10.2f}")
print(f"valor 3: {valor3:10.2f}")

print(f"valor 1: {valor1:010.2f}")
print(f"valor 2: {valor2:010.2f}")
print(f"valor 3: {valor3:010.2f}")

#=======================================


valor4 = 0.7536

print(f"valor 4:{valor4:.1%}")

texto_valor2 = f"R${valor2:_.2f}"
print(f"texto valor 2:{texto_valor2}")

#substituindo o que e ponto por virgular e o que e underlande por ponto
texto_valor_Br = texto_valor2.replace(".",",").replace("_",".")
print(f"texto valor br:{texto_valor_Br}")











