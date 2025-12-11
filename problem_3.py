a = int(input('a='))

if a%2 == 0:
    a-=1
result = []
for i in range(1, 2*a,2):
    result.append(i)

print(", ".join(map(str, result)))
