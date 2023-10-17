RU = 4207559

# Criando interface do usuário

lista = []

print(f'Bem vindo a Lanchonete do Elizeu Pinheiro França - {RU}')
print('' * 15, 'Cardapio', '' * 15)
print('|  Código   |        Descrição        | Valor |')
print('|    100    |    Cachorro quente      |  9,00 |')
print('|    101    |  Cachorro Quente Duplo  | 11,00 |')
print('|    102    |         X-Egg           | 12,00 |')
print('|    103    |         X-Salada        | 12,00 |')
print('|    104    |         X-Bacon         | 14,90 |')
print('|    105    |         X-Tudo          | 17,00 |')
print('|    200    |   Refrigerante Lata     |  5,00 |')
print('|    201    |       Chá Gelado        |  4,00 |')
soma = 0
while True:
    codigo = int(input('Entre com o codigo desejado:'))
    try:
        if codigo == 100:
            print('Você pediu um Chachorro-Quente no valor de 9,00')
            soma = soma + 9.00
        elif codigo == 101:
            print('Você pediu um Chachorro-Quente Duplo no valor de 11,00')
            soma = soma + 11.00
        elif codigo == 102:
            print('Você pediu um X-Egg no valor de 12,00')
            soma = soma + 12.00
        elif codigo == 103:
            print('Você pediu um X-Salada no valor de 12,00')
            soma = soma + 12.00
        elif codigo == 104:
            print('Você pediu um X-Bacon no valor de 14,00')
            soma = soma + 14.00
        elif codigo == 105:
            print('Você pediu um X-Tudo no valor de 17,00')
            soma = soma + 17,00
        elif codigo == 200:
            print('Você pediu um Refrigerante Lata no valor de 5,00')
            soma = soma + 5.00
        elif codigo == 201:
            print('Você pediu um Chpa Gelado no valor de 4,00')
            soma = soma + 4.00
        else:
            print('Opção incorreta')
            continue
        
    except: 
        print('Digite corretamente')
        continue
    
    pedido = (input('Deseja pedir mais alguma coisa?\n 1 - Sim \n 0 - Não\n'))

    if pedido == '0':
        break
    elif pedido == '1':
        continue
    
print(f'o valor total foi de: {soma:,.2f}')