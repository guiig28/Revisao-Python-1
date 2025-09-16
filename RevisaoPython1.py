#1 - 

print("Olá, Mundo!")

#2 - 

Nome = input("Digite seu nome: ")

print("Boas vindas, {}!" .format(Nome))

#3 - 

N1 = float(input("Digite o primeiro número: "))
N2 = float(input("Digite o segundo número: "))

print("A soma dos dois números foi de {}." .format((N1 + N2)))

#4 - 

Nome = input("Digite seu nome: ")

Saudacao1 = "Seja bem vindo, {}!"
Saudacao2 = "Seja bem vinda, {}!"
Saudacao3 = "Boas vindas, {}!"
Opcao = input("Selecione a opção de saudação (entre 1, 2 ou 3):\n1 - {}\n2 - {}\n3 - {}\n\n" .format(Saudacao1, Saudacao2, Saudacao3))

while (Opcao != "1" and Opcao != "2" and Opcao != "3"):
    print("Favor insira uma opção válida.\n")
    Opcao = input("Selecione a opção de saudação (entre 1, 2 ou 3):\n1 - {}\n2 - {}\n3 - {}\n\n" .format(Saudacao1, Saudacao2, Saudacao3))

if (Opcao == "1"):
    print(Saudacao1 .format(Nome))

if (Opcao == "2"):
    print(Saudacao2 .format(Nome))
    
if (Opcao == "3"):
    print(Saudacao3 .format(Nome))

#5 - 

B = float(input("Digite o valor da base do retângulo: "))
A = float(input("Digite o valor da altura do retângulo: "))

if (B <= 0 or A <= 0):
    print("Valor da base ou da altura inválido.")
else:
    print("Área do retângulo: {:.2f}." .format((B * A)))

#6 - 

C = float(input("Digite a temperatura em °C: "))

if (C < -273.15 ):
    print("Temperatura inválida.")
else:
    F = (C * 1.8) + 32
    print("Temperatura em Farenheit: {:.2f}°F." .format(F))

#7 - 

R = float(input("Digite o valor do raio do círculo: "))

if (R <= 0):
    print("Valor do raio inválido.")
else: 
    print("Valor do perímetro do círculo: {:.2f}" .format((2 * 3.14 * R)))

#8 - 

N1 = float(input("Digite o valor da primeira nota: "))
N2 = float(input("Digite o valor da segunda nota: "))
N3 = float(input("Digite o valor da terceira nota: "))

M = (N1 + N2 + N3) / 3

print("Média: {:.2f}" .format(M))

#9 - 

N = float(input("Digite um número: "))

print("O quadrado desse número é: {:.2f}" .format((N * N)))

#10 - 

Boolean = 7 > 3
Int = 2
Float = 3.2
Str = "Hello, World!"

print(type(Boolean))
print(type(Int))
print(type(Float))
print(type(Str))

#11 - 

P = float(input("Digite seu peso: "))
A = float(input("Digite sua altura: "))

if (P <= 0 or A <= 0):
    print("Favor digitar valores válidos.")
else:
    IMC = P / (A ** 2)
    print("IMC: {:.2f}" .format(IMC))

#12 - 

A = input("Digite um valor para a variável A: ")
B = input("Digite um valor para a variável B: ")

Troca = A
A = B
B = Troca 

print("A = {}\nB = {}" .format(A, B))

#13 - 

Anos = int(input("Digite sua idade em anos: "))

if(Anos < 0 ):
    print("Idade inválida.")
else: 
    Dias = Anos * 365
    print("Você nasceu a {} dias (desconsiderando o mês e o dia de nascimento)." .format(Dias))

#14 - 

PreçoAnterior = float(input("Digite o valor do preço anterior: "))
PreçoAtual = float(input("Digite o valor do preço atual: "))

Desc = ((PreçoAnterior - PreçoAtual) / PreçoAnterior) * 100

print("O desconto foi de {:.1f}%" .format(Desc))

#15 - 

B = float(input("Digite o valor da base do triângulo: "))
A = float(input("Digite o valor da altura do triângulo: "))

if (B <= 0 or A <= 0):
    print("Valor da base ou da altura inválido.")
else:
    print("Área do triângulo: {:.2f}." .format(((B * A ) / 2)))

