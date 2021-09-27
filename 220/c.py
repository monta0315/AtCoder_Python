def solve(n, a, x):
    num = 0
    SUM = 0
    flag = True
    while flag:
        for i in a:
            SUM += i
            num += 1
            if SUM > x:
                flag = False
                break

    return num

def main():

    n = int(input())
    a = list(map(int, input().split()))
    x = int(input())
    amari = x % sum(a)
    shortcut = int(x / sum(a)) * len(a)
    ans = solve(n, a, amari) + shortcut
    print(ans)


main()
