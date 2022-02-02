class Graph:
	def __init__(self, n):
		# количество ребер
		# матрица смежности
		self.edge_arr2 = [list(map(int, input().split())) for _ in range(n)]
		# ввод пустой строки
		input()
		# количество и цвета вершин
		self.vert_color_arr = list(map(int, input().split()))
		# вывод плохих ребер
		print(self.__search(n))
		
	# поиск плохих ребер
	def __search(self, n):
		cnt = int()
		for i in range(n):
			for j in range(n):
				if self.vert_color_arr[i] == self.vert_color_arr[j]:
					continue
				else:
					if self.edge_arr2[i][j]:
						cnt += 1
		return int(cnt / 2)
		
if __name__ == '__main__':
	# ввод количества вершин
	Graph(int(input()))