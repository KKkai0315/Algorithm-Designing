from math import ceil
def Merge_And_Count(A,B,ans):
    current_A = 0
    current_B = 0
    merge = []
    count = 0
    while(current_A < len(A) and current_B < len(B)):
        if A[current_A] < B[current_B]:
            merge.append(A[current_A])
            current_A += 1
        else:
            merge.append(B[current_B])
            count += len(A)-current_A
            for i in A[current_A:]:
                ans[B[current_B]].append(i)
            current_B += 1
    merge.extend(A[current_A:])
    merge.extend(B[current_B:])
    return count,merge,ans

def Sort_And_Count(L,ans):
    r=0
    if len(L) == 1:
        return r,L,ans
    else:
        A = L[:ceil(len(L)/2)]
        B = L[ceil(len(L)/2):]
        (ra,A,ans) = Sort_And_Count(A,ans)
        (rb,B,ans) = Sort_And_Count(B,ans)
        (r,L,ans) = Merge_And_Count(A,B,ans)
        r = ra + rb + r
        return r,L,ans

n = int(input())
L = list(map(int,input().split()))
ans={}
for l in L:
    ans[l]=[]
r,L,ans = Sort_And_Count(L,ans)
print(r)
for i in ans:
    for j in ans[i]:
        print(f"{j}-{i}")

