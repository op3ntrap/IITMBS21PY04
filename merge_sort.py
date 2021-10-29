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
# MergeSort in Python


def mergeSort(array):
	global inversions
	if len(array) > 1:

		#  r is the point where the array is divided into two subarrays
		mid = len(array) // 2
		low = array[:mid]
		high = array[mid:]

		# Sort the two halves
		mergeSort(low)
		mergeSort(high)

		i = j = k = 0
		global inversions
		# Until we reach either end of either L or M, pick larger among
		# elements L and M and place them in the correct position at A[p..r]
		while i < len(low) and j < len(high):
			if low[i] < high[j]:
				array[k] = low[i]
				i += 1
			else:
				array[k] = high[j]
				inversions += (len(low) - i)
				j += 1
			k += 1

		# When we run out of elements in either L or M,
		# pick up the remaining elements and put in A[p..r]
		while i < len(low):
			array[k] = low[i]
			i += 1
			k += 1

		while j < len(high):
			array[k] = high[j]
			j += 1
			k += 1
	# return inversions


data_le = io.read_var()
data = io.read_list()
# invs = mergeSort(data)
inversions = 0
mergeSort(data)
io.print_ans(inversions)
