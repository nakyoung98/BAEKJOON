class Solution {
  Time video_len_time ;
  Time now_time;
  Time op_start_time;
  Time op_end_time;

  public String solution(String video_len, String pos, String op_start, String op_end, String[] commands) {
      this.video_len_time = new Time(video_len);
      this. now_time = new Time(pos);
      this. op_start_time = new Time(op_start);
      this. op_end_time = new Time(op_end);
      
      
      //커맨드 끝나고 지금 시간이 오프닝 사이인지 무조건 체크
      for(String command: commands){
        TimeCalculator timeCalculator = new TimeCalculator();

        if(timeCalculator.isSmaller(now_time, op_end_time) && timeCalculator.isBigger(op_start_time, now_time)){ //오프닝 구간이면
          this.now_time = op_end_time;
        }
        now_time = this.commander(command);
        if(timeCalculator.isSmaller(now_time, op_end_time) && timeCalculator.isBigger(op_start_time, now_time)){ //오프닝 구간이면
          this.now_time = op_end_time;
        }
        System.out.println(now_time);

      }
      
      return now_time.toString();
  }
  
  public Time commander(String command){
    TimeCalculator timeCalculator =  new TimeCalculator();

    Time result = new Time(0);

    switch (command) {
      case "prev": {
        result =  timeCalculator.sub(now_time, 10);
        break;
      }
      
      case "next": {
        result = timeCalculator.add(now_time, 10, video_len_time);
        break;
      }
    }

    return result;
  }
}


class TimeCalculator {
  public Time add(Time time1, int time2, Time maxTime){
    int result = time1.time + time2;
    if ( result > maxTime.time ){
      result = maxTime.time;
    }


    return new Time(result);
  }

  public Time sub(Time time1, int time2) {
    int result = time1.time - time2;
    if (result < 0){
      result = 0;
    }

    return new Time(result);
  }

  public boolean isBigger(Time time1, Time time2){
    if(time1.time > time2.time) {
      return true;
    }else{
      return false;
    }
  }

  public boolean isSmaller(Time time1, Time time2){
    if(time2.time > time1.time) {
      return true;
    }else{
      return false;
    }
  }

}

class Time{
  int time;  

  public Time(String time){
    String[] splitedTime = time.split(":");
    
    int minute = Integer.parseInt(splitedTime[0]);
    int second = Integer.parseInt(splitedTime[1]);
    this.time = minute * 60 + second;
  }

  public Time(int time) {
    this.time = time;
  }

  public String toString(){
    int minute = time / 60;
    int second = time % 60;

    String strMin = minute >= 10 ? ""+minute : "0"+minute;
    String strSecond = second >= 10 ? ""+second : "0"+second;

    return strMin + ":" + strSecond;
  }
}