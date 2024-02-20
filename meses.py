mes = input("Digite um mes")

if mes in ("dezembro", "janeiro", "fevereiro"):
    estacao = "Verão"
    
if mes in ("março", "abril", "maio"):
    estacao = "Outono"
    
if mes in ("junho", "julho", "agosto"):
    estacao = "Inverno"
    
if mes in ("setembro", "outubro", "novembro"):
    estacao = "Primavera"
    
print(f"Seu mes está na estação do {estacao}")