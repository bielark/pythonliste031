nome = "Carla Joaquina" # tipo str
idade = 27 # tipo int
altura = 1.759 # tipo float

print(f"tipo de var nome:{type(nome)}")
print(f"tipo de var idade:{type(idade)}")
print(f"tipo de var altura:{type(altura)}")

print("Nome: %s" % nome)
print("Idade: %d" % idade)
print("Altura: %.2f" % altura)
print("%s possui %d anos e tem %.2fm de altura" % (nome,idade,altura))
