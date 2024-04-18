  const fs = require("fs");
  const rawInput = fs.readFileSync('dev/stdin').toString().split(/ |\n/g);

  const C = +rawInput.shift();
  const R = +rawInput.shift();
  const K = +rawInput.shift();

  const Seats = new Array(R + 2); //위 아래 바운더리 만들기 위해 R+2
  for (let i = 0; i < Seats.length; i++) {
    Seats[i] = new Array(C + 2).fill(0); //모든 값을 0으로 초기화, 양 옆 바운더리 만들기 위해 C+2
  }

  // 바운더리 값 -1로 변경
  Seats.forEach((_, i, arr) => {
    if (i === 0 || i === Seats.length - 1) {
      //모든 칸 -1로 변경
      arr[i].fill(-1);
    } else {
      //앞과 뒤를 -1로 변경
      arr[i][0] = -1;
      arr[i][arr[i].length - 1] = -1;
    }
  });

  //D,R,U,L 이동
  const move = [
    [0, 1], //D
    [1, 0], //R
    [0, -1], //U
    [-1, 0], //L
  ];

  //시작 포지션
  const position = [1, 0];
  let curK = 1;
  //끝낼지 말지 결정
  let isFinish = false;
  let isSeatable = false;

  while (!isFinish) {
    // 내가 갈 길이 0일 때까지 반복
    while (Seats[position[1] + move[0][1]][position[0] + move[0][0]] === 0) {
      //칸 이동하기
      position[0] += move[0][0];
      position[1] += move[0][1];

      // (x,y) 좌표기 때문에 Seats[y][x]로 입력
      //좌석에 사람 앉히기 - 이전 계산에서 내가 다음 갈 길이 0임을 확인했기 때문에 착석 가능
      Seats[position[1]][position[0]] = curK;

      //만약 지금 사람이 K면 종료
      if (curK === K) {
        isFinish = true;
        isSeatable = true;
        break;
      }
      // 아니면 다음 사람 부르기
      curK++;
    }

    if (isFinish) break;

    //현재 문제 => 위치를 원복해도, 이미 내 자리 값이 0이 아니라 갈 곳이 없음 돌아와서 한칸 이동시키는 것이 맞을 듯
    
    // 먼저 더이상 갈 곳이 없는지 확인
    if (
      Seats[position[1]][position[0] + 1] !== 0 &&
      Seats[position[1]][position[0] - 1] !== 0 &&
      Seats[position[1] + 1][position[0]] !== 0 &&
      Seats[position[1] - 1][position[0]] !== 0
    ) {
      // 더이상 갈 곳이 없으므로 종료
      isFinish = true;
      break;
    }

    // 이동 순서 변경하기
    const newMove = move.shift();
    // 지금 이동순서는 다시 맨 뒤로 보내기
    move.push(newMove);
  }

  // 앉을 수 있으면 포지션 출력
  if (isSeatable) {
    console.log(...position);
  } else {
    //앉을 수 없으면 0 출력
    console.log(0);
  }