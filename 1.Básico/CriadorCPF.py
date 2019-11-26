# 168.995.350-09
from random import randint

while True:
    cpf = str(randint(10000000000, 99999999999))

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

    if cpf == cpf_novo:
        print("CPF válido.")
        print(f"{cpf[0:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}")
        break
