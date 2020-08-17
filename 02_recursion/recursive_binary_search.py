def binary_search_recursion(
    ar: list, first: int,last: int, target: int) -> int:
    mid: int
    if first > last:
        return -1  # 탐색 실패
    mid = int((first + last) / 2)  # 탐색 대상의 중앙
    if ar[mid] == target:
        return mid
    elif target < ar[mid]:
        return binary_search_recursion(ar, first, mid-1, target)
    else:
        return binary_search_recursion(ar, mid+1, last, target)

if __name__ == "__main__":
    arr: list = [1, 3, 5, 7, 9]
    idx: int

    idx = binary_search_recursion(arr, 0, len(arr)-1, 7)
    if idx == -1:
        print(f"탐색 실패")
    else:
        print(f"타켓 저장 인덱스: {idx}")

        idx = binary_search_recursion(arr, 0, len(arr)-1, 4)
    if idx == -1:
        print(f"탐색 실패")
    else:
        print(f"타켓 저장 인덱스: {idx}")