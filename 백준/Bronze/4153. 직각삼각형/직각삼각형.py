while True:
    inputString = input()
    
    if inputString == "0 0 0":
        break
        
    triangle = list(map(int, inputString.split()))

    
    triangle.sort()
    
    # 가장 큰 값을 구한다
    c = triangle[2]
    # 큰 값의 제곱을 구한다
    
    # 나머지 두 값의 제곱을 구한다
    a = triangle[0]
    b = triangle[1]
    
    
    # 만약 더한게 같다면 right
    # 같지 않다면 wrong
    if a**2 + b**2 == c**2 :
        print("right")
    else:
        print("wrong")
