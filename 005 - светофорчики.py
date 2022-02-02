class Traffic:
	def __init__(self, n, m):
		# создаем двумерный массив для хранения светофоров на перекрестках
		self.traffic_arr = [[0] for _ in range(n)]
		# считываем перекрестки
		self.crossroad = [list(map(int, input().split())) for _ in range(m)]
		# вызов методов
		self.__algo__()
		self.__print__()
		
	# выводим количество светофоров на каждом перекрестке 
	def __print__(self):
		for i in self.traffic_arr:
			print(*i, end=' ')
	
	# подсчет количества светофоров на каждом перекрестке 
	# если перекресток i и j пересекается с тунелем 1...n то этим перекресткам прибавляем по светофору
	def __algo__(self):
		for i, j in self.crossroad:
			self.traffic_arr[i - 1][0] += 1
			self.traffic_arr[j - 1][0] += 1
		
if __name__ == '__main__':
	Traffic(*list(map(int, input().split())))