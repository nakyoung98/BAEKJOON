import sys

sys.setrecursionlimit(10000)


def solution(nodeinfo):
    for i in range(len(nodeinfo)):
        nodeinfo[i].append(i + 1)
    sorted_nodeinfo = sorted(nodeinfo, key=lambda point: (-point[1], point[0]))

    # 노드 트리 만들기
    head_node = Node(sorted_nodeinfo[0])

    for nodeinfo in sorted_nodeinfo[1:]:
        cur_node = head_node
        new_node = Node(nodeinfo)

        while True:
            if cur_node.x > new_node.x:
                if cur_node.left:
                    cur_node = cur_node.left
                else:
                    cur_node.left = new_node
                    break
            else:
                if cur_node.right:
                    cur_node = cur_node.right
                else:
                    cur_node.right = new_node
                    break

    # 전위 순회 - 뿌리, 왼쪽, 오른쪽
    preorder_result = []
    preorder(preorder_result, head_node)

    postorder_result = []
    postorder(postorder_result, head_node)

    return [preorder_result, postorder_result]


def preorder(preorder_result, node):
    preorder_result.append(node.value)
    if node.left is not None:
        preorder(preorder_result, node.left)
    if node.right is not None:
        preorder(preorder_result, node.right)


def postorder(postorder_result, node):
    if node.left is not None:
        postorder(postorder_result, node.left)
    if node.right is not None:
        postorder(postorder_result, node.right)
    postorder_result.append(node.value)


class Node:
    def __init__(self, nodeinfo):
        self.x = nodeinfo[0]
        self.y = nodeinfo[1]
        self.value = nodeinfo[2]

        self.left = None
        self.right = None