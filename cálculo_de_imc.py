print('|',30*'-','|')
print('| CALCULO DE IMC')
print('|',30*'-','|')

nome = input('| Qual o seu nome? ')
peso = float(input('| Informe o seu peso: '))
altura = float(input('| Informe a sua altura: '))
calculo = round(peso/(altura**2),2 )

print('|',30*'-','|')
print(f'| {nome}, o seu IMC é {calculo}.')

if calculo <=18.5:
    print('| Abaixo do Peso')
    print('| Você está abaixo do peso recomendado. Cuidado!')
elif calculo <=24.9:
    print('| Peso Normal')
    print('| Peso ideal! Matenha seus bons hábitos.')
elif calculo <=29.9:
    print('| Sobrepeso')
    print('| Resultado indica sobrepeso. Cuidar da alimentação e da rotina pode ajudar!')
elif calculo <=34.9:
    print('| Obesidade Grau 1')
    print('| Seu IMC indica obesidade grau 1. Com apoio certo, é possível reverter esse quadro.')
elif calculo <=39.9:
    print('| Obesidade Grau 2')
    print('| Cuidado! É hora de buscar apoio e agir! ')
else:
    print('| Obesidade Grau 3')
    print('| Atenção! O seu quadro pode trazer sérios riscos à sua saúde.')

print('|',30*'-','|')