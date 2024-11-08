# point (r,c) 각 포인트의 위치
# route (s, 1, 2, 3) 시작위치 ~ 끝 위치
# 이동 주의: r을 먼저 갈 것
def solution(points, routes):
    r_max = max(points, key=lambda x: x[0])[0] + 1
    c_max = max(points, key=lambda x: x[1])[1] + 1

    end_robots = 0
    danger = 0

    routes.insert(0, [1])
    points.insert(0, [1, 1])
    cur_poses = [points[route[0]] for route in routes]  # 각 로봇의 첫 위치를 담은 배열

    map = [[set() for _ in range(c_max)] for _ in range(r_max)]
    for robot in range(1, len(cur_poses)):
        r = cur_poses[robot][0]
        c = cur_poses[robot][1]
        map[r][c].add(robot)  # 로봇 초기 위치 시키기

    robot_count = len(routes) - 1  # 총 로봇 개수
    while end_robots < robot_count:
        # 겹치는 지점 찾기
        point = []
        for cur_pos in cur_poses:
            r = cur_pos[0]
            c = cur_pos[1]
            if len(map[r][c]) > 1:
                if map[r][c] not in point:
                  point.append(map[r][c])
        danger += len(point)

        # 모든 로봇에 대해서
        for robot in range(1, robot_count + 1):
            if len(routes[robot]) == 0:  # 더이상 갈 곳이 없는 로봇이면 종료
                continue
            # 현재 위치가 route[0]의 위치라면 해당 route 도착했으므로 route에서 unshift
            cur_r = cur_poses[robot][0]
            cur_c = cur_poses[robot][1]

            target_r = points[routes[robot][0]][0]
            target_c = points[routes[robot][0]][1]

            if cur_r == target_r and cur_c == target_c:
                routes[robot].pop(0)
                if len(routes[robot]) == 0:
                    end_robots += 1
                    map[cur_r][cur_c].remove(robot)
                    continue

                # 다음 목표점 설정
                target_r = points[routes[robot][0]][0]
                target_c = points[routes[robot][0]][1]

            map[cur_r][cur_c].remove(robot)  # 현재 위치에서 빼기

            new_r = cur_r
            new_c = cur_c

            if cur_r != target_r:
                new_r = cur_r + (1 if target_r > cur_r else -1)
            elif cur_c != target_c:
                new_c = cur_c + (1 if target_c > cur_c else -1)

            map[new_r][new_c].add(robot)
            cur_poses[robot] = [new_r, new_c]

    return danger

