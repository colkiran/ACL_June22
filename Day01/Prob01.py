
lower = 50
upper = 150
count = 0
print("Prime numbers between", lower, "and", upper, "are:")

for num in range(lower, upper + 1):
   # all prime numbers are greater than 1
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num, end=" ")
           count = count + 1
print("\nThe Count of prime numbers between 50 and 150 is:", count)
