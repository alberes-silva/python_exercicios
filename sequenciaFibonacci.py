numero = int(input('Digite o valor da sequência desejada: '))

contador = 3
priSeq = 0
segSeq = 1

print(f'{priSeq} -> {segSeq}', end='')
while contador <= numero:
    tercSeq = priSeq + segSeq
    print(f' -> {tercSeq}', end='')
    priSeq = segSeq
    segSeq = tercSeq
    contador +=1
