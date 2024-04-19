  const fs = require("fs");
  const rawInput = fs.readFileSync('dev/stdin').toString().split(/\n/g).map(Number);
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