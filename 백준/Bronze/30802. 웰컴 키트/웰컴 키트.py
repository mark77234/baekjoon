N = int(input())
sizes = list(map(int, input().split()))
T, P = map(int, input().split())

Tbundle = 0
for size in sizes:
    Tbundle += size // T
    if size % T != 0:
        Tbundle += 1


Pbundle = N // P
pen = N % P

print(Tbundle)
print(Pbundle, pen)
