const fs = require("fs");
const rawInput = fs.readFileSync("백준/2439/test.txt").toString();

const N = Number(rawInput);
let result = "";

for (let i = 1; i <= N; i++) {
  for (let j = 1; j <= N - i; j++) {
    result += " ";
  }
  for (let k = 1; k <= i; k++) {
    result += "*";
  }
  result += "\n";
}

console.log(result);
