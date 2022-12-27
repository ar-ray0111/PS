def main():
    for i in range(1,6):
        for j in range(1,i+1):
            print(j, end = " ")
        for j in range(10, 2*i, -1):
            print(" ", end = ' ')
        for j in range(i, 0, -1):
            print(j, end = " ")
        print("\n")

main()
