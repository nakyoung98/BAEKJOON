  const fs = require("fs");
  const rawInput = fs.readFileSync('dev/stdin').toString().split(/ /g);
  const N = +rawInput.shift();
  const M = +rawInput.shift();

  let result = "";

  const recurse = (M, list) => {
    if (M === 0) {
      result += list.join(" ") + "\n";
      return;
    }

    for (let i = 1; i <= N; i++) {
      const newList = list.slice();
      newList.push(i);
      recurse(M - 1, newList);
    }
  };

  recurse(M, []);

  console.log(result);