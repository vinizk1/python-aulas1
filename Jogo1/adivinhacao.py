import random

def jogar_adivinhacao():
    nivel = int(input("Escolha um nivel de dificuldade(1-Recém nascido, 2-Normal, 3-Doomslayer):"))
    max_numero = 10 if nivel == 1 else 50 if nivel == 2 else 100
    numero_secreto = random.randint(1, max_numero)
    tentativas = 10 if nivel == 1 else 5 if nivel == 2 else 3
    pontos = 1000
    
    print(f"Jogo de adivinhação lv 1 {nivel}")
    print(f"tente adivinhar o numero q a tecnologia esta pensando, de 1 até {max_numero}")
    
    for Tentativa in range(1, tentativas + 1):
        print(f"Tentativa {Tentativa} de {tentativas}")
        palpite = int(input("Diga seu palpite: "))
        
        if palpite < 1 or palpite > max_numero:
            print(f"Digite um numero entre 1 e {max_numero}")
            continue
        
        acertou = palpite == numero_secreto
        maior = palpite > numero_secreto
        menor = palpite < numero_secreto
        
        if acertou:
            print(f"Você ganhou e fez {pontos} pontos.")
            break
        
        else:
            pontos_perdidos = abs(numero_secreto - palpite)
            pontos -= pontos_perdidos
            if maior:
                print("Seu palpite foi maior q o numero secreto")
            elif menor:
                print("Seu palpite foi menor q o numero secreto")
                
    if not acertou:
         print(f"Suas tentativasacabaram, o numero era {numero_secreto}")
    print("Fim de jogo")
            
if __name__ == "__main__":
    jogar_adivinhacao()