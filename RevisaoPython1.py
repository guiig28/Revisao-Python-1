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

#33 - 

NI = float(input("Digite o número inicial: "))
NF = float(input("Digite o número final: "))
NV = float(input("Digite o número a ser verificado: "))

if (NI <= NV <= NF):
    print("O número esta no intervalo: ")
else:
    print("O número não esta no intervalo: ")

#34 - 

N1 = float(input("Digite o primeiro valor: "))
Op = ""

while (Op != "+" and Op != "-" and Op != "*" and Op != "/"):
    print("\nOperador inválido.\n")
    Op = input("Digite o operador (+, -, *, /): ")

N2 = float(input("Digite o segundo valor: "))

if (Op == "+"):
    print(N1 + N2)
elif (Op == "-"):
    print(N1 - N2)
elif (Op == "*"):
    print(N1 * N2)
elif (Op == "/"):
    print(N1 / N2)

#35 - 

L1 = float(input("Digite o primeiro lado do triângulo: "))
L2 = float(input("Digite o segundo lado do triângulo: "))
L3 = float(input("Digite o terceiro lado do triângulo: "))

if (L1 <= 0 or L2 <= 0 or L3 <= 0): 
    print("Favor digitar valores válidos.")
else:
    if (L1 == L2 == L3):
        print("Triângulo equilátero.")
    elif (L1 == L2 or L1 == L3 or L2 == L3):
        print("Triângulo Isósceles.")
    else: 
        print("Triângulo Escaleno.")

#36 - 

Pw = input("Digite uma senha: ")
ConfirmPw = input("Confirme sua senha: ")

if Pw != ConfirmPw:
    print("As senhas estão diferentes.")
else:
    print("Senha cadastrada com sucesso!")

#37 - 

V = float(input("Digite o valor da compra: "))
Desc = 0

if (V >= 200):
    Desc = 0.4
elif (V >= 100):
    Desc = 0.3
elif (V >= 50):
    Desc = 0.2
elif (V >= 30):
    Desc = 0.1

NovoV = V - (V * Desc)

print("Valor atualizado: {:.2f}" .format(NovoV))

#38 - 

C = input("Digite um caractere: ").upper()

if (C == "A" or C == "E" or C == "I" or C == "O" or C == "U"):
    print("O caractere é uma vogal.")
else: 
    print("O caractere é uma consoante.")

#39 - 

N = input("Digte seu nickname: ")
S = input("Digite sua senha")

NCadastrado = "Nick123"
SCadastrada = "Senha123"

if (N == NCadastrado):
    if (S == SCadastrada):
        print("Login efetuado com sucesso.")
    else: 
        print("Senha inválida")
else: 
    print("Nickname inválido")

#40 - 

Temp = float(input("Digite a temperatura (em °C): "))

if Temp >= 30:
    print("Está muito calor!")
elif Temp >= 22:
    print("Está calor.")
elif Temp >= 18:
    print("Está ameno.")
elif Temp >= 12:
    print("Está frio.")
elif Temp >= 6:
    print("Está muito frio!")
else:
    print("Está congelando!")

#41 - 

N = int(input("Digite um número: "))
M = int(input("Digite um número para verificar se ele é multiplo do primeiro número: "))

if M % N == 0:
    print("{} é multiplo de {}" .format(M, N))
else:
    print("{} não é multiplo de {}" .format(M, N))

#42 - 

X = float(input("Digite o valor de X: "))
Y = float(input("Digite o valor de Y: "))

if (X > 0 and Y > 0):
    print("Primeiro quadrante.")
elif (X < 0 and Y > 0):
    print("Segundo quadrante.")
elif (X < 0 and Y < 0):
    print("Terceiro quadrante.")
elif (X > 0 and Y < 0):
    print("Quarto quadrante.")
elif (X == 0 and Y != 0):
    print("Sobre o eixo Y.")
elif (X != 0 and Y == 0):
    print("Sobre o eixo X.")
else:
    print("Sobre o eixo X e Y.")

#43 - 

N = int(input("Digite um número: "))

if (N % 3 == 0 and N % 5 == 0):
    print("O número é divisível por 3 e por 5.")
elif (N % 3 == 0 and N % 5 != 0):
    print("O número é divisível por 3.")
elif (N % 3 != 0 and N % 5 == 0):
    print("O número é divisível por 5.")
else: 
    print("O número não é divisível por 3 nem por 5.")

#44 - 

I = int(input("Digite sua idade: "))

if I < 6:
    print("O valor da passagem será isenta.")
elif I < 18:
    print("O valor da passagem será de R$ 25,00 (metade do preço)")
else: 
    print("O valor da passagem será de R$ 50,00 (preço cheio)")

#45 - 

Dia = int(input("Digite o dia: "))
Mes = int(input("Digite o mês: "))
Ano = int(input("Digite o ano: "))

if (Mes < 1 or Mes >12):
    print("Mês inválido.")
else:
    if((Dia < 1) 
       or (Mes == 1 and Dia > 31) 
       or (Ano % 4 != 0 and Mes == 2 and Dia > 28) or (Ano % 4 == 0 and Mes == 2 and Dia > 29) 
       or (Mes == 3 and Dia > 31) 
       or (Mes == 4 and Dia > 30)
       or (Mes == 5 and Dia > 31)
       or (Mes == 6 and Dia > 30)
       or (Mes == 7 and Dia > 31)
       or (Mes == 8 and Dia > 31)
       or (Mes == 9 and Dia > 30)
       or (Mes == 10 and Dia > 31)
       or (Mes == 11 and Dia > 30)
       or (Mes == 12 and Dia > 31)):
        print("Dia inválido.")
    else:
        print("Data válida.")

#46 - 

Str1 = input("Digite a primeira string: ")
Str2 = input("Digite a segunda string: ")

Retorno = "A {} possui mais caracteres que a {}, pois possui um total de {} caracteres, enquanto a {} possui {} caracteres."

if (len(Str1) > len(Str2)):
    print(Retorno .format("primeira string", "segunda string", len(Str1), "segunda string", len(Str2)))
elif (len(Str1) < len(Str2)):
    print(Retorno .format("segunda string", "primeira string", len(Str2), "primeira string", len(Str1)))
else:
    print("As strings possuem o mesmo número de caracteres.")