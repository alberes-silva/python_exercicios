celsiusParaFahrenheit = float(input('Digite a temperatura em graus Celsius: '))

tFahrenheit = (celsiusParaFahrenheit * 1.8) + 32

if 0 < tFahrenheit <= 32:
    print(f'{tFahrenheit} é fria')
elif 33 <= tFahrenheit < 68:
    print(f'{tFahrenheit} é amena')
else:
    print(f'{tFahrenheit} é quente')
