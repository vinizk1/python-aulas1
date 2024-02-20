nome = input("Digitai-vos vosso nome, por gentileza");
try:
    idade = int(input("Digitai-vos vossa idade, por gentileza"));
#idade = int;
except ValueError:
    print("Você não digitou um numero valído");
print(f"Olá {nome}, você possui {idade} anos.");
try:
    n1 = float(input("Ditite um número"));
    n2 = float(input("Ditite um número"));
except ValueError:
    print("Você não digitou um valor válido");
soma = n1+n2;

print(f"o número {n1} mais o número {n2} é igual a {soma}")