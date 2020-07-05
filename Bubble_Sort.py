#버블 정렬

bubble=list(map(int,input('input : ').split()))
for x in range(len(bubble)):
    for y in range(len(bubble)-1):
        if bubble[y] > bubble[y+1]:
            bubble[y],bubble[y+1]=bubble[y+1],bubble[y]
            print(bubble)