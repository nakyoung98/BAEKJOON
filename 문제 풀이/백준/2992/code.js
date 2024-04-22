// 실 코드
const code = (test) => {
  const fs = require("fs");
  const rawInput = fs.readFileSync(test).toString();
  const input = String(Number(rawInput)).split("").map(Number);
  const inputLength = input.length;
  const defaultNumber = Number(rawInput);

  let min = Infinity;

  const visited = new Array(inputLength).fill(false);
  const current = new Array(inputLength);

  //재귀함수
  const recurse = (n) => {
    // 종료부
    if (n === inputLength) {
      const number = +current.join("");

      if (number > defaultNumber && number < min) {
        min = number;
      }

      return;
    }

    // 실행부
    for (let i = 0; i < inputLength; i++) {
      if (!visited[i]) {
        visited[i] = true;
        current[n] = input[i];
        recurse(n + 1);
        visited[i] = false;
      }
    }
  };

  recurse(0);

  console.log(min === Infinity ? 0 : min);
};

//테스트 루트
const testRoot = "백준/2992";

//테스트 개수대로 추가
const testList = [
  `${testRoot}/test1.txt`,
  `${testRoot}/test2.txt`,
  `${testRoot}/test3.txt`,
  `${testRoot}/test4.txt`,
  `${testRoot}/test5.txt`,
  `${testRoot}/test6.txt`,
  `${testRoot}/test7.txt`,
];

//실제 테스트가 돌아가는 코드
for (let test of testList) {
  console.time(`${test} 측정 시작`);
  code(test);
  console.timeEnd(`${test} 측정 시작`);
}
