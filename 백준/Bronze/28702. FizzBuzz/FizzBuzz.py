li = []
for i in range(3):
    a = input()
    li.append(a)

for i in range(3):
    if li[i].isdigit() == True:
        ans = int(li[i]) + 3 - i
        if ans % 3 == 0 and ans % 5 == 0:
            print("FizzBuzz")
            break
        elif ans % 3 == 0:
            print("Fizz")
            break
        elif ans % 5 == 0:
            print("Buzz")
            break
        else:
            print(ans)
            break
