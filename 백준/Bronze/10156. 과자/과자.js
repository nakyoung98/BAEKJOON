  const fs = require("fs");
  const rawInput = fs.readFileSync('dev/stdin').toString();
  const inputs = rawInput.split(" ");
  const K = Number(inputs[0]);
  const N = Number(inputs[1]);
  const M = Number(inputs[2]);

  const total = K * N;
  const left = total - M;

  if (left <= 0) console.log(0);
  else console.log(left);