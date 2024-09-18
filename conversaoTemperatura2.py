print('-'*30)
print('Conversar de Temperatura')
print('-'*30)

while True:
    menu = int(input('\nEscolha a opção para realizar a conversão: \n[1] Celsius para Fahrenheit \n[2] Fahrenheit para Celsius \n[3] Sair\nDigite aqui: '))

    
    if menu == 1:
        valor = float(input('Digite o valor da temperatura em Celsius: '))
        celsiusFaherenheit = (valor*1.8) + 32
        print(f'\nA temperatura {valor}º em Celsius é igual {celsiusFaherenheit}º Fahrenheit ')
    elif menu == 2:
        valor = float(input('Digite o valor da tempratura em Faherenheit: '))
        Faherenheitcelsius = (valor-32) / 1.8
        print(f'\nA temperatura {valor}º em Fahrenheit é igual {Faherenheitcelsius:.1f}º Celsius ')
    elif menu == 3:
        print('\nFinalizando a operação')
        break
    else:
        print('\nOpção inválida, tente novamente')
