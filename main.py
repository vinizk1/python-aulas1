nome = input("Digitai-vos vosso nome, por gentileza");
try:
    idade = int(input("Digitai-vos vossa idade, por gentileza"));
#idade = int;
except ValueError:
    print("Você não digitou um numero valído");
print(f"Olá {nome}, você possui {idade} anos.");