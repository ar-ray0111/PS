def main():
    for i in range(0,5):
        for j in range(0,i):
            print(chr(64+i+j),end="")
        print("\n")
    
main()