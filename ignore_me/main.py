def count(a, n, pair, sum):
	if pair == n:
		return 1 if sum % 2 == 1 else 0
	
	cnt1 = count(a, n, pair + 1, sum + a[pair][0])
	cnt2 = count(a, n, pair + 1, sum + a[pair][1])

	return cnt1 + cnt2


a = [[1, 2], [3, 5], [4, 1]]
ans = count(a, len(a), 0, 0)
print(ans)