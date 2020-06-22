# coding: utf-8
# Your code here!
def saiki(i,cost,score_list):
    if i == N:
        if min(score_list) >= X:
            ans.append(cost)
    else:
        temp = [score_list[j]+book_lists[i][j+1] for j in range(M)]
        saiki(i+1,cost,score_list)
        saiki(i+1,cost+book_lists[i][0],temp)
 
N,M,X = map(int,input().split())
book_lists = [list(map(int, input().split())) for _ in range(N)]
ans=[]
saiki(0,0,[0]*M)
print(min(ans) if len(ans)!=0 else -1)