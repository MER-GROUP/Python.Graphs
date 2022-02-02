class Graph:
	# конструктор
	def __init__(self, v, e):
		# список ребер
		self.list_edge_arr2 = [list(map(int, input().split())) for _ in range(e)]
		# пустая матрица смежности
		self.matrix_adj_arr2n = [[0] * v for _ in range(v)]
		# словарь смежности
		self.dict_adj = dict()
		print('###########')
		self.__print_edge()
		print('###########')
		self.__convert()
		self.__print()
		print('###########')
		self.__dict_adj_fill()
		print(self.dict_adj)
		print('###########')
		print(self.__is_trans_3е(e))
		print('###########')
		self.__convert_matrix_adj(v)
		self.__print()
		print('###########')
		# print(self.__is_trans(self.dict_adj))
		print('###########')
		
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
	def __is_trans_3е(self, e):
		arr = list()
		# записываем в массив вершину и инцидентные ей вершины
		for k, v in self.dict_adj.items():
			tmp = [k]
			for i in v:
				tmp.append(i)
			arr.append(tmp)
		# выводим массив для проверки
		print(arr)
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
	
	# проверка на транзитивность неорентированного графа
	# если вершина имеет два ребра то неорентированный граф транзентивен, иначе нет
	'''
	# не работает
	def __is_trans(self, dictor):
		for i in dictor.values():
			if not 1 < len(i) <3:
				return 'NO'
			else:
				continue
		else:
			return 'YES'
	'''
		
if __name__ == '__main__':
	Graph(*list(map(int, input().split())))