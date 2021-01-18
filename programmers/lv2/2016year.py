#2016년
def solution(a, b):
    m=[31,29,31,30,31,30,31,31,30,31,30,31]
    z=(sum(m[:a-1])+b-3)%7
    day=['SUN','MON','TUE','WED','THU','FRI','SAT']
    answer = day[z]
    return answer


if __name__ == '__main__':
    a,b,e=5,24,'TUE'
    print(f'-input-\n a : {a}, b : {b}')
    print(f'-output-\n expected : {e}, result : {solution(a,b)}')

