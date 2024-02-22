import random

numero_aleatorio = random.randint(0,10)
tentativas = 5
tentativas_max = 0

print("Bem vindo ao jogo de adivinhação")
print("Tente adivinhar o número que a tecnologia estas à pensar, de 0 a 10!")

while tentativas > tentativas_max:
    palpite = int(input("Digite seu número"))
    tentativas -= 1
    
    if palpite == numero_aleatorio:
        print("Você ganhou da tecnologia!!")
        break
    elif palpite > numero_aleatorio:
        print("O número é menor")
    else:
        print("O número é maior")
    if tentativas > tentativas_max:
        print(f"Você tem {tentativas} restantes")
    else:
        print(f"Suas tentativas acabaram, o número era {numero_aleatorio}")
print("O jogo acabou")
        