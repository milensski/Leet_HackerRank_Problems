if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))

    filtered_arr = []
    [filtered_arr.append(x) for x in arr if x not in filtered_arr]
    print(sorted(filtered_arr)[-2])
