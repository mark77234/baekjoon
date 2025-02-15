floor = 1
level = 1

room = int(input())
while True:
    if room > level:
        level += 6 * floor
        floor += 1
    else:
        break

print(floor)
