import sys
from heapq import heapify, heappop, heappush
from typing import List, Dict
from collections import defaultdict


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


t_: int = int(sys.stdin.readline().strip())
for _ in range(t_):
	distinct_short_songs: List[int] = []  # band wise songs
	discography: Dict[int, List[int]] = defaultdict(list)  # band wise songs
	ns = int(sys.stdin.readline().strip())  # shortest distinct band songs
	# total songs
	# Store song lengths in band heaps
	for a_ in range(ns):
		band, length = map(int, sys.stdin.readline().strip().split(' '))
		if band in discography:
			heappush(discography[band], length)
		else:
			heapify(discography[band])
			heappush(discography[band], length)
	# Pop out the smallest song from the band heap
	for band in discography:
		short_song = heappop(discography[band])
		distinct_short_songs.append(short_song)
	# sort the distinct songs

	distinct_short_songs.sort()

	cost(discography, distinct_short_songs)
