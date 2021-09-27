def change(num, base):
    num = list(reversed(str(num)))
    SUM = 0
    for i in range(len(num)):
        SUM += int(num[i]) * pow(base, i)

    return SUM


def solve(k, a, b):
    # 入力値を文字列に変換し、一つ一つに対して
    return change(a, k) * change(b, k)


def main():
    k = int(input())
    a, b = map(int, input().split())
    print(solve(k, a, b))


main()
