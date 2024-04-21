  const fs = require("fs");
  const rawInput = fs.readFileSync('dev/stdin').toString().split(/\n/g);
  const K = +rawInput.shift();
  const Arrows = rawInput.shift().split(/ /g);
  const Numbers = new Array(K + 1);
  const Visits = new Array(K + 1).fill(false);

  let min = Infinity;
  let max = -Infinity;

  const recurse = (k) => {
    // 조기 리턴 (중복값 검사)
    if (Numbers.indexOf(Numbers[k]) !== k) return;

    // 끝까지 도달 시 종료
    if (k === K) {
      const answer = Numbers.join("");
      if (+answer > +max) {
        max = answer;
      }
      if (+answer < +min) {
        min = answer;
      }

      return;
    }

    for (let n = 0; n < 10; n++) {
      if (Visits[n]) continue;

      switch (Arrows[k]) {
        case "<":
          if (Numbers[k] < n) {
            Visits[n] = true;
            Numbers[k + 1] = n;
            recurse(k + 1);
            Visits[n] = false;
          }
          break;
        case ">":
          if (Numbers[k] > n) {
            Visits[n] = true;
            Numbers[k + 1] = n;
            recurse(k + 1);
            Visits[n] = false;
          }
          break;
      }
    }
  };

  // 실행부
  for (let n = 0; n < 10; n++) {
    Numbers[0] = n;
    recurse(0);
  }

  console.log(max);
  console.log(min);