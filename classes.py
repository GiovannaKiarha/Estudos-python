from datetime import datetime
# OOP
    # Classes
        # Utilizadas para criar objetos (instances)
        # Objetos são partes dentro de uma classe (instancias)
        # Classes são utilizadas para agrupar dados e funções, podendo reutilizar
        # ====
        # Class: frutas
        # Objetos: banana, abacate...

# criar a classe
class Funcionarios: # classe
    
    def __init__(self, nome, sobrenome, ano_nascimento):# criando um construtor para reduzir os argumentos
        self.nome = nome
        self.sobrenome = sobrenome
        self.ano_nascimento = ano_nascimento
    
    def nome_completo(self): # adicionando mais função a classe
        return self.nome + ' ' + self.sobrenome

    def idade_funcionario(self):
        ano_atual = datetime.now().year
        return ano_atual - self.ano_nascimento

# criar o objeto
usuario1 = Funcionarios('Elena', 'Cabral', '12/01/2009')
usuario2 = Funcionarios('Carolina', 'Silva', '15/10/2005')
usuario3 = Funcionarios('Giovanna', 'Guerin', '28/10/1997')


#print
print(usuario1.nome)
print(usuario2.nome)
print(usuario1.nome_completo())
print(Funcionarios.nome_completo(usuario1)) # classe + função + parâmetro



# criar os parâmetros do usuário 1
#usuario1.nome = 'Elena'
#usuario1.sobrenome = 'Cabral'
#usuario1.data_nascimento = '12/01/2009'

# criar os parâmetros do usuário 2
#usuario2.nome = 'Carolina'
#usuario2.sobrenome = 'Silva'
#usuario2.data_nascimento = '15/10/2005'



