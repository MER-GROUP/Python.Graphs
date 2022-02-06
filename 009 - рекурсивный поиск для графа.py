# пример рекурсивного поиска в любом графе (ориентированном и не ориентированном)
# поиск вершины в графе
def search_rec(fnd_key, key, dictor, step, cnt_edge, check=True):
	print('--------------------')###
	# step += 1
	print('fnd_key =', fnd_key)
	print('key =', key)
	print('dictor =', dictor)
	print('step =', step)
	print('cnt_edge =', cnt_edge)
	if 1 >= len(dictor):
		return 'NO'
	else:
		if check:
			key = min(dictor[key])
		else:
			if key not in dictor: 
				return 'NO'
			key = max(dictor[key])
		if step == cnt_edge and fnd_key in dictor[key]:
			return 'YES'
		elif step > cnt_edge:
			return 'NO'
		else:
			step += 1
			return search_rec(fnd_key, key, dictor, step, cnt_edge, check=False)

# определение количества ребер в графе (в словаре смежности)
# для простого графа
def count_edge(dictor):
	res = set()
	for v in dictor.values():
		for i in v:
			res.add(i)
	return len(res)
	
# словарь смежности неорентированного графа тест1 + YES
dictor = {1: [2, 4],
			2: [1, 3],
			3: [2, 4],
			4: [3, 1]}
# словарь смежности неорентированного графа тест2 + YES
dictor = {2: [5],
			5: [2]}
# словарь смежности неорентированного графа тест3 + NO
dictor = {1: [2, 4],
			2: [1, 3],
			3: [2, 4],
			4: [3, 2]}
# словарь смежности неорентированного графа тест4 + NO
dictor = {1: [2],
			3: [4],
			5: [6],
			7: [8]}
# словарь смежности неорентированного графа тест5 + NO
dictor = {1: [2],
			2: [3]}
# словарь смежности неорентированного графа тест6 - NO
dictor = {1: [2],
			2: [1, 3],
			3: [2]}
# словарь смежности неорентированного графа тест7 - NO
dictor = {1: [2],
			2: [1, 3, 4],
			3: [2, 4],
			4: [3, 2]}

fnd_key = list(dictor.keys())[0]
print('fnd_key =', fnd_key)
key = int(fnd_key)
print('key =', key)
print('dictor =', dictor)
step = int()
print('step =', step)
cnt_edge = count_edge(dictor)
print('cnt_edge =', cnt_edge)
print('---------------------------')
print(search_rec(fnd_key, key, dictor, step, cnt_edge))