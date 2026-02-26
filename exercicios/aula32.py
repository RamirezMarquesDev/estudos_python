"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
# num1 = input("Digite um número inteiro: ")

# try:

#     num1 = int(num1)
#     if num1 % 2 == 0:
#         print("Número par!")
#     elif num1 % 2 != 0:
#         print("Número Impar!")

# except Exception as e:

#     print(f"Isso não é um número inteiro! {e}")


"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
# horas = input("Informe as Horas: ")
# try:
#     horas = int(horas)
#     if horas >= 0 and horas <= 11:
#         print('Bom dia')
#     elif horas >= 12 and horas <= 17:
#         print('Boa Tarde')
#     else:
#         print('Boa Noite')
# except Exception as e:
#     print(f'Digitou algo errado. {e}')
    

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

# nome = input('Digite seu primeiro nome: ')

# try:
#     if len(nome) < 5:
#         print('Nome Curto')
#     elif len(nome) in range(5,7):
#        print('Nome Normal')
#     else:
#        print('Nome Grande')

# except Exception as e:
#  print(f"Erro: {e}")