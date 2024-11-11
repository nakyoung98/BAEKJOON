import heapq
# n: 셔틀 운행 횟수
# t: 셔틀 운행 간격
# m: 한 셔틀에 탈 수 있는 최대 승객 수
def solution(n, t, m, timetable):
    
    # timetable 최소 힙으로 변경
    timetable = [Time(time).time for time in timetable]
    heapq.heapify(timetable)
    
    bus = Time("09:00")
    interval = Time(f"00:{t}")
    bus_passengers_in_time = []
    
    for _ in range(n):
        cur_passenger = []
        while timetable and len(cur_passenger) < m:
            if timetable[0] <= bus.time:
                passenger = heapq.heappop(timetable)
                cur_passenger.append(Time.intToTime(passenger))
            else:
                break
        bus_passengers_in_time.append((bus+Time("00:00"), cur_passenger))
        bus = bus + interval
        
    bus_time, passengers = bus_passengers_in_time[-1]
    result = bus_time if len(passengers) < m else passengers[-1]- Time("00:01") if passengers else bus_time
    
    return str(result)
    

class Time:
    @classmethod
    def intToTime(cls,time):
        new_time = cls("00:00")
        new_time.time = time
        return new_time
    
    def __init__(self, time):
        time = list(map(int,time.split(":")))
        hour = time[0]
        minute = time[1]
        
        # 시:분 => 분으로 변환
        self.time = hour * 60 + minute
        
    def __add__(self, other):
        new_time = Time(str(self))
        new_time.time += other.time
        
        return new_time
        
    def __sub__(self, other):
        new_time = Time(str(self))
        new_time.time -= other.time
        
        return new_time
    
    def __str__(self):
        hour = self.time // 60
        minute = self.time % 60
        hour = f'0{hour}' if hour < 10 else f'{hour}'
        minute = f'0{minute}' if minute < 10 else f'{minute}'
        
        return f'{hour}:{minute}'
        
        
        