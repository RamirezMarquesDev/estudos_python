primeiro_valor = input('Digite um valor: ')
segundo_valor = input('Digite outro valor: ')

if primeiro_valor > segundo_valor:
    print(f'Primeiro valor="{primeiro_valor}" é maior que o Segundo Valor="{segundo_valor}"')
elif segundo_valor > primeiro_valor:
    print(f'Segundo valor="{segundo_valor}" é maior que o Primeiro Valor="{primeiro_valor}"')
else:
    print('Nenhuma das condições foi atendida!')