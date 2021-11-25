# BOJ 단계별로 풀어보기
# 6. 함수

# 4673
def d(num):
    result = 0
    num_to_str = str(num)
    if num < 10:
        result = num * 2
    else:
        result = num
        for i in range(len(num_to_str)):
            result += int(num_to_str[i])

    return result
