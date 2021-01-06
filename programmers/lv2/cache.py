# 캐시
def solution(cacheSize, cities):
    
    c=[]
    t=0    
    for i in cities:
        if cacheSize >0:
            if i.lower() in c:
                t+=1
            else:
                t+=5
            if len(c) <cacheSize:
                if not i.lower() in c:
                    c.append(i.lower())
                else:
                    c.append(i.lower())
            else:
                if not i.lower() in c:
                    c=c[1:]
                    c.append(i.lower())
                else:
                    c.remove(i.lower())
                    c.append(i.lower())
        else:
            t=len(cities)*5
    return t


if __name__ == '__main__':
    cachesize,cities,e=3,['Jeju', 'Pangyo', 'Seoul', 'NewYork', 'LA', 'Jeju', 'Pangyo', 'Seoul', 'NewYork', 'LA'],50
    print(f'-input-\n Cachesize : {cachesize}, Cities : {cities}')
    print(f'-output-\n expected : {e}, result : {solution(cachesize,cities)}')

