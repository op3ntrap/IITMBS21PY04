from sys import stdin, stdout
from typing import List


class myIO:
	def __init__(self):
		pass

	def print_ans(self, answer):
		if type(answer) != str:
			stdout.write(str(answer))
		else:
			stdout.write(answer)

	def read_var(self):
		var = int(stdin.readline().strip())
		return var

	def read_list(self) -> List[int]:
		var_seq = list(map(int, stdin.readline().strip().split(' ')))
		return var_seq

	def read_pairs(self):
		a, b = tuple(map(int, stdin.readline().strip().split(' ')))
		return a, b


io = myIO()
given_array = [0, 0, 0]
given_length = 3 + io.read_var()
rf = io.read_list()
given_array = given_array + rf
summation = 0
for i in given_array:
	summation += i
for i in range(3, given_length):
	given_array[i] += min(given_array[i - 1], given_array[i - 2], given_array[i - 3])
print(summation - min(given_array[-1], given_array[-2], given_array[-3]))
