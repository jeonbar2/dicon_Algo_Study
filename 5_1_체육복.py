def solution(n, lost, reserve):
    answer = 0            
    temp=lost
    lost=list(set(lost)-set(reserve))
    reserve=list(set(reserve)-set(temp))  ##도난 당한 사람이 여분을 갖고 왔을경우 두 리스트를 뺴기 위한 연산
    print(lost)
    print(reserve)
    for i in reserve:
        if i in lost:
            lost.remove(i)
        elif i-1 in lost:
            #print("삭제전",lost)
            lost.remove(i-1)
            #print("삭제후",lost)  
        elif i+1 in lost:
            lost.remove(i+1)
       
        
    
    answer = n - len(lost)
    return answer


print(solution(5,[2,3,4],[1,2,3]))