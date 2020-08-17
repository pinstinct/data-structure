def hanoi_tower_move(num: int, fr: str, by: str, to: str) -> None:
    if num == 1:
        print(f"원반1을 {fr}에서 {to}로 이동")
    else:
        hanoi_tower_move(num-1, fr, to, by)
        print(f"원반{num}을(를) {fr}에서 {to}로 이동")
        hanoi_tower_move(num-1, by, fr, to)

if __name__ == "__main__":
    # 막대A의 원반 3개를 막대 C로 옮기기
    hanoi_tower_move(3, "A", "B", "C")