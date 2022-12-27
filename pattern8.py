def main():
    for i in range(1,7):
        for j in range(1, 8-i):
            print(j, end = " ")
        for j in range(1,(2*i - 1)):
            print(" ", end = " ")
        for j in range(7-i,0,-1):
            if i==1 and j == 7-i:
                continue
            print(j, end = " ")
        print("\n")

main()