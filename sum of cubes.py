def cubes(m, n):
    if m > n:
        return 0  
    
    sum = 0
    for i in range(m, n+1):
        sum += i**3
    
    return sum


m = int(input("Enter the value of m: "))
n = int(input("Enter the value of n: "))

result = cubes(m, n)
if result == 0:
    print("Invalid range: m should be less than or equal to n.")
else:
    print(f"The sum of cubes from {m} to {n} is: {result}")
