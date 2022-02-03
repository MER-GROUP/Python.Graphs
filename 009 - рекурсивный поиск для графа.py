# сделать обход в одну сторону 
# (включить условие: вход в ключи и из всех значений выбрать первый раз юольшее потом остальные меньшее)

def search_rec(fnd_key, key, dictor, step, cnt_vert, check=True):
	print('--------------------')###
	# step += 1
	print('fnd_key =', fnd_key)
	print('key =', key)
	print('dictor =', dictor)
	print('step =', step)
	print('cnt_vert =', cnt_vert)
	if 1 >= len(dictor):
		return 'NO'
	else:
		if check:
			key = min(dictor[key])
		else:
			if key not in dictor: 
				return 'NO'
			key = max(dictor[key])
		if step == cnt_vert and fnd_key in dictor[key]:
			return 'YES'
		elif step > cnt_vert:
			return 'NO'
		else:
			step += 1
			return search_rec(fnd_key, key, dictor, step, cnt_vert, check=False)
	
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

fnd_key = list(dictor.keys())[0]
print('fnd_key =', fnd_key)
key = int(fnd_key)
print('key =', key)
print('dictor =', dictor)
step = int()
print('step =', step)
cnt_vert = len(dictor)
print('cnt_vert =', cnt_vert)
print('---------------------------')
print(search_rec(fnd_key, key, dictor, step, cnt_vert))