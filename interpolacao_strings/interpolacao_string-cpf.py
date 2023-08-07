cpf = "3655521304" #cpf e do tipo str

print("cpf inserido:{}".format(cpf))

if len(cpf)< 11:
    cpf = cpf.zfill(11)
    print("cpf com funçao zfill(11):{}".format(cpf))

cpf_formatado = "{}.{}.{}-{}".format(cpf[:3],cpf[3:6],cpf[6:9],cpf[9:])
print("cpf formatado:{}".format(cpf_formatado))













