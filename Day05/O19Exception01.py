
num = "0"
inv = 1

try:
    inv = 1 / num

except ZeroDivisionError as z:
    print(z)

except TypeError as t:
    print(t)

except Exception as e:              # base class of all exceptions
    print(e)

else: print(f"Inverse :{inv}")

finally: print("Division of the number successfully done.....")