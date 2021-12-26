nome = input('Digite um nome: ')
name = nome.split()
silva = 'SILVA'
count = 0
for i in name:

    if name[count].upper() == silva:
        print('Há silva no nome!\n\n\n')
        break
    count += 1

# forma de pessoas normais
print('Há silva no nome? {}'.format('silva' in nome.lower()))
