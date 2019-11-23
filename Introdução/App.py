# print("Hello World!")

# Comentários

"""

Comentários de bloco

print("Marcus", "Beladona")
print("Alex", "Menezes", sep="-", end="!!")

print("824", "176", "456", sep=".", end="-")
print("30")

print("Olá Jonas, está 'tudo' bem!")



str  # String
int  # Integer
float  # Float
bool  # Boolean

print(type("Hello"), int("10"))  # <class 'str'> , casting

print("Marcus", 19)

nome = "Marcus"
idade = 19
altura = 1.70
peso = 58
de_maior = 19 > 18
imc = peso / altura ** 2

print("Nome", nome, ", idade", idade, ", altura", altura, ", de maior", de_maior)

print(f"Nome: {nome}, idade {idade}, altura {altura}," +
f" é de maior {de_maior}, imc {(peso / altura ** 2):.2f}")

nome = input("Digite nome: ")
idade = int(input("Digite idade: "))

print(f"Olá {nome}, sua idade é {idade} e você nasceu em {2019-idade}.")

"""

a = 2
b = 1

if a > b:
    print("A")
elif a < b:
    print("B")
else:
    print("A = B")

# AND OR NOT IN

if a > b or a == b:
    print("Sim")
else:
    print("Não")

#print("sim") if a > b or a == b else print("não")