#16 - 

import math

Seg = int(input("Digite um total de segundos: "))

if (Seg < 0): 
    print("Valor de segundos inválido.")
else: 
    Min = math.floor(Seg / 60)
    SegFalt = Seg % 60
    H = math.floor(Min / 60)
    MinFalt = Min % 60

    print("{:02d}:{:02d}:{:02d}" .format(H, MinFalt, SegFalt))

#17 - 

N = int(input("Digite o valor de um número: "))
P = int(input("Digite o valor da potência para elevar o número anterior: "))

print("O valor de {} elevado a {} é {}" .format(N, P, (N ** P)))

#18 - 

Dist = float(input("Digite o valor da distância percorrida (em m): "))
T = float(input("Digite o valor do tempo percorrido (em s): "))

if(Dist < 0 or T < 0):
    print("Favor digitar valores válidos.")
else: 
    VelMed = Dist / T
    print("Velocidade média: {:.2f} m/s." .format(VelMed))

#19 - 

V = float(input("Digite o valor inicial: "))
J = float(input("Digite o valor da porcentagem do juros simples: ")) / 100

if(V <= 0 or J <= 0):
    print("Favor digitar valores válidos.")
else:
    print("Valor do juros ao mês: {:.2f}" .format((V * J)))

#20 - 

Str1 = input("Digite a primeira string: ")
Str2 = input("Digite a segunda string: ")

Concat = Str1 + Str2

print(Concat)

#21 - 

P1 = int(input("Digite a posição do ponto 1: "))
P2 = int(input("Digite a posição do ponto 2: "))
Dist = 0

if (P1 > P2):
    Dist = P1 - P2
else:
    Dist = P2 - P1

print("A distância é de {}" .format(Dist))

#22 - 

R = float(input("Digite o valor do raio da esfera: "))

if (R < 0):
    print("Raio inválido.")
else:
    V = (4 / 3) * 3.14 * (R ** 3)
    print("O volume da esfera é de {:.2f}" .format(V))

#23 - 

R = float(input("Digite o valor em Reais (R$): "))

if (R < 0):
    print("Valor inválido.")
else: 
    D = R * 5.39
    print("U${:.2f}" .format(D))

#24 - 

Dividendo = float(input("Digite o valor do dividendo: "))
Divisor = float(input("Digite o valor do divsor: "))
Resto = Dividendo % Divisor

print("O resto da divisão é de {:.2f}" .format(Resto))

#25 - 

import math 

C1 = float(input("Digite o valor do primeiro cateto: "))
C2 = float(input("Digite o valor do segundo cateto: "))

H = math.sqrt((C1 ** 2) + (C2 ** 2))
print("Hipotenusa: {:.2f}" .format(H))

#26 - 

N = float(input("Digite um número: "))

if (N < 0):
    print("O número é negativo.")
elif (N > 0):
    print("O número é positivo")
else: 
    print("O número é neutro")

#27 - 

I = int(input("Digite sua idade: "))

if (I < 18):
    print("Menor de idade.")
else: 
    print("Maior de idade.")

#28 - 

N = int(input("Digite um número: "))

if (N % 2 == 0):
    print("O número é par.")
else:
        print("O número é ímpar.")

#29 - 

N1 = float(input("Digite o primeiro número: "))
N2 = float(input("Digite o segundo número: "))
N3 = float(input("Digite o terceiro número: "))

if (N1 >= N2 and N1 >= N3):
    print(N1)
elif (N2 >= N1 and N2 >= N3):
    print(N2)
elif (N3 >= N1 and N3 >= N2):
    print(N3)

#30 - 

Nota = float(input("Digite o valor da nota: "))

if Nota >= 6:
    print("Aprovado!")
else:
    print("Reprovado!")

#31 - 

Ano = int(input("Digite o ano: "))

if Ano % 4 == 0:
    print("O ano é bissexto.")
else:
    print("O ano não é bissexto.")

#32 - 

Peso = float(input("Digite seu peso: "))
Alt = float(input("Digite sua altura: "))

if (Peso < 0 or Alt < 0):
    print("Peso ou altura inválidos.")
else:
    IMC = Peso / (Alt ** 2)
    print("Seu IMC é de {:.2f}." .format(IMC))