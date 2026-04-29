# Lógica e condições
# Se condição verdadeira (IF)
# enao condição falsa (else) 
# If elif e else 

# Exemplo 1
# print ("verificar idade")
# idade = int(input("digite sua idade"))

# if idade >= 18:
#      print("voce é maior de idade")
# elif idade >=16:
#         ptint("voce não é de maior porém pode votar")
# else:
#     print ("voce não é de maior")
    















# Exemplo 3 
# Criar um algoritimo que permita escolher a opção que deseja 
# print("Menu de opção ")
# print ("escolha uma das opções")
# print("filmes F e séries S e X para sair")

# escolha = input("Digite uma opção")

# if  escolha == "F":
#     print("Voce escolheu Filmes")
# elif escolha == "S":
#     print ("Voce escolheu Séries")
# else:
#     print("Voce saiu do programa")

# Exercício 1 
# Criar um algoritimo para realizar a locução de filmes ou séries seguir o modelo anterior. Ao escolher a opção voce
#  deverá perguntar o nome do cliente do filme ou série e quantidade que deseja assim como o valor de aluguel 
# Para filmes R$ 5,00 e para séries R$ 10,00

print ("Filmes e séries")
print ("Escolha uma das opções")
print("Digite F para filmes, S para séries e Y para sair  ")
escolha = input("Digite sua opção \n")

if escolha == "F":
   print ("Voce esta na sessão filmes")
   nome = input("Digite seu nome \n")
   filmes = input("Qual filme deseja? \n")
   qtidade = input("Qual a quantidade deseja? \n")
   valor = int("5")
   print( "Seu aluguel de filme foi concluído \n" , nome ,"O seu filme escolhido \n", filmes , "A quantidade foi \n", qtidade , "E o valor total foi \n", valor )
elif escolha == "S":
     print("Voce esta na sessão séries")
     nome = input("Digite seu nome")
     séries = input("Qual o nome da série que deseja?")
     qtidade = input ("Que a quantidade deseja?") 
     valor = 10 
     print ("Certo! A compra da sua série escolida foi concluída \n" , nome , "A sua série escolida\n"  , séries , "A quantidade foi? \n", qtidade , "E o valor ttal foi: \n ", valor )
else:
     ("Voce saiu do programa")


# Exercício 2
# Loja de Comidas 
# Criar um algoritimo para compra de produtos 
# 1- Comida 
# 2- bebida 
# 3- doces
# Ao escolher as opções cada um terá um valor de porcentagem, comida = 10%, bebida = 5%, doces = 2% 
# calcular porcentagem valor / 100 ou valor * valor / 100 

print ("Bem-vindo a Vilinha!")
print ("Temos comidas, bebidas e Doces")
print ("Para iniciar digite a opção desejada")
print ("Para comida digite 1")
print ("Para Bebidas digite 2") 
print ("Para Doces digite 3")

opção = int(input("Digite sua opção \n" ))
if opção  == 1:
    print("Voce está na sessão de comidas")
    print ("Temos:\n PF, salados e panqueca")
    comida = input("Qual será seu pedido? \n")
    valor = float(input("Digite o valor da comida \n"))
    desconto = valor * 10 / 100
    total = valor - desconto 
    print("Sua compra total foi: \n", total)

elif opção == 2:
    print ("Bebida para acompanhar? Qual voce deseja?")
    print ("As opções que oferecemos são: Coca-cola, Guaraná e Fanta laranja \n" ) 
    bebida = input("Qual voce deseja? \n") 
    valor = float(input("Digite o valor da bebida \n"))
    desconto = valor * 5 / 100
    total = valor - desconto 
    print("Sua compra total foi de: \n", total )

else:
    print("Se desejar temos a sua sobremesa")
    print("Temos paçoca, barra de chocolate ao leite - Lacta e bala halls \n")
    doces = input("Deseja algumas das opções? \n")
    valor = float(input("Digite o valor do doce \n"))
    desconto = valor * 2/  100
    total = valor - desconto 
    print("Sua compra total foi de: \n",valor )

# Exercício 3 
# Calculadora com operadores 
# Sua Calculadora deverá pergntar qual operador ela deseja e calcular os valores desejados 
# operador + -/*

# Exercício 4 
# Calculo de Notas 
# Nossas atividades são por base de calculos em somativa 1 e somativa 2. no final temos um média.
# Acima ou igual a 50 o aluno será aprovado caso contrario reprovado 
# O programa deverá perguntar o nome e as notas e apresentar o resultado final do aluno 

# Exercício 5 
# Criar um algoritimo



