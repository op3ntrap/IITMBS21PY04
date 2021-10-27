import heapq
import sys
from collections import defaultdict
from typing import List, Dict


def main():
	t_: int = int(sys.stdin.readline().strip())
	for _ in range(t_):
		s: Dict[int, List[int]] = defaultdict(list)
		main_s: List[int] = []
		ns = int(sys.stdin.readline().strip())  # total songs
		for _ in range(ns):
			b, l = tuple(map(int, sys.stdin.readline().strip().split(' ')))
			heapq.heappush(s[b], l)
		# global distinct songs with min length
		for band in s:
			tmp = heapq.heappop(s[band])
			heapq.heappush(main_s, tmp)

		def cost(non_distinct_songs: Dict[int, List[int]],
		         distinct_songs: List[int]):
			tc = 0  # Total cost
			for i, w in enumerate(distinct_songs):
				tc += (i + 1) * w
			db = len(distinct_songs)
			for o in non_distinct_songs:
				tc += sum(non_distinct_songs[o]) * db
			print(tc)
			return tc

		cost(s, main_s)


if __name__ == '__main__':
	main()
