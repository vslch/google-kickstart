MAX = 1000000000

def solution(P):
	
	X = [0]
	Y = [0]
	C = []
	m = 0
	
	for c in P:
		if c == "E":
			X[-1] += 1
		elif c == "W":
			X[-1] -= 1
		elif c == "N":
			Y[-1] -= 1
		elif c == "S":
			Y[-1] += 1
		elif c.isnumeric():
			m = m * 10 + int(c)
		elif c == "(":
			C.append(m)
			X.append(0)
			Y.append(0)
			m = 0
		elif c == ")":
			c = C.pop()
			x = X.pop()
			y = Y.pop()
			X[-1] += c * x
			Y[-1] += c * y
			
	x = X[-1] % MAX + 1
	y = Y[-1] % MAX + 1 
	
	return x, y

if __name__ == "__main__":
	T = int(input())
	for i in range(1, T + 1):
		P = input()
		x, y = solution(P)
		ans = "Case #%s: %s %s" % (i, x, y)
		print(ans)