#다리를 지나는  트럭 
def solution(bridge_length, weight, truck_weights):
    n=len(truck_weights)
    a=truck_weights
    b=[]
    c=[]
    t=[]
    et=0
    while len(c) < n:
        t=[i-1 for i in t if i-1 >0 ]
        if len(t) < len(b):
            c+=b[:len(b)-len(t)]
            b=b[len(b)-len(t):]
            
        if len(a) >0:
            if sum(b)+ a[0] <= weight:
                b.append(a[0])
                t.append(bridge_length)
                a.pop(0)
        et+=1        
    return et


if __name__ == '__main__':
    bridge_length, weight, truck_weights,expected=2,10,[7,4,5,6],8
    print(f'-input-\n  bridge_length : {bridge_length}, weight : {weight}, truck_weights : {truck_weights}')
    print(f'-output-\n expected : {expected}, result : {solution(bridge_length, weight, truck_weights)}')

