def leastTask(lst,n):
    ct=0
    lst.sort()
    for i in range(len(lst)-1):
        if lst[i] == lst[i+1] and n != 0:
            ct += n
        else: ct += 1
    return ct


"""
["A","A","A","B","B","B"]
                      |
ct 9

"""
def leastTask2(tasks,n):
    tasks.sort()
    freq_list = []
    ct = 1
    for i in range(1,len(tasks)):
        if tasks[i] != tasks[i-1]:
            freq_list.append(ct)
            ct = 1
        else: 
            ct += 1
    freq_list.append(ct)
    freq_list.sort().reverse()
    print(freq_list)
    assumed_least = freq_list[0](n + 1) - n
    # answer one last thing, which is --at which last moment do the processor finishes its job
    for i in range(1,len(freq_list)):
        ct = 0
        while freq_list[i] == freq_list[i-1] and ct < freq_list[i]:
            assumed_least += 1

    # a code to write ...
        
    
    return  assumed_least






# print(leastTask2(["A","A","A","B","B","B"],2))
# print(leastTask2(["A","A","A","B","B","B"],0))
# print(leastTask2(["A","A","A","A","A","A","B","C","D","E","F","G"],2))   



def leastTask3(tasks,n):
    tasks.sort()
    freq_list = []
    ct = 1
    for i in range(1,len(tasks)):
        if tasks[i] != tasks[i-1]:
            freq_list.append(ct)
            ct = 1
        else: 
            ct += 1
    freq_list.append(ct)
    freq_list.sort()
    freq_list.reverse()
    idle_slot = (freq_list[0] - 1) * n
    for i in range(1,len(freq_list)):
        idle_slot -= min(freq_list[0]-1,freq_list[i])
    
    return len(tasks) + idle_slot
    
