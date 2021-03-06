# 토끼는 언제나 시계를 들고 이곳저곳을 뛰어다니며 이동 시간을 측정합니다.
# 토끼는 오늘 A에서 출발해 B, C, D를 들러 다시 A로 돌아와야 합니다. 그런데 하필 오늘 시계가 고장이 나서 분침과 시침은 돌아가지 않고 초침만 돌아가고 있습니다. 어쩔 수 없이 엘리스 토끼는 초침만을 이용해서 시간을 측정하기로 했습니다.
# 하루 동안 측정한 결과가 주어지면, 토끼가 이날 총 이동한 시간이 몇 분 몇 초인지 출력하는 프로그램을 작성하세요.

# [입력]
# 첫 번째 줄에 A에서 B의 이동 시간을 입력합니다.
# 두 번째 줄에 B에서 C의 이동 시간을 입력합니다.
# 세 번째 줄에 C에서 D의 이동 시간을 입력합니다.
# 네 번째 줄에 D에서 A의 이동 시간을 입력합니다.
# 총 이동시간은 항상 1 분 0 초 이상 59 분 59 초 이하입니다.

# [출력]
# 총 이동시간 x 분 y 초를 출력합니다.
# 첫 번째 줄에 x를, 두 번째 줄에 y를 출력합니다.


# ------------------------------------------------------


def sol():
    time = 0
    for i in range(4):
        time += int(input())
    print(time // 60)
    print(time % 60)


sol()
