cidade = str(input('Digite o nome da sua cidade: ')).strip()

print(cidade[:5].upper() == 'SANTO')

if cidade[0].upper() == 'SANTO':
    print('O nome da cidade começa com santo')
else:
    print('O nome da cidade não começa com santo')
