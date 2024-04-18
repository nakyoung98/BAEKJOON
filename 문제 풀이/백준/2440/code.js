// 실 코드
const code = (test) => {
  const fs = require("fs");
  const rawInput = fs.readFileSync(test).toString();
  const N = +rawInput;

  let result = "";

  const recurse = (i) => {
    if (i === N + 1) return;
    recurse(i + 1);
    result += "*".repeat(i) + "\n";
  };

  recurse(1);
  console.log(result);
};

//테스트 루트
const testRoot = "백준/2440";

//테스트 개수대로 추가
const testList = [`${testRoot}/test1.txt`];

//실제 테스트가 돌아가는 코드
for (let test of testList) {
  console.time(`${test} 측정 시작`);
  code(test);
  console.timeEnd(`${test} 측정 시작`);
}
