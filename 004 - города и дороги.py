class Graph:
	def __init__(self, n):
		# заполнение матрицы смежности графом
		self.arr = [list(map(int, input().split())) for _ in range(n)]
		# вывод количества ребер
		print(self.__edge_count__(n))
		
		# матрица смежности неориентированного графа всегда симметрична относительно главной диагонали, значит сумма всех единиц которые выше или ниже главной диагонали и есть количество ребер (дорог)
	def __edge_count__(self, n):
		sm = int()
		for i in range(n):
			for j in range(n):
				if i < j and self.arr[i][j]:
					sm += 1
		return sm
		
if __name__ == '__main__':
	Graph(int(input()))