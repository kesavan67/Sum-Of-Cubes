def cubes(m, n): #defined the variables
    if m > n:  
        return 0  #satisify the condition return value 0
    
    sum = 0
    for i in range(m, n+1): #using for loop to implement the code to the range values
        sum += i**3
    
    return sum  #return the sum value


m = int(input("Enter the value of m: ")) #get the input value from the user
n = int(input("Enter the value of n: "))

result = cubes(m, n) #calculate the result
if result == 0:
    print("0")
else:
    print(f"The sum of cubes from {m} to {n} is: {result}") #The condition is not satisfied it print the else part
