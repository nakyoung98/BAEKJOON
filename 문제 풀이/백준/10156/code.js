// 실 코드
const code = (test) => {
  const fs = require("fs");
  const rawInput = fs.readFileSync(test).toString();
  const inputs = rawInput.split(" "); /** 입력형식이 300 4 1000*/

  const K = Number(inputs[0]);
  const N = Number(inputs[1]);
  const M = Number(inputs[2]);

  const total = K * N;
  const left = total - M;

  if (left <= 0) console.log(0);
  else console.log(left);
};

//테스트
const testRoot = "백준/10156";
const testList = [`${testRoot}/test1.txt`, `${testRoot}/test2.txt`, `${testRoot}/test3.txt`, `${testRoot}/test4.txt`];

for (let test of testList) {
  console.time(`${test} 측정 시작`);
  code(test);
  console.timeEnd(`${test} 측정 시작`);
}

