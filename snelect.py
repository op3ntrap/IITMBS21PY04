from sys import stdin, stdout
from typing import List


def print_ans(answer):
	if type(answer) != str:
		stdout.write(str(answer))
	else:
		stdout.write(answer)


def read_var():
	var = int(stdin.readline().strip())
	return var


def read_list() -> List[int]:
	var_seq = list(map(int, stdin.readline().strip().split(' ')))
	return var_seq


def read_pairs():
	a, b = tuple(map(int, stdin.readline().strip().split(' ')))
	return a, b


from collections import defaultdict

t = read_var()


def solve(x: str):
	s = defaultdict(bool)
	m = defaultdict(bool)
	nm = 0  # Total Mongoose
	nds = 0
	sm = len(x)
	for i, _p in enumerate(x):
		if _p == 'm':
			nm += 1
			if i > 0 and x[i - 1] == 's':
				if s[i - 1] is False:
					m[i] = True  # True mongoose as it ate a snake
					s[i - 1] = True  # True that snake is dead.
					nds += 1
			if i + 1 < sm and x[i + 1] == 's' and s[i + 1] is False:
				if m[i] is False:
					m[i] = True
					s[i + 1] = True
					nds += 1
	ns = sm - (nm + nds)
	if ns > nm:
		print_ans("snakes" + '\n')
	elif nm > ns:
		print_ans("mongooses" + '\n')
	elif nm == ns:
		print_ans("tie" + '\n')


def main():
	for _ in range(t):
		d = stdin.readline().strip()
		solve(d)


if __name__ == '__main__':
	main()
