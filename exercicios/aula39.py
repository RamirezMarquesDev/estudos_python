"""
Iterando strings com while
"""
#       012345678910
nome = 'Ramirez Marques'  # Iteráveis
#      1110987654321
# tamanho_nome = len(nome)
# print(nome)
# print(tamanho_nome)
# print(nome[3])

# nova_string = ''
# nova_string += '*L*u*i*z* *O*t*á*v*i*o'
contador = 0
nova = ''

while contador < len(nome):
    
    nova += f'*{nome[contador]}'
    contador += 1

nova += '*'
print(nova)


