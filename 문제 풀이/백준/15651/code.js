// 실 코드
const code = (test) => {
  const fs = require("fs");
  const rawInput = fs.readFileSync(test).toString().split(/ /g);
  const N = +rawInput.shift();
  const M = +rawInput.shift();

  let result = "";
  const list = new Array(M);

  const recurse = (m) => {
    if (m === M) {
      result += list.join(" ") + "\n";
      return;
    }
  
    for (let i = 1; i <= N; i++) {
      list[m] = i;
      recurse(m + 1);
    }
  };
  
  recurse(0);
  
  console.log(result);
};

//테스트 루트
const testRoot = "백준/15651";

//테스트 개수대로 추가
const testList = [`${testRoot}/test1.txt`, `${testRoot}/test2.txt`, `${testRoot}/test3.txt`];

//실제 테스트가 돌아가는 코드
for (let test of testList) {
  console.time(`${test} 측정 시작`);
  code(test);
  console.timeEnd(`${test} 측정 시작`);
}
