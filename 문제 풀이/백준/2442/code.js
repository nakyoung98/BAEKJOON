// 실 코드
const code = (test) => {
  const fs = require("fs");
  const rawInput = fs.readFileSync(test);
  const N = Number(rawInput);

  let result = "";

  for (let i = 1; i <= N; i++) {
    result = result.concat(" ".repeat(N - i), "*".repeat(2 * i - 1), "\n");
  }

  console.log(result);
};

//테스트 루트
const testRoot = "백준/2442";

//테스트 개수대로 추가
const testList = [`${testRoot}/test.txt`];

//실제 테스트가 돌아가는 코드
for (let test of testList) {
  console.time(`${test} 측정 시작`);
  code(test);
  console.timeEnd(`${test} 측정 시작`);
}
