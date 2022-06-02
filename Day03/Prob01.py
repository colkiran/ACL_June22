
def factorial(a):
    if a == 1:
        return 1
    else:
        return (a * factorial(a-1))


number = int(input("Enter a number to find its factorial :"))
print(f"The factorial of {number} is {factorial(number)}")
