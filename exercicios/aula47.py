"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
"""
import os


palavra_secreta = 'ramirez'
acertos = ''
tentativas = 0

while True:
    
    tentativas += 1

    letra_user = input('Digite uma letra: ')
    if len(letra_user) > 1:
        print('Digite apenas uma letra.')
        continue

    if letra_user in palavra_secreta:
        acertos += letra_user
    formada =''
    for letra in palavra_secreta:
        if letra in acertos:
            formada += letra
        else:
            formada += '*'
    print(formada)
    if formada == palavra_secreta:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f'Parabéns, você acertou a palavra secreta "{palavra_secreta}" com {tentativas} tentativas.')
        acertos = ''
        tentativas = 0
        

    
        