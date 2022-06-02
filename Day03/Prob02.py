
def recur_fibo(n):
    if n <= 1:
        return n
    else:
        return recur_fibo(n - 1) + recur_fibo(n - 2)

ntrms = int(input("Enter the number of terms :"))
print("Fibanocci Series")
for i in range(ntrms):
    print(recur_fibo(i), end=" ")

