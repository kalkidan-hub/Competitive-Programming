def merge(intervals):
    merged=[]
    for i in range(len(intervals)):
        subInterval=intervals[i]
        for j in range(i+1,len(intervals)):
            if subInterval[1]>=intervals[j][0]:
                subInterval[1]=intervals[j][1]
            else: break
    merged+=[subInterval]

    return merged





print(merge([[1,3],[2,3],[3,6],[8,10],[15,18]]))