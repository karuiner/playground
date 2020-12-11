# 두개 뽑아서 더하기
def solution(numbers):
    u=[]
    
    def f(x,i,u):
        a=[x[i]+y  for j ,y in enumerate(x) if i !=j]
        for ia in a:
            if not ia in u:
                u.append(ia)
        return u

    for i in range(len(numbers)):
        u=f(numbers,i,u)

    return sorted(u)

t1=[2,1,3,4,1]
exp_ans1=[2,3,4,5,6,7]
ans1=solution(t1)
print(f"input : {t1}")
print(f"expected : {exp_ans1}, result : {ans1}")
t2=[5,0,2,7]
exp_ans2=[2,5,7,9,12]
ans2=solution(t2)
print(f"input : {t2}")
print(f"expected : {exp_ans2}, result : {ans2}")

