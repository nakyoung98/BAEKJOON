import sys

n, m = map(int, sys.stdin.readline().split())

class Node:
    name = None
    parent = None

    def __init__(self, name, parent):
        self.name = name
        self.parent = parent

    def setParent(self, parent):
        self.parent = parent
        return self

    def __str__(self):
        return str(self.name)+" "+str(self.parent)+"\n"

parent = 0

Nodes = [Node(0,0).setParent(None)]
for i in range(1,n):
    Nodes.append(Node(i,parent)) #1부터 n-1까지의 node 리스트 모두 0에 붙어있음

leaf = n #이때 leaf는 n-1개

while leaf != m:
    parent += 1
    for i in range(parent+1,n):
        Nodes[i].setParent(parent)
    leaf -=1

print(*Nodes[1:], sep="")