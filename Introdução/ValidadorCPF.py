# 168.995.350-09

while True:

    cpf = input("CPF: ")

    lista = cpf.split(".")
    cpf = "".join(lista)
    lista = cpf.split("-")
    cpf = "".join(lista)

    soma = 0
    result = 0

    for a, b in enumerate(range(10, 1, -1)):
        soma += int(cpf[a])*b

    cpf_novo = cpf[0:9]

    result = 11 - (soma % 11)

    cpf_novo += "0" if result > 9 else str(result)

    soma = 0
    result = 0

    for a, b in enumerate(range(11, 1, -1)):
        soma += int(cpf[a])*b

    result = 11 - (soma % 11)

    cpf_novo += str(result)

    print("CPF válido.") if cpf == cpf_novo else print("CPF inválido.")
