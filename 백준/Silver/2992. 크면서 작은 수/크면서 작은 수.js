  const fs = require("fs");
  const rawInput = fs.readFileSync('dev/stdin').toString();
  //실제 코드 내용
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