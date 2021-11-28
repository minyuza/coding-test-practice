# BOJ 단계별로 풀어보기
# 7. 문자열

# 11654
word = input()
print(ord(word))


11720
n = int(input())
word = input()
result = 0
for i in range(n):
    result += int(word[i])

print(result)
