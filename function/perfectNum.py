def perfect(m , n):
    for i in range(m, n+1):
        sum = 0
        for j in range(1, i//2 +1):
            if (i%j ==0):
                sum = sum + j
        
        if sum == i :
            print(i)


def main():
    perfect(1, 100)


main()
