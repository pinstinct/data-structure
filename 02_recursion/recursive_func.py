def recursive(num: int):
    if num <= 0:  # 재귀의 탈출 조건
        return  # 재귀 탈출
    print(f"Recursive call {num}")
    recursive(num - 1)

if __name__ == "__main__":
    recursive(3)
