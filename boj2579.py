import sys
length_ = int(input())
stairs = []
scores = []

for i in range(length_):
    stairs.append(int(input()))

scores.append(stairs[0])
if length_<3 :
    if length_==1 :
        print(scores[-1])
        sys.exit()
    elif length_==2 :
        print(stairs[0]+stairs[1])
        sys.exit()
        
scores.append(stairs[0]+stairs[1])
scores.append(max(stairs[0]+stairs[2], stairs[1]+stairs[2]))

for i in range(3, length_) :
    scores.append(max(scores[i-2]+stairs[i], scores[i-3]+stairs[i-1]+stairs[i]))
    
print(scores[-1])