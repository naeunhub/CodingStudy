import sys

N = int(sys.stdin.readline())
student_num = int(sys.stdin.readline())
vote_list = list(map(int, sys.stdin.readline().split(' ')))

fin_candi = []
fin_candi_vote = []

for vote in vote_list :
    if vote in fin_candi: # 이미 있다면
        fin_candi_vote[fin_candi.index(vote)] += 1

    else : # fin_candi에 없다면
        if len(fin_candi)>=N :
            idx = fin_candi_vote.index(min(fin_candi_vote))
            del fin_candi_vote[idx]
            del fin_candi[idx]

        fin_candi.append(vote)
        fin_candi_vote.append(1)

ans = str(sorted(fin_candi)[0])
for fin_student in sorted(fin_candi)[1:] :
    ans = ans + " " + str(fin_student)

print(ans)