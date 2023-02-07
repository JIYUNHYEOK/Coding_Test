# 8-3 호출되는 함수 확인
## 재귀함수를 이용하여 소스코드를 작성: 큰 문제를 해결하기 위해 작은 문제를 호출: 탑다운 방식
## 단순 반복문을 이용하여 소스코드를 작성: 작은 문제부터 차근차근 답을 도출: 보텀업 방식

d = [0]*100

def pibo(x):
    print(f"f({str(x)})", end = ' ')
    if x == 1 or x == 2:
        return 1
    if d[x] != 0:
        return d[x]
    d[x] = pibo(x-1) + pibo(x-2)
    return d[x]
pibo(6)