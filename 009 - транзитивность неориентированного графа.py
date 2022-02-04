class Graph:
	# конструктор
	def __init__(self, v, e):
		# список ребер
		self.list_edge_arr2 = [list(map(int, input().split())) for _ in range(e)]
		# пустая матрица смежности
		self.matrix_adj_arr2n = [[0] * v for _ in range(v)]
		# словарь смежности
		self.dict_adj = dict()
		# print('###########')
		# self.__print_edge()
		# print('###########')
		self.__convert()
		# self.__print()
		print('###########')
		self.__dict_adj_fill()
		print(self.dict_adj)
		print('###########')
		# print(self.__is_trans_3е())
		# print('###########')
		self.__convert_matrix_adj(v)
		# self.__print()
		# print('###########')
		fnd_key = list(self.dict_adj.keys())[0]
		key = int(fnd_key)
		step = int()
		cnt_edge = e
		# print(self.__search_rec(fnd_key, key, self.dict_adj, step, cnt_edge))
		# print('###########')
		print(self.__is_trans(fnd_key, key, self.dict_adj, step, cnt_edge))
		# print('###########')
		
	# вывод списка ребер
	def __print_edge(self):
		for i in self.list_edge_arr2:
			print(*i)
		
	# вывод графа (матрица смежности)
	def __print(self):
		for i in self.matrix_adj_arr2n:
			print(*i)
		
	# конвертация списка ребер в матрицу смежности неорентированного графа
	def __convert(self):
		for i, j in self.list_edge_arr2:
			self.matrix_adj_arr2n[i - 1][j - 1] = 1
		for i in self.list_edge_arr2:
			i.reverse()
		for i, j in self.list_edge_arr2:
			self.matrix_adj_arr2n[i - 1][j - 1] = 1
		for i in self.list_edge_arr2:
			i.reverse()
		
	# конвертация матрицы смежности в словарь смежности	
	def __dict_adj_fill(self):
			for i in range(len(self.matrix_adj_arr2n)):
				for j in range(len(self.matrix_adj_arr2n)):
					if self.matrix_adj_arr2n[i][j]:
						if (i + 1) in self.dict_adj.keys():
							self.dict_adj[i + 1] += [j + 1]
						else:
							self.dict_adj[i + 1] = [j + 1]
							
	# проверка на транзитивность неорентированного графа до трех ребер включительно
	def __is_trans_3е(self):
		arr = list()
		# записываем в массив вершину и инцидентные ей вершины
		for k, v in self.dict_adj.items():
			tmp = [k]
			for i in v:
				tmp.append(i)
			arr.append(tmp)
		# выводим массив для проверки
		# print(arr)
		# если все множества равны то граф транзитивен
		for i in range(1, len(arr)):
			if not set(arr[0]) == set(arr[i]):
				return 'NO'
		return 'YES'
		
	# конвертация матрицы смежности в числовую последовательность матрицы смежности
	def __convert_matrix_adj(self, v):
		for i in range(v):
			for j in range(v):
				if self.matrix_adj_arr2n[i][j]:
					self.matrix_adj_arr2n[i][j] = j + 1

	# рекурсивный поиск заданной вершины в графе
	# сделать обход в одну сторону 
	# (включить условие: вход в ключи и из всех значений выбрать первый раз юольшее потом остальные меньшее)
	def __search_rec(self, fnd_key, key, dictor, step, cnt_edge, check=True):
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
				return self.__search_rec(fnd_key, key, dictor, step, cnt_edge, check=False)
	
	# проверка на транзитивность неорентированного графа
	def __is_trans(self, fnd_key, key, dictor, step, cnt_edge,):
		return self.__search_rec(fnd_key, key, dictor, step, cnt_edge)
		'''
		if 3 >= cnt_edge:
			return self.__is_trans_3е()
		else:
			return self.__search_rec(fnd_key, key, dictor, step, cnt_edge)
		'''
		
if __name__ == '__main__':
	Graph(*list(map(int, input().split())))