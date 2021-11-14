def fgfs(t):
	for _ in range(t):
		n, k = map(int, input().split())
		cust_p = {}
		for c in range(n):
			s, f, p = map(int, input().split())
			if p not in cust_p:
				cust_p[p] = [(s, f)]
			else:
				cust_p[p].append((s, f))

		count = 0
		for v in cust_p.values():
			v.sort(key=lambda x: x[1])
			previous = (0, 0)
			for item in v:
				if item[0] >= previous[1]:
					previous = item
					count += 1
		print(count)


t = int(input())
# total number of test cases
fgfs(t)
