print('******************************')
print('*    Jogo da adivinhação     *')
print('******************************')

numero_secreto = 42
total_de_tentativas = 3
rodada = 1

while (total_de_tentativas >= rodada):
    print('Tentativa {} de {}'.format(rodada, total_de_tentativas))
    
    chute = int(input('Digite um número: '))

    print('Você digitou: ', chute)

    acertou = numero_secreto == chute
    maior = numero_secreto < chute
    menor = numero_secreto > chute

    if acertou:
        print('Você acertou')
        break
    elif maior:  
        print('Você errou! O seu chute foi maior que o número secreto')
    elif menor:
        print('Você errou! O seu chute foi menor que o número secreto')
    rodada += 1
print('Fim de jogo')

