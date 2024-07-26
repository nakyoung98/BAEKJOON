import sys


def count_ord():
    n, n_ord = map(int, sys.stdin.readline().strip().split())
    arr = list(map(int, sys.stdin.readline().strip().split()))
    print(arr)
    find_key = arr[n_ord]
    last_num = -1
    count = 0
    dict_ord = {}
    for i in range(n):
        dict_ord.setdefault(arr[i], []).append(i)

    print(dict_ord)
    dict_ord = dict(sorted(dict_ord.items(), key=lambda item: item[0], reverse=True))
    print(dict_ord)

    for key, value in dict_ord.items():
        print(key, value)
        # 내가 찾고있는 애의 우선순위라면
        if key == find_key:
            # 그리고 그 길이가 1이면
            if len(value) == 1:
                # 순서를
                count += 1
            # 아니라, 만약 -1이면 
            elif last_num < value[0] or last_num > value[-1]:
                count += value.index(n_ord) + 1
            elif last_num > value[0] and n_ord > last_num:
                while True:
                    if value.pop() == n_ord:
                        break
                    count += 1
            else:
                while True:
                    m = value.pop()
                    if m < last_num:
                        value.append(m)
                        break
                    count += 1
                count += value.index(n_ord) + 1
            return count
        
        # 내가 찾고있는 애의 우선순위가 아니면
        else:
            #  
            if last_num < value[0] or last_num > value[-1]:
                last_num = value[-1]
            else:
                new_value = list(value)
                while new_value:
                    n = new_value.pop()
                    if n < last_num:
                        last_num = n
                        break
            count += len(value)


def solution():
    n = int(sys.stdin.readline().strip())
    for i in range(n):
        print(count_ord())


solution()
