#  login authentication

usuario_1 = 'admin'
usuario_1_senha = '123456'

usuario = input('Digite o seu nome de usuário:')
senha = input('Digite a sua senha:')

if usuario == usuario_1 and senha == usuario_1_senha:
    print('Login ok')
else:
    print('Usuário ou senha incorretos')

