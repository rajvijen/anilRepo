def oddEven(n):
    if n % 2 == 0:
        return 1
    else:
        return 0


n = int(input("Enter a number: "))

for i in range(2, n):
    # print("Number is: ", oddEven(i))
    x = oddEven(i)
    if (x):
        x = x + 1
    else:
        x = x - 1
    print("x is: ", x)
