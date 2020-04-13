def solution(S, N, K, P):
	
	M = [[0] * K for i in range(N)]
	
	for i in range(N):
		v = 0
		w = 0
		for j in range(K):
			v += S[i][j]
			w += 1
			M[i][j] = (v, w)
	
	D = [[0] * (P + 1) for i in range(N + 1)]
	
	for i in range(1, N + 1):
		r = i - 1
		for j in range(1, P + 1):
			D[i][j] = D[i - 1][j]
			for c in range(min(j, K)):
				v, w = M[r][c]
				D[i][j] = max(D[i][j], v + D[i - 1][j - w])
	
	return D[-1][-1]

if __name__ == "__main__":
	T = int(input())
	for i in range(1, T + 1):
		N, K, P = map(int, input().split())
		S = []
		for _ in range(N):
			S.append(list(map(int, input().split())))
		result = solution(S, N, K, P)
		answer = "Case #%s: %s" % (i, result)
		print(answer)