def merge(intervals):
    intervals.sort()
    merged=[]
    ct=0
    for i in range(len(intervals)):
        if ct>0:
            ct-=1
            continue
        subInterval=intervals[i]
        for j in range(i+1,len(intervals)):
            if subInterval[1]>=intervals[j][0]and subInterval[1]<=intervals[j][1] :
                subInterval[1]=intervals[j][1]
                ct+=1
            elif subInterval[1]>=intervals[j][0] and subInterval[1]>=intervals[j][1]:
                ct+=1
            else: break
        merged.append(subInterval)
        
        

    return merged




print(merge([[1,3],[2,6],[8,10],[15,18]]))