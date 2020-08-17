def fibo(n: int) -> int:
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)

if __name__ == "__main__":
    for i in range(1, 15):
        print(f"{fibo(i)}")