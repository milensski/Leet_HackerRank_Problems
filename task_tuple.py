

if __name__ == '__main__':
    n = int(input())
    tn = input().split()
    print(hash(tuple(int(i) for i in tn)))