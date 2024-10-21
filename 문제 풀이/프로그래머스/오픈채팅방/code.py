def solution(record):
    answer = []
    logs = []
    session = {}
    
    # 레코드 분석
    for log in record: 
        temp = log.split()
        print(temp)
        
        action = temp[0]
        uid = temp[1]
        nickname = temp[2] if action != "Leave" else None
        
        # 로그 저장하기
        save_log(uid, action, logs)
        save_session(uid, action, nickname, session)

        
    # 실 로그 생성
    for uid, action in logs:
        if action == "Enter":
            answer.append(f'{session[uid]["current_nick"]}님이 들어왔습니다.')  
        elif action == "Leave":
            answer.append(f'{session[uid]["current_nick"]}님이 나갔습니다.')
        
    return answer

def save_log(uid, action, logs):
    if action == "Enter" or action == "Leave":
        logs.append((uid,action)
    elif action == "Change":
        None
        
# 유저들의 정보를 모아놓는 session
def save_session(uid, action, nickname, session):
    session.setdefault(uid, {"action":action, "current_nick": nickname, "will_nick": None})
    
    # Enter일 시
    if action == "Enter":
        # 변경될 닉네임이 존재한다면 변경
        if session[uid]["will_nick"] is not None:
            session[uid]["current_nick"] = session[uid]["will_nick"] 
            session[uid]["will_nick"] = None
            
    # Leave일 시
    elif action == "Leave":
        None
    
    # Change일 시
    elif action == "Change":
        # 마지막 상태가 Leave이면 다음 Enter에 닉네임 변경되도록 설정
        if session[uid]["action"] == "Leave":
            session[uid]["will_nick"] = nickname
        # Enter이면 바로 닉네임 변경
        elif session[uid]["action"] == "Enter":
            session[uid]["current_nick"] = nickname
            
        
        
            
        