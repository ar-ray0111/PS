



def pal(num):
    temp = num
    sum = 0
    while (num > 0):
        sum = sum*10 + num % 10
        num = num // 10

    if temp == sum:
        return True
    else:
        return False


def recPal(m, r, n):
    print(m, r, n, "before")
    if (m == r and n == 0):
        return True
    if (m!=r and n == 0):
        return False
    print(m, r, n, "after")
    recPal(m, r*10+n%10, n//10)


def main():
    num = int(input())
    print(recPal(num, 0, num))

main()
