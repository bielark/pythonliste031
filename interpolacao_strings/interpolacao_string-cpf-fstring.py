cpf = "3655521304" #cpf e do tipo str

print("cpf inserido:{}".format(cpf))

if len(cpf)< 11:
    cpf = cpf.zfill(11)
    print(f"cpf com funçao zfill(11):{cpf}")

cpf_formatado = f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"
print(f"cpf formatado:{cpf_formatado}")













