def pell(n):
    if n <= 2:
        return n

    a = 1
    b = 2
    for i in range(3, n + 1):
        c = 2 * b + a
        a = b
        b = c

    return b


def pell2(n):
    if n <= 2:
        return n
    return 2 * pell(n - 1) + pell(n - 2)


def pelldyanamic(n):
    if n <= 2:
        return n
    memo = [0, 1]
    for i in range(2, n + 1):
        memo.append(2 * memo[i - 1] + memo[i - 2])
    return memo[n]


def gardener(m, n):
    memo = []
    for i in range(0, len(m)):
        if n <= m[i][0]:
            n - m[i][0]
            memo.append(m[i])
    return memo


if __name__ == "__main__":
    i = pell(5)
    print(i)
    i = pelldyanamic(5)
    print(i)
    Packs = [(5, 2), (8, 3), (12, 4)]
    n = 25
    i = gardener(Packs, n)
