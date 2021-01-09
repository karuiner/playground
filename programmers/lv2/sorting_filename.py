#파일명 정렬

def solution(files):
    def f(x):
        a,b=0,1
        for i,ix in enumerate(x):
            if (ix.isdigit()) and (a==0):
                a=i
                b=0
            if (not ix.isdigit()) and (b==0):
                b=i
        if b ==0:
            b=len(x)
        return [x[:a].lower(),int(x[a:b]),x[b:]]
    db={}
    for i in files:
        db[i]=f(i)
        
    h=sorted(set([db[i][0] for i in files]))
    p=[]
    for i in h:
        n=[db[j][1] for j in files if db[j][0] == i]
        for j in sorted(set(n)):
            o=[k for k in files if (db[k][0] == i) and(db[k][1] ==j)]
            p+=o
    return p


if __name__ == '__main__':
    f,expected=['img12.png', 'img10.png', 'img02.png', 'img1.png', 'IMG01.GIF', 'img2.JPG'],['img1.png', 'IMG01.GIF', 'img02.png', 'img2.JPG', 'img10.png', 'img12.png']
    print(f'-input-\n  filename : {f}')
    print(f'-output-\n expected : {expected}\n result : {solution(f)}')

