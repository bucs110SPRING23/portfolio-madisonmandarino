def multiply(x,y):
    product = 0
    for i in range(y):
        product = product + x
    return product

def exponent(x, expo):
    ans = 1
    for i in range(expo):
        ans = ans * x
    return ans

def square(x):
    return exponent(x,2)


def main():
    print(multiply(5,8))
    print(exponent(7,2))
    print(square(4))

main()