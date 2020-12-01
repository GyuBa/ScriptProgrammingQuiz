
list = [[a,b,c] for a in range(1,101) for b in range(1,101) for c in range(1, 1001) if (a**2 + b**2 == c) and (a <= b and b <= c)]
print(list)

result = [i for i in range(2, 1001)if all([i%x != 0 for x in range(2,i)])]
print(result)
