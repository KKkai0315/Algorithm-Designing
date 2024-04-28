n = int(input())
mission = []
for i in range(n):
    mission.append(list(map(int, input().split())))
    mission[i].append(i)
mission.sort(key=lambda mis: mis[1])
p = [0] * n
for i in range(n):
    for j in range(i-1,-1,-1):
        if mission[j][1] <= mission[i][0]:
            p[i] = j+1
            break
M = [0] * (n+1)
for j in range(1,n+1):
    M[j] = max(mission[j-1][2]+M[p[j-1]],M[j-1])
print(M[n])
ans = []
def find_solution(n):
    if n == 0 : return
    if M[n]>M[n-1]:
        ans.append(mission[n-1][-1]+1)
        find_solution(p[n-1])
    else:
        find_solution(n-1)
    return
find_solution(n)
for i in ans:
    print(i,end=' ')