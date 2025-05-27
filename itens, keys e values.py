# Dicionários
    # Utiliza index no formato de keys e values
    # Aceita string, integer, float...

aluno = {
    'nome': 'Giovanna',
    'idade': 27,
    'nota_final': 'A',
    'aprovação': True,
    'matérias': ['Física', 'Matemática', 'Inglês']
}

print(aluno)

print(aluno.get('matérias'))
print(len(aluno))
print(aluno.keys())
print(aluno.values())
print(aluno.items())
