  const fs = require("fs");
  const rawInput = fs.readFileSync('dev/stdin');
  const N = Number(rawInput);

  let result = "";

  for (let i = 1; i <= N; i++) {
    result = result.concat(" ".repeat(N - i), "*".repeat(2 * i - 1), "\n");
  }

  console.log(result);