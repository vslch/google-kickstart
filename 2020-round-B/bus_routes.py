if __name__ == "__main__":
    T = int(input())
    for i in range(1, T + 1):
        N, D = map(int, input().split())
        X = list(map(int, input().split()))
        for j in range(N - 1, -1, -1):
            D -= D % X[j]
        ans = "Case #%s: %s" % (i, D)
        print(ans)