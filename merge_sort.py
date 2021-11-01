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


def mergesort(arr: List[int], length: int):
	_tmp = [0] * length
	return _ms(arr, _tmp, 0, length - 1)


def _ms(lst, tmp, l, hi):
	inversions = 0
	if l < hi:
		mid = (l + hi) // 2
		inversions += _ms(lst, tmp, l, mid)
		inversions += _ms(lst, tmp, mid + 1, hi)
		inversions += merge(lst, tmp, l, mid, hi)
	return inversions


def merge(arr, tmp, l, mid, hi):
	# i = j = k = 0
	i = l
	j = mid + 1
	k = l

	inv = 0

	while i <= mid and j <= hi:
		if arr[i] <= arr[j]:
			tmp[k] = arr[i]
			i += 1
			k += 1
		else:
			tmp[k] = arr[j]
			inv += (mid - i + 1)
			j += 1
			k += 1

	while i <= mid:
		tmp[k] = arr[i]
		i += 1
		k += 1
	while j <= hi:
		tmp[k] = arr[j]
		j += 1
		k += 1
	for _ in range(l, hi + 1):
		arr[_] = tmp[_]
	return inv


# if __name__ == "__main__":
leng = int(input())
data = list(map(int, input().split()))
print(mergesort(data, leng))
