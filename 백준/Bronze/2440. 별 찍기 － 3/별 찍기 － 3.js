  const fs = require("fs");
  const rawInput = fs.readFileSync('dev/stdin').toString();
  const N = +rawInput;

  let result = "";

  const recurse = (i) => {
    if (i === N + 1) return;
    recurse(i + 1);
    result += "*".repeat(i) + "\n";
  };

  recurse(1);
  console.log(result);