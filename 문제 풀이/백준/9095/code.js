// 실 코드
const code = (test) => {
  const fs = require("fs");
  const rawInput = fs.readFileSync(test).toString().split(/\n/g).map(Number);
  //실제 코드 내용
  const T = rawInput.shift();
  let result = 0;
  let results = "";

  const recurse = (n) => {
    if (n === 0) {
      result++;
      return;
    }

    if (n < 0) {
      return;
    }

    for (let i = 1; i <= 3; i++) {
      recurse(n - i);
    }
  };

  for (let t = 0; t < T; t++) {
    const n = rawInput.shift();
    recurse(n);
    results += `${result}\n`;
    result = 0;
  }

  console.log(results);
};

//테스트 루트
const testRoot = "백준/9095";

//테스트 개수대로 추가
const testList = [`${testRoot}/test1.txt`];

//실제 테스트가 돌아가는 코드
for (let test of testList) {
  console.time(`${test} 측정 시작`);
  code(test);
  console.timeEnd(`${test} 측정 시작`);
}
