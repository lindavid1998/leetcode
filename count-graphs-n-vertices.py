MOD = 10 ** 9 + 7

a = 0.1 + 0.2
print(a)
print(a == 0.3)

def pow(a, b, mod = MOD):
	res = 1
	while b > 0:
		if b % 2:
			res = (res * a) % mod
		a = (a * a) % mod
		b = b // 2

	return res


print(pow(2, 13))


def countGraphs(n):
	numEdges = n * (n - 1) // 2
	res = pow(2, numEdges, MOD)
	return res

print(countGraphs(4));
print(countGraphs(97319));
