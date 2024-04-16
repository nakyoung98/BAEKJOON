// 실 코드
const code = (test) => {
  const input = require("fs").readFileSync(test).toString().trim().split("\n");
  const N = Number(input.shift());
  const student = input.map((el) => el.split(" ").map(Number));
  let count = new Array(N).fill(0);

  for (let i = 0; i < N; i++) {
    for (let j = 0; j < N; j++) {
      if (i === j) continue;
      for (let k = 0; k < 5; k++) {
        if (student[i][k] === student[j][k]) {
          count[i]++;
          break;
        }
      }
    }
  }

  console.log(count.indexOf(Math.max(...count)) + 1);
};

//테스트 루트
const testRoot = "백준/1268";

//테스트 개수대로 추가
const testList = [`${testRoot}/test1.txt`];

//실제 테스트가 돌아가는 코드
for (let test of testList) {
  console.time(`${test} 측정 시작`);
  code(test);
  console.timeEnd(`${test} 측정 시작`);
}
