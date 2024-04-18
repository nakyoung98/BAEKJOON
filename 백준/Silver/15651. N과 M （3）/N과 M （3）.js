  const fs = require("fs");
  const rawInput = fs.readFileSync('dev/stdin').toString().split(/ /g);
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