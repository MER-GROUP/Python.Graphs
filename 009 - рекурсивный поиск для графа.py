'''
def search_rec(fnd, vert_key, size):
	print('--------------------')###
	global cnt, stack
	if 1 == size:
		print('stack =',stack)###
		return 'NO'
	elif fnd in dictor[vert_key] and cnt == size:
		print('stack =',stack)###
		print('Ответ Да')###
		return 'YES'
	elif fnd in dictor[vert_key] and cnt > size:
		print('stack =',stack)###
		print('Ответ Нет')###
		return 'NO'
	elif fnd in dictor[vert_key] and cnt < size:
		print('vetka 1')###
		cnt -= 1
		print('cnt =', cnt)###
		if not len(stack):
			stack.extend(dictor[vert_key])
		print('stack =',stack)###
		vert_key = stack.pop(0)
		print('vert_key =', vert_key)###
		return search_rec(fnd, vert_key,size)
	else:
		print('vetka 2')###
		cnt += 1
		print('cnt =', cnt)###
		if not len(stack):
			stack.extend(dictor[vert_key])
		print('stack =',stack)###
		vert_key = stack.pop(0)
		print('vert_key =', vert_key)###
		return search_rec(fnd, vert_key,size)
'''

def search_rec(dictor):
	for i in dictor.values():
		if not 1 < len(i) <3:
			return 'NO'
		else:
			continue
	else:
		return 'YES'
	
# словарь смежности неорентированного графа тест1 +
'''
dictor = {1: [2, 5],
			2: [1, 3],
			3: [2, 4],
			4: [3, 5],
			5: [1, 4]}'''
# словарь смежности неорентированного графа тест2 -
'''
dictor = {1: [2, 3],
			2: [1, 3],
			3: [2, 4],
			4: [3, 2]}'''
# словарь смежности неорентированного графа тест3 -
dictor = {1: [2],
			2: [1, 3],
			3: [2, 4],
			4: [3]}
# словарь смежности неорентированного графа тест4 +
'''
dictor = {1: [2, 3]}'''
print(dictor)
# счетчик
cnt = int(1)
# стэк хранения вершин
stack = list()
# поисковое значение
fnd = list(dictor.keys())[0]
print(fnd)###
# вершина с которой начинаем поиск 
vert_key = int(fnd)
# количество вершин неорентированного графа
size = len(dictor)###
print(size)
# тест
print('#######################')
# s = search_rec(fnd, vert_key, size)
# print(s)
print(search_rec(dictor))