import random


def present_or_not(x, V):
	flag = 0
	for i in range(len(V)):
		if x == V[i]:
			flag = 1
	return flag


def check_distinct_genius(L, H):
	# H = create_movie_theatre(len(L))
	flag = 1
	for i in range(L):
		seat_number = L[i] % len(L)
		if present_or_not(L[i], H[seat_number]):
			flag = 0
		H[seat_number].append(L[i])
	return flag


def test_aadhar():
	def gen_aadhar():
		num = random.random() * (10 ** 12)
		num = int(num)
		return num

	aa_db = [None] * 1000
	for _ in range(10 ** 8):
		aadhr = gen_aadhar()
		aadhr_grp: int = aadhr % 1000
		if aa_db[aadhr_grp] is not None:
			if aadhr not in aa_db[aadhr_grp]:
				aa_db[aadhr_grp].append(aadhr)
		else:
			aa_db[aadhr_grp] = [aadhr]
	return aa_db


aa_db1 = test_aadhar()
with open('aadhrs', 'w') as dump:
	for aadhar in aa_db1:
		for a in aadhar:
			dump.write(f'{aadhar}'+'\n')

