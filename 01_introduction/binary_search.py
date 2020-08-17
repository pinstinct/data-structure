def BSearch(ar: list, length: int, target: int) -> int:
    first: int = 0  # 탐색 대상의 시작 인덱스 값
    last: int = length - 1 # 탐색 대상의 마지막 인덱스 값
    mid: int

    while first <= last:
        mid = int((first + last) / 2)  # 탐색 대상의 중앙을 찾는다.
        if target == ar[mid]:  # 중앙에 저장된 것이 타겟이라면
            return mid
        else:
            if target < ar[mid]:
                last = mid - 1
            else:
                first = mid + 1
    return -1

if __name__ == "__main__":
    arr: list = [1, 3, 5, 7, 9]
    idx: int

    idx = BSearch(arr, len(arr), 7)
    if idx == -1:
        print(f"탐색 실패")
    else:
        print(f"타겟 저장 인덱스: {idx}")

        idx = BSearch(arr, len(arr), 4)
    if idx == -1:
        print(f"탐색 실패")
    else:
        print(f"타겟 저장 인덱스: {idx}")
