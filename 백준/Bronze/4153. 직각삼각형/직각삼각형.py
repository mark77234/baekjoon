while True:
    a, b, c = map(int, input().split())

    if a == 0 and b == 0 and c == 0:
        break
    if (a * a + b * b) == c * c:
        print("right")
    elif (c * c + b * b) == a * a:
        print("right")
    elif (c * c + a * a) == b * b:
        print("right")
    else:
        print("wrong")
