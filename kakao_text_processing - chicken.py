date = 0; time = 0; name = '';
times = []; names = [];
l_month = 0; l_day = 0; l_ampm = ''; l_hour = 0; l_minute = 0;

f = open("kakaotalk-chicken.txt",'r',encoding='UTF8')
lines = f.readlines()
member = lines[3][:-1].split('|')
matrix = [[0]*len(member) for i in range(len(member))]  # matrix[src][dst]

for l in lines:
    if(l[:5] == "-----"):   # date
        l = l.split('-'*15)[1][1:-1]
        l_month = int(l.split('월')[0].split('년 ')[1])
        l_day = int(l.split('월 ')[1].split('일')[0])
        
        date = l_month*30+l_day   # set date

    elif(l.split(']')[0][1:] in member):  # chat
        name = l.split(']')[0][1:]
        l = l.split('] [')[1]
        l_ampm = l[0:2]
        l_hour, l_minute = l[3:].split(']')[0].split(':')
        l_hour = int(l_hour); l_minute = int(l_minute)
        
        if(l_ampm == '오후' and l_hour != 12):
            l_hour += 12
        elif(l_ampm == '오전' and l_hour == 12):
            l_hour = 0
        
        time = l_minute + l_hour*60 + date*24*60
        times.append(time)
        names.append(name)
#        print(time, name)

for i in range(len(times)): # i: dst, 대답받은 사람, 관심 받음
    for j in range(i+1, len(times)):  # j: src, 대답한 사람, 관심 줌
        if(times[j]-times[i]>10):
            break
#        print(times[i],times[j])
        matrix[member.index(names[j])][member.index(names[i])] += 1
#        print(i,names[i],j,names[j])

print('srcdst ', end='')
for i in range(len(member)):
    print("%2s"%member[i][0:3],end=' ')
print()

for i in range(len(member)):
    print("%s"%member[i][0:3], end='\t')
    for j in range(len(member)):
        print("%4d"%matrix[i][j], end=' ')
    print()


