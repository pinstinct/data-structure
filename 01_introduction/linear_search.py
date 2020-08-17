def LSearch(ar: list, length: int, target: int) -> int:
    """순차 탐색 알고리즘 함수 """
    for i in range(length):
        if ar[i] == target:
            return i  # 찾은 대상의 인덱스 값 반환
    return -1  # 찾지 못했음을 의미하는 값 반환

if __name__ == "__main__":
    arr: list = [3, 5, 2, 4, 9]
    idx: int

    idx = LSearch(arr, len(arr), 4)
    if idx == -1:
        print(f"탐색 실패")
    else:
        print(f"타켓 저장 인덱스: {idx}")

    idx = LSearch(arr, len(arr), 7)
    if idx == -1:
        print(f"탐색 실패")
    else:
        print(f"타켓 저장 인덱스: {idx}")