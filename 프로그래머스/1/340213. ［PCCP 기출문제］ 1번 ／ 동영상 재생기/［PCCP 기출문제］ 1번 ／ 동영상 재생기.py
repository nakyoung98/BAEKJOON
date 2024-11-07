def solution(video_len, pos, op_start, op_end, commands):
    # 비디오 객체 생성
    video = Video(video_len, pos, op_start, op_end)
    
    # 명령 수행
    for command in commands:
        video.command(command)
        
    return str(video.cur_pos)

class Time:
    def __init__(self, time):
        time_sep = time.split(":")
        minute = int(time_sep[0])
        second = int(time_sep[1])
        self.time = minute * 60 + second # 초로 형태변환
        
    def __add__(self, other):
        self.time = self.time + other.time

    def __sub__(self, other):
        self.time = self.time - other.time
    
    def __str__(self):
        minute = self.time // 60
        second = self.time % 60
        minute = "00" if minute == 0 else f'0{minute}' if minute < 10 else str(minute)
        second = "00" if second == 0 else f'0{second}' if second < 10 else str(second)
        return f'{minute}:{second}'

class Video:
    def __init__(self, video_len, pos, op_start, op_end):
        self.end = Time(video_len)
        self.cur_pos = Time(pos)
        self.op_start = Time(op_start)
        self.op_end = Time(op_end)
        self.interval = Time("00:10")
        self.__move_to_op_end()

    def prev(self):
        self.cur_pos - self.interval
        # 현재 시간이 0초보다 작아지면 0으로 이동
        if self.cur_pos.time < 0:
            self.cur_pos.time = 0
        # 현재 시간이 오프닝 사이에 있으면 오프닝 끝으로 이동
        self.__move_to_op_end()
        
    def next(self):
        self.cur_pos + self.interval
        # 현재 시간이 end보다 뒤에있으면 end로 이동
        if self.cur_pos.time > self.end.time:
            self.cur_pos.time = self.end.time
        # 현재 시간이 오프닝 사이에 있으면 오프닝 끝으로 이동
        self.__move_to_op_end()
        
    def __move_to_op_end(self):
        if self.op_start.time <= self.cur_pos.time <= self.op_end.time:
            self.cur_pos.time = self.op_end.time
    
    def command(self, command):
        if command == "prev":
            self.prev()
        elif command == "next":
            self.next()