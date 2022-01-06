n = int(input())
fullsec = []
tempstr = ''
for i in range(n):
    flag= False
    check, c1,t = map(str,input().split())
    if check == 'type':
        tempstr += c1
        fullsec.append((int(t), tempstr))
    else:
        #undo일때 t-c1보다 작은 인덱스중 가장 큰값의 문자열가져오기
        c1 = int(c1)
        t = int(t)
        for i in range(len(fullsec)-1,-1,-1):
            if fullsec[i][0] >= t-c1:continue
            #건너뛴다 undo하는 시간보다 작아야하므로
            
            flag = True
            tempstr = fullsec[i][1]
            fullsec.append((t,tempstr))
            break
        if not flag:
            #이 경우가 t-c1가 0초보다 작아지는 순간이므로
            tempstr = '' #공백처리
            fullsec.append((t,tempstr))
print(fullsec[-1][1])
