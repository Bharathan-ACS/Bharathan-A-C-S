a = int(input('a='))
result = []
for i in range(1, 2*a, 2):
    result.append(i)

print(", ".join(map(str, result)))
