while True:
    a = input()
    num = list(a)
    end = len(num) - 1
    length = len(num)
    if a == "0":
        break

    if length > 3:
        if num[0] == num[end] and num[1] == num[end - 1]:
            print("yes")
        else:
            print("no")
    elif length > 1:
        if num[0] == num[end]:
            print("yes")
        else:
            print("no")
    else:
        print("yes")
