# i want to use a recursive function to recursively calculate the factorial of a number

def factorial(a: int) -> int:
    if a == 1:
        return 1
    return a * factorial(a-1)

print(factorial(5))