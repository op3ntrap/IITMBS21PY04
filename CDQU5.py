import sys
from sys import stdin, stdout
from typing import List

sys.setrecursionlimit(10 ** 9)


class myIO:
	def __init__(self):
		pass

	def print_ans(self, answer):
		if type(answer) != str:
			stdout.write(str(answer) + '\n')
		else:
			stdout.write(answer + '\n')

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

results = {0: 0, 1: 0, 2: 1, 3: 1}


def cdq5(floor, limit):
	global results
	for x in range(floor, limit):
		results[x] = (results[x - 2] + results[x - 3]) % (10 ** 9 + 1)


def compute(num):
	global results
	if num in results:
		return results[num]
	else:
		aff = compute(num - 2) + compute(num - 3)
		results[num] = aff
	return aff


def fetch(num):
	global results
	return results[num]


# if __name__ == '__main__':
cdq5(4, 10 ** 6)
tests = io.read_var()
for _ in range(tests):
	io.print_ans(results[io.read_var()])
