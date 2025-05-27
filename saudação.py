# saudações

horas = int(input('Digite que horas são:'))

if horas < 12:
    print('Bom dia')
elif 12 < horas < 18:
    print('Boa tarde')
else:
    print('Boa noite')