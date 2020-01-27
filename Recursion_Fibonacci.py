

# Function for nth Fibonacci number
def Fibonacci(n):
    """
    F0 = 0
    F1 = 1
    Fn = Fn-1 + Fn-2
    :param n:
    :return:
    """
    if n < 0:
        # first Fibonacci number is zero;
        print("Incorrect input")
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return Fibonacci(n-1) + Fibonacci(n-2)


print(Fibonacci(9))

