import random
# ASCII disponivel na internet. adicionei tres aspas simples no inicio e no final
tesoura = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
pedra = '''''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

papel = ''''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''
# input que captura a escolha do usuario e converte para numero com o int (input gera string)
escolha = int(input("Qual vc escolhe? 0 é pedra, 1 é papel e 2 é tesoura\n"))

# mostra qual foi a escolha do usuario
if escolha == 0:
    print(pedra)
elif escolha == 1:
    print(papel)
elif escolha == 2:
    print(tesoura)
else:
    print("Digite um numero valido")
    escolha = int(input("Qual vc escolhe? 0 é pedra, 1 é papel e 2 é tesoura\n"))
   


print("\n O computador jogou:\n")

# codigo parar gerar a jogada do pc (tive que importar o random la em cima)
computador = random.randint(0,2)

if computador == 0:
    print(pedra)
elif computador == 1:
    print(papel)
elif computador == 2:
    print(tesoura)

# logica para saber quem ganhou
if escolha == 0:
    if computador == 0:
        print("\ndeu empate\n")
    elif computador == 1:
        print("\n vc perdeu\n")
    else:
        print("\n vc ganhou\n")
elif escolha == 1:
    if computador == 0:
        print("\nvc ganhou\n")
    elif computador == 1:
        print("\n deu empate\n")
    else:
        print("\n vc perdeu\n")
elif escolha ==2:
    if computador == 0:
        print("\nvc perdeu\n")
    elif computador == 1:
        print("\n vc ganhou\n")
    else:
        print("\n deu empate\n")





