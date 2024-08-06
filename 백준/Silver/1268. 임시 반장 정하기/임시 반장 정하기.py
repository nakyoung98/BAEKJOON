import sys

input = sys.stdin.readline

studentCount = int(input())


def solution(studentCount):
    # 학생반 정보
    classes = [list(map(int, input().split())) for _ in range(studentCount)]
    friendInfo = [set() for _ in range(studentCount)]
    for c in range(5):
        # 모든학생이 특정학년에 어떤반이었는지 추출
        classesInyear = list(map(lambda x: x[c], classes))
        # 해당 학년에서 같은반끼리 묶음
        classesInfo = [[] for _ in range(10)]
        for student, stClass in enumerate(classesInyear):
            classesInfo[stClass].append(student)
        for students in classesInfo:
            for student in students:
                friendInfo[student].update(
                    students
                )  # 같은반이었던 학생 리스트 업데이트

    # 같은반이었던 학생수로 전환
    friendsNumInfo = list(map(lambda x: len(x), friendInfo))
    maxFriends = max(friendsNumInfo)
    candidate = friendsNumInfo.index(maxFriends) + 1  # 0부터 시작을 1부터 시작으로 원복
    print(candidate)


solution(studentCount)
