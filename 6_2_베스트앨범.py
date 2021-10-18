def solution(genres, plays):
    answer = []
    dic = {x:y for x,y in zip( range(0,len(genres)),plays)}
    dic2 = {x:y for x,y in zip( range(0,len(genres)),genres)}
    dic3=sorted(dic.items(), key=lambda x: x[1])


    print(dic)
    print(dic2)
    print(dic3)

    for x in range(0,len(genres)):
        print(dic2[x])

    
    return answer

genres=["classic", "pop", "classic", "classic", "pop"]
plays=[500,600,150,800,2500]
print(solution(genres,plays))