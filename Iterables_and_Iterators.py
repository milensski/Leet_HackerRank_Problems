from itertools import combinations

if __name__ == '__main__':

    n = int(input())
    letter = input().split()
    k = int(input())

    comb = list(combinations(letter, k))
    cont = 0

    for i in comb:
        print(i)
        if "a" in i:
            cont += 1

    print(f'{cont / len(comb):.3f}')
