import sys

T = int(sys.stdin.readline())


def solution(applicantCount):
    applicants = []

    for _ in range(applicantCount):
        rank = list(map(int, sys.stdin.readline().split()))
        applicants.append(rank)

    # 서류 성적순으로 분류
    applicants.sort(key=lambda x: x[0])

    count = 1  # 서류 1등은 무조건 합격이다.
    mostInterviewRank = applicants[0][1]

    # 서류 성적순으로 분류되었으므로, 면접 성적만 비교한다
    # 면접 성적이 앞 사람(면접 성적이 본인보다 높은사람)보다 낮다면, 앞사람들에 비해 아무것도 높지 않으므로 탈락한다.
    for i in range(1, len(applicants)):
        if applicants[i][1] < mostInterviewRank:
            mostInterviewRank = applicants[i][1]
            # 최고 면접성적이 나오면, 이를 기억해놓는다
            # 이는, 이 지원자가 앞에 모든 지원자들을 이길 수 있는 지 판단하는 척도가 된다.
            count += 1

    print(count)


def code(T):
    for _ in range(T):
        applicantCount = int(sys.stdin.readline())
        solution(applicantCount)


code(T)
