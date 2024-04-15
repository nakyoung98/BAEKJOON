// 실 코드
const code = (test) => {
  const fs = require("fs");
  const rawInput = fs.readFileSync(test).toString();
  const input = rawInput.split(/\n/g); // 띄어쓰기 및 개행문자 단위로 나눔
  const datas = input.map((value) => value.split(/ /g));

  //각 row의 max가 담긴 배열
  const max = {max: datas[0][0], row: 0, col: 0};

  //비교하기
  for (let r = 0; r < datas.length; r++) {
    //row 내에서 max 찾기
    for (let c = 0; c < datas[r].length; c++) {
      if (max.max < Number(datas[r][c])) {
        max.max = Number(datas[r][c]);
        max.row = r;
        max.col = c;
      }
    }
  }

  console.log(`${max.max}\n${max.row+1} ${max.col+1}`);
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
