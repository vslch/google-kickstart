def solution(N, K, S):
	
	prev = S[0]
	
	for i in range(1, N):
		dist = S[i] - prev
		prev = S[i]
		S[i] = dist
	
	maxDist = max(S[1:])
	condition = lambda d: sum(z // d - 1 * int(z % d == 0) for z in S[1:]) <= K
	left = 1
	right = maxDist
	
	while (left != right):
		mid = (left + right) // 2
		if condition(mid) == True:
			right = mid
		else:
			left = right if left == mid else mid
					
	return left

if __name__ == "__main__":
	T = int(input())
	for i in range(T):
		N, K = map(int, input().split())
		S = list(map(int, input().split()))
		result = solution(N, K, S)
		answer = "Case #{}: {}".format(i + 1, result)
		print(answer)
		