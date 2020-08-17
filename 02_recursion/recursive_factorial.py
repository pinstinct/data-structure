def factorial(n: int) -> int:
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

if __name__ == "__main__":
    print(f"1! = {factorial(1)}")
    print(f"2! = {factorial(2)}")
    print(f"3! = {factorial(3)}")
    print(f"4! = {factorial(4)}")
    print(f"9! = {factorial(9)}")
