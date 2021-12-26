for i in range(1, 51):
    if i % 2 == 0:
        print('{} '.format(i), end=" ")
print('\n\n')
#modo com menos laços
for i in range(2, 51, 2):
    print('{} '.format(i), end=" ")