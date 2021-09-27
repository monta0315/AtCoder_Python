def solve(a, b, c):
    ans = 0
    for i in range(a, b + 1):
        if i % c == 0:
            ans = i
            return ans

    return ans


def main():
    a, b, c = map(int, input().split())
    ans = solve(a, b, c)
    if ans != 0:
        print(ans)
    else:
        print(-1)


main()
