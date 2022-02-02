class Graph:
	def __init__(self, n):
		# матрица смежностм ребер
		self.vert_arr2 = [list(map(int, input().split())) for _ in range(n)]
		# пустой список ребер
		self.edge_arr = list()
		# конвертируем матрицу смежности в список ребер
		self.__algo(n)
		# выводим список ребер
		self.__print()
		
	# перевод матрицы смежности ребер в список ребер
	def __algo(self, n):
		# меняем единицы на номера вершин выше главной диагонали и заполняем список ребер
		for i in range(n):
			for j in range(n):
				if self.vert_arr2[i][j] and i <= j:
					#self.vert_arr2[i][j] = j + 1
					#self.edge_arr.append([i + 1, self.vert_arr2[i][j]])
					self.edge_arr.append([i + 1, j + 1])
		
	# вывод списка ребер	
	def __print(self):
		for i in self.edge_arr:
			print(*i)
		
if __name__ == '__main__':
	# ввод количества вершин
	Graph(int(input()))