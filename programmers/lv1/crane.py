#크레인 인형 뽑기 게임
def solution(board, moves):
    l= len(board[0])
    b=[]
    bm=0
    for i,m in enumerate(moves):
        g,j=1,0
        
        while g :
            p=board[j][m-1]  
            if p:
                board[j][m-1]=0
                if len(b) >= 1:
                    if b[-1] != p:
                        b.append(p)
                    else:
                        b=b[:-1]
                        bm+=1
                else:
                    b.append(p)
                        
                g=0
            if j == l-1:
                g=0
            j+=1
    answer = bm*2
    return answer

if __name__ == '__main__':
    board=[[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
    moves=[1,5,3,5,1,2,1,4]
    expected=4


    print(f'input : board')
    for i in board:
        print(i)
    print(f'moves : {moves}')
    print(f'expected : {expected}, result : {solution(board,moves)}')

