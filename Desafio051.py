valor = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
decimoPA = valor + (10 - 1) * razao
for i in range(valor, decimoPA + razao, razao):
    print(i, end=' -> ')
