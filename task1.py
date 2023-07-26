# Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, 
# которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества. 
# m — кол-во элементов второго множества. Затем пользователь вводит сами 
# элементы множеств.


# Решение. Cразу размещать вводимые с клавиатуры значения в множества M и N. 
# Затем найти пересечение множеств, таким образом получим множество, где останутся 
# только повторяющиеся элементы. Затем конвертировать полученное множество в список, 
# отсортировать его и вывести результат в консоль. 

n = int(input('Введите количество элементов первого набора чисел: '))
m = int(input('Введите количество элементов второго набора чисел: '))
setN = set()
setM = set()

for i in range(1, n+1):
    setN.add((input(f'Введите {i} элемент множества: ')))
print()
for j in range(1, m+1):
    setM.add((input(f'Введите {j} элемент множества: ')))
print() 
list_1 = list(setN & setM)
list_1.sort()
print(list_1)