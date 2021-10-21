"""두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오."""


def add_7(T):
    for i in range(1, T + 1):
        a, b = map(int, input().split())
        print(
            "Case #",
            i,
            ": ",
            a + b,
            sep="",
        )


add_7(int(input()))
