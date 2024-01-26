q = ['Which language is used to construct python?',
     'How many planets are there?',
     'Which is a small computer?']
ans = [['A.C++', 'B.Java','C.Klingon','D.Microsoft'],
       ['A.5','B.7','C.8','D.9'],
       ['A.Macbook', 'B.Rasberry Pi', 'C.MUBC', 'D.Quantam computer']]

y = ['A', 'C', 'B']
r = []
for i in range(3):
    print(q[i])
    for a in ans[i]:
        print(a)

    g = input()
    while not (g=='A' or g=='B' or g=='C' or g=='D'):
        g = input()
    r.append(g)

t=0
for j in range(3):
   if(r[j]==y[j]):
       t+=1


print(f"You got {(t/3)*100:.2f}% in the quiz")
print("YOU DID IT")