RU = 4110677

print(f'Bem-Vindo a Loja do Elizeu Pinheiro França - {RU}')

#Loop para pegar o valor e a quantidade de produtos
while True:
    try:
        valor = float(input('Digite o valor dos produtos:'))
        quantidade = float(input('Digite a quantidade dos produtos:'))
    except ValueError:
        print('Você não digitou um valor numerico, tente novamente.')
        continue
    break

valor_bruto = valor * quantidade

print(f'O valor do final sem desconto foi de : R$ {valor_bruto}')

# Realiza-a-validação do desconto e mostra em seguida
if quantidade < 10:
    print(f'O valor com desconto foi de: R$ {valor_bruto}  (desconto 0%)')
elif quantidade >= 10 and quantidade < 100:
    print(f'O valor com desconto foi de: R$ {valor_bruto - valor_bruto * 0.05}  (desconto 5%)')   
elif quantidade >= 100 and quantidade < 1000:
    print(f'O valor com desconto foi de: R$ {valor_bruto - valor_bruto * 0.10}  (desconto 10%)')  
else:
    print(f'O valor com desconto foi de: R$ {valor_bruto - valor_bruto * 0.15}  (desconto 15%)')  