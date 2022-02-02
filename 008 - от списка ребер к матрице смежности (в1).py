class Graph:
	# конструктор
	def __init__(self, n, m):
		# список ребер
		self.edge_arr2 = [list(map(int, input().split())) for _ in range(m)]
		# пустая матрица смежности ребер
		self.vert_arr2 = [[0] * n for _ in range(n)]
		# конвертация списка ребер в матрицу смежности
		self.__convert()
		# вывод матрицы смежности
		self.__print()
		
	# вывод матрицы смежности
	def __print(self):
		for i in self.vert_arr2:
			print(*i)
			
	# конвертация списка ребер в матрицу смежности
	def __convert(self):
		# заполняем матрицу смежности
		for i, j in self.edge_arr2:
			self.vert_arr2[i - 1][j - 1] = 1
		# делаем симметрию относительно главной диагонали
		# сначала сделаем реверс списку ребер
		for i in self.edge_arr2:
			i.reverse()
		# заполняем матрицу смежности обновленным списком ребер
		for i, j in self.edge_arr2:
			self.vert_arr2[i - 1][j - 1] = 1
		
if __name__ == '__main__':
	# ввод количества вершин и ребер
	Graph(*list(map(int, input().split())))