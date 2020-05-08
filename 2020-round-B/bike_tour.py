if __name__ == "__main__":
    T = int(input())
    for i in range(1, T + 1):
        _ = int(input())
        H = list(map(int, input().split()))
        res = sum(
            a < b and b > c 
            for a, b, c in zip(H, H[1:], H[2:])
        )
        ans = "Case #%s: %s" % (i, res)
        print(ans)