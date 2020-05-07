def solution(W, H, L, U, R, D):

	if W == 1 or H == 1:
		return 0
	elif L == 1 and R == W:
	    return 0
	elif U == 1 and D == H:
	    return 0
	
	l = 0
	
	if L > 1 and D < H:
	
		if R == W:
			U = 1
		
		s = L + U - 3
		c = 1
		
		for k in range(L - 2):
			c *= (s - k)
			c /= (L - 2 - k)
			
		p = c * .5**s
		
		for k in range(U, D + 1):
			l += p * .5
			p *= (L - 2 + k)
			p /= k
			p *= .5
			
	if U > 1 and R < W:
	
		if D == H:
			L = 1
		
		s = L + U - 3
		c = 1
		
		for k in range(U - 2):
			c *= (s - k)
			c /= (U - 2 - k)
			
		p = c * (.5**s)
		
		for k in range(L, R + 1):
			l += p * .5
			p *= (U - 2 + k)
			p /= k
			p *= .5
		
	return 1 - l

if __name__ == "__main__":
	T = int(input())
	for i in range(T):
		W, H, L, U, R, D = map(int, input().split())
		result = solution(W, H, L, U, R, D)
		answer = "Case #{}: {}".format(i + 1, result)
		print(answer)