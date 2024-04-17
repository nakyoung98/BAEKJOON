  const fs = require("fs");
  const rawInput = fs.readFileSync('dev/stdin').toString().split(/\n/g);
  const Bingo = rawInput.slice(0, 5);
  Bingo.forEach((value, i, arr) => (arr[i] = value.split(/ /g).map(Number)));
  const Calls = rawInput.slice(5);
  Calls.forEach((value, i, arr) => (arr[i] = value.split(/ /g).map(Number)));

  //빙고 개수
  let Bingos = 0;

  // 번호 부르기 5*5 (O(1))
  for (let row = 0; row < 5; row++) {
    for (let col = 0; col < 5; col++) {
      const call = Calls[row][col];

      let BingoRow;
      let BingoCol;
      // 빙고에서 번호 찾기
      for (let i = 0; i < 5; i++) {
        for (let j = 0; j < 5; j++) {
          if (Bingo[i][j] === call) {
            BingoRow = i;
            BingoCol = j;
            // 빙고 배열에서 0으로 만들기
            Bingo[i][j] = 0;
          }
        }
      }

      //빙고 체크하기
      //가로
      if (Bingo[BingoRow].every((value) => value === 0)) Bingos++;
      //세로
      if (Bingo.every((_, r) => Bingo[r][BingoCol] === 0)) Bingos++;
      //대각선
      if (BingoRow === 2 && BingoCol === 2) {
        // 빙고 가운데라면

        //왼쪽 대각선
        if (Bingo.every((bingoRow, i) => bingoRow[i] === 0)) Bingos++;
        //오른쪽 대각선
        if (Bingo.every((bingoRow, i) => bingoRow[4 - i] === 0)) Bingos++;
      } else if (BingoRow === BingoCol) {
        //(x,x) 라면

        //왼쪽 대각선
        if (Bingo.every((bingoRow, i) => bingoRow[i] === 0)) Bingos++;
      } else if (BingoRow === 4 - BingoCol) {
        //(x,4-x) 라면

        //오른쪽 대각선
        if (Bingo.every((bingoRow, i) => bingoRow[4 - i] === 0)) Bingos++;
      }

      // 빙고 개수가 3줄을 넘으면
      if (Bingos >= 3) {
        // 부른 번호 row * 5 + col + 1
        console.log(row * 5 + col + 1);
        return;
      }
    }
  }