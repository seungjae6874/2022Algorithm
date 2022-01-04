
n = input()

nums = {'c':26, 'd':10}

s = len(n)
ans = nums[n[0]] #초기 값은 n의 첫번째 문자 c/d

for i in range(1,s):
    mul = nums[n[i]]
    if n[i] == n[i-1]:
        mul -=1
    ans *= mul

print(ans)
