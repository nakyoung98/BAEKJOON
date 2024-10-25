import sys
sys.setrecursionlimit(300000)

def solution(sales, links):
    tree = {i: [] for i in range(1, len(sales) + 1)}
    for link in links:
        tree.setdefault(link[0], [])
        tree[link[0]].append(link[1])

    # [미참여시최소값, 참여시최소값]
    DP = [[0, 0] for _ in range(len(sales) + 1)]
    dfs(1, tree, DP, sales)
    return min(DP[1])


def dfs(node, tree, DP, sales):
    leader = node
    members = tree[leader]

    # 리프노드면
    if not members:
        DP[leader] = [0, sales[leader - 1]]
        return

    # 아니면 리프노드 먼저 탐색
    for member in members:
        dfs(member, tree, DP, sales)

    # 나 참, 팀 미참일 때
    # 미참하는 팀원들의 미참 최소값 합
    sum_min = 0
    for member in members:
        sum_min += DP[member][0]
    min_leader_go = sales[leader - 1] + sum_min
    
    # 나 미참, 팀 중 한명이라도 참일 때
    # 팀원 한명을 참으로 두고, 나머지는 참여 미참여 중 최소값을 가져감
    sum_mins = []
    for i in range(len(members)):
        sum_min = DP[members[i]][1]  # 확정으로 가는 멤버
        for i_left in range(i):
            sum_min += min(DP[members[i_left]])
        for i_right in range(i + 1, len(members)):
            sum_min += min(DP[members[i_right]])
        sum_mins.append(sum_min)

    min_leader_not_go = min(sum_mins)
    
    # 나 참 팀 미참과 나 참, 팀 중 한명이라도 참일 경우 중 더 적은 값 고르기
    min_leader_go = min(min_leader_go, min_leader_not_go + sales[leader-1])

    DP[leader] = [min_leader_not_go, min_leader_go]
