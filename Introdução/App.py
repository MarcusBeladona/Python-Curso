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

nome = input("Seu nome: ")

if 4 < len(nome):
    print("Nome pequeno.")
elif 4 < len(nome) < 6:
    print("Nome normal.")
elif len(nome) >= 6:
    print("Nome grande.")
else:
    print("Não consegui dizer.")
"""

#nome = "Marcus"
# print(nome[:4:2])

'''

# LAÇO WHILE

x = 0

while x < 6:

    if x == 3:
        x += 1
        continue

    print(x)
    x += 1

string = "string"
'''

# [0:1:2] 0 = início, 1 = fim, 2 = quantidade de pulos.
# string[::-1] = gnirts : A string retorna ao contrário.

# Toda string tem código ao contrário também, começando do -1.
#  0  1  2  3  4  5
#  s  t  r  i  n  g
# -6 -5 -4 -3 -2 -1

# LAÇO FOR IN

'''
texto = "João Victor"

for c in texto:
    print(c)

# range(start,stop,step)
for numero in range(1, 51, 1):
    if numero % 2 == 0:
        print(numero)

# pra contar as iterações
for n, numero in enumerate(texto):
    print(n, numero)

texto = "Oh lord of love"
new = ""

for letra in texto:
    if letra == "o":
        new += letra.upper()
    elif letra == "l":
        new += letra.upper()
    else:
        new += letra

print(new)



# LISTAS

# Aceitam misturas de diferentes tipos de variáveis.
lista = [1, 2, 3, 4]

print(lista[3])

# print(lista[:-4:-1])

lista.append(5)

lista.insert(5, 6)
lista.pop(5)

del(lista[4])

print(lista)
print(max(lista), min(lista))

# É possível usar lista[0:0:0] em listas também;

lista_dois = list(range(1, 11))
print(lista_dois)


#FOR / ELSE

char = "B"
nomes = ["Letícia", "Alex", "João"]

for c in nomes:

    if c.upper().startswith(char):
        print(f"Há palavras com {char}.")
        break

else:
    print(f"Não há palavras com {char}.")
    
'''

# SPLIT JOIN ENUMERATE
