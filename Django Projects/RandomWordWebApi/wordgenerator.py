from random import randrange
import os

class RandomWordGenerator:
	__file='words.txt'
	__data = []
	__size = 0

	def __init__(self):
		"""
		Constructor to open file from __file and store words in __data	
		"""
		if len(self.__data) == 0:
			
			# find location where the project is running
			path = os.path.dirname(__file__)
			path = os.path.join(path, self.__file)
			
			try:
				f = open(path, 'r')
			except FileNotFoundError:
				print("FileNot Found", os.getcwd(), path)
			else:
				for line in f:
					if len(line.strip()) >= 6:
						self.__data.append(line)
				self.__size = len(self.__data)
				f.close()

	def get_word(self):
		if self.__size > 0:
			return self.__data[randrange(self.__size)]
		return "ERROR"

if __name__ == '__main__':
	d = RandomWordGenerator()
	print(d.get_word())
