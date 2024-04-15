// 실 코드
const code = (test) => {
  const fs = require("fs");
  const rawInput = fs.readFileSync('dev/stdin').toString();
  const input = rawInput.split(/\n/g); // 띄어쓰기 및 개행문자 단위로 나눔
  const datas = input.map((value) => value.split(/ /g));

  //각 row의 max가 담긴 배열
  const maxs = [];

  //비교하기
  for (let r = 0; r < datas.length; r++) {
    const maxInRow = { max: Number(datas[r][0]), col: 0 };

    //row 내에서 max 찾기
    for (let c = 1; c < datas[0].length; c++) {
      if (maxInRow.max < Number(datas[r][c])) {
        maxInRow.max = Number(datas[r][c]);
        maxInRow.col = c;
      }
    }

    //해당 row의 max 추가
    maxs.push(maxInRow);
  }

  const maxInMaxs = { max: maxs[0].max, row: 0, col: maxs[0].col };
  // maxs 중 max 찾기
  for (let i = 1; i < maxs.length; i++) {
    if (maxInMaxs.max < maxs[i].max) {
      maxInMaxs.max = maxs[i].max;
      maxInMaxs.row = i;
      maxInMaxs.col = maxs[i].col;
    }
  }

  console.log(`${maxInMaxs.max}\n${maxInMaxs.row+1} ${maxInMaxs.col+1}`);
};

//테스트 루트
const testRoot = "백준/2566";

//테스트 개수대로 추가
const testList = [`${testRoot}/test1.txt`];

//실제 테스트가 돌아가는 코드
for (let test of testList) {
  console.time(`${test} 측정 시작`);
  code(test);
  console.timeEnd(`${test} 측정 시작`);
}
