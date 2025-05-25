n = int(input())

meeting = []

for i in range(n):
    a, b = map(int, input().split())
    meeting.append([a, b])


meeting.sort(key=lambda x: (x[1], x[0]))

endPoint = 0
result = 0

for start, end in meeting:
    if endPoint <= start:
        result += 1
        endPoint = end

print(result)
