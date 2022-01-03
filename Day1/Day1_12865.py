N,K = map(int,input().split())

weight = [0]
value = [0]

for i in range(N):
    w,v = map(int,input().split())
    weight.append(w)
    value.append(v)

#DP 사용 -> 가로0 ,세로 0은 모두 0으로
dp = [[0 for _ in range(K+1)] for _ in range(N+1)]
#dp[a][b]는 dp[a-1][b]와 dp[a-1][b-weight[a]]+value[a] 중 큰 값
#단 b-weight[a]가 0보다 작을 수 있으므로 이때는 dp[a-1][b]

for a in range(N+1):
    for b in range(K+1):
        if b-weight[a] >=0:
            dp[a][b] = max(dp[a-1][b],dp[a-1][b-weight[a]]+value[a])
        else:
            dp[a][b] = dp[a-1][b]

print(dp[N][K])
