import copy

#DFS func
def DFS(Linkedlist, V):
    list = copy.deepcopy(Linkedlist)
    DFSlist = [] #stack
    DFSResult = [] #result 저장
    
    DFSlist.append(V)
    DFSResult.append(V)

    if not list[V]:
        print(V) #길이 없음
        return
        
    while True:
        if not DFSlist:
            break
        V = DFSlist.pop()
        
        if list[V]:
            temp = -1

            for i in range(len(list[V])):
                if list[V][i] not in DFSResult:
                    temp = i
                    break
            if temp != -1:
                DFSlist.append(V)
                next = list[V].pop(temp)
                DFSlist.append(next)
                DFSResult.append(next)
                list[next].remove(V)
        

    
    for word in DFSResult:
        print(word, end=" ")
    print()
    return


def BFS(Linkedlist, V):
    list = copy.deepcopy(Linkedlist)
    BFSlist = [] #stack
    BFSResult = [] #result 저장
    
    BFSlist.append(V)
    BFSResult.append(V)

    if not list[V]:
        print(V) #길이 없음
        return

    while True:
        if not BFSlist:
            break
 
        V = BFSlist.pop()

        for index in list[V]:
            if index not in BFSResult:
                BFSlist.insert(0,index)
                BFSResult.append(index)
                list[index].remove(V)


    for word in BFSResult:
        print(word, end=" ")
    return

    
#메인 func
def main():
    N,M,V = map(int,input().split())
    # 이중 배열 만들기 index 1부터 N까지 쓰기위해(0은 안씀)
    # 0부터 N번 index까지 있는 이중 배열
    Linkedlist = [[] for _ in range(N+1)] 
    for _ in range(M):
        Cur, Nex = map(int,input().split())
        Linkedlist[Cur].append(Nex)
        Linkedlist[Nex].append(Cur)
    for i in range(N):
        Linkedlist[i+1].sort()

    DFS(Linkedlist, V)
    BFS(Linkedlist, V)


if __name__ == '__main__':
    main()
