def solution(S, B):
    
    X = {i:0 for i in range(1, 1001)}
    
    for c in S:
        X[c] += 1
        
    n = 0
        
    for i in range(1, 1001):
        t = B // i
        if t == 0:
            break
        else:
            y = min(X[i], t)
            n += y
            B -= y * i
    
    return n
	
if __name__ == "__main__":
	
	T = int(input())
	
	for i in range(T):
		N, B = map(int, input().split())
		S = list(map(int, input().split()))
		answer = solution(S, B)
		print("Case #{}: {}".format(i + 1, answer))