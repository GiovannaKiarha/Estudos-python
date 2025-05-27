# Criando sets
# Similar a listas
# Evita itens duplicados
# Não utiliza index. Então tem como fazer print(num1[0]). Vai dar erro.

list1 = [10, 20, 30, 40, 50]
list2 = [10, 20, 60, 70]

num1 = set(list1)
num2 = set(list2)

print(num1 | num2) # union. Junta retirando os valores repetidos
print(num1 - num2) # difference. Mostra os números não repetidos
print(num1 ^ num2) # symmetric difference. Retira todos os duplicados nas duas listas
print(num1 & num2) # And. Coloca só os duplicados
print(len(num1))
print(len(num2))

# Funções em sets

list1 = set([1, 2, 3, 5, 6])
s1 = {1, 2, 3, 5, 6} # deixa mais limpo e mais curto
s1.add(7) # tem como adicionar diferente de tuple
s1.update({7,8,9,10})
s1.remove(10) # ler documentação do set
s1.discard(9) # mesmo que não tenha o número, ele não dá erro diferente do remove

print(s1)
print(type(list1))

# Sets com strings

set1 = {'a', 'b', 'c'}
set2 = {'a', 'd', 'e'}
set3 = {'c', 'd', 'f'}

set4 = set1.union(set2)
set5 = set1.difference(set3)
set6 = set1.intersection(set2)
set7 = set1.symmetric_difference(set3)

print(set4)
print(set5)
print(set6)
print(set7)

