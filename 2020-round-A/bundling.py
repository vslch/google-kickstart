def commonPrefix(a, b):
	m = min(len(a), len(b))
	r = next((i for i in range(m) if a[i] != b[i]), m)
	return r	

def solution(N, K, S):

	if K == 1:
		return sum(len(x) for x in S)
	
	S = sorted(S)
	X = [0] * (N + 1)
	
	for i in range(1, N):
		X[i] = commonPrefix(S[i - 1], S[i])
	
	maxRank = max(X)
	score = 0
	
	for rank in range(1, maxRank + 1):
		counter = 0
		state = 0
		for idx in range(1, N + 1):
			if state == 0:
				if X[idx] >= rank:
					counter = 2
					state = 1
				else:
					state = 0
			elif state == 1:
				if X[idx] >= rank:
					counter += 1
					state = 1
				else:
					score += counter // K 
					state = 0
					
	return score

if __name__ == "__main__":
	T = int(input())
	for i in range(T):
		N, K = map(int, input().split())
		S = []
		for j in range(N):
			S.append(input())
		result = solution(N, K, S)
		answer = "Case #{}: {}".format(i + 1, result)
		print(answer)