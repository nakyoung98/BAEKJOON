// 실 코드
const code = (test) => {
  const fs = require("fs");
  const RawInput = fs.readFileSync(test).toString();
  const Inputs = RawInput.split(/\n/g);
  Inputs.forEach((value, i, arr) => (arr[i] = value.split(/ /g)));

  //각 승리횟수를 카운트하는 변수
  let A = 0;
  let B = 0;

  // 1부터 10라운드까지 게임하기
  for (let i = 0; i < 10; i++) {
    // 각각 카드를 하나씩 꺼낸다
    const ACard = +Inputs[0][i];
    const BCard = +Inputs[1][i];

    //각 카드의 수를 비교한다
    //더 큰 수를 가진 사람에게 승리 카운트가 올라간다
    if (ACard > BCard) A++;
    if (BCard > ACard) B++;
  }

  //게임이 끝난 후 승리 카운트를 비교한다
  if (A > B) console.log("A");
  if (A < B) console.log("B");
  if (A === B) console.log("D");
};

//테스트 루트
const testRoot = "백준/10801";

//테스트 개수대로 추가
const testList = [`${testRoot}/test1.txt`, `${testRoot}/test2.txt`];

//실제 테스트가 돌아가는 코드
for (let test of testList) {
  console.time(`${test} 측정 시작`);
  code(test);
  console.timeEnd(`${test} 측정 시작`);
}
