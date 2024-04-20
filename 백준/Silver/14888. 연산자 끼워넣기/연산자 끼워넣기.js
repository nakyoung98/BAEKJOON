  const fs = require("fs");
  const rawInput = fs.readFileSync('dev/stdin').toString().split(/\n/g);
  const N = +rawInput.shift();
  const A = rawInput.shift().split(/ /g).map(Number);
  const op = rawInput.shift().split(/ /g).map(Number);

  let min = Infinity;
  let max = -Infinity;

  const recurse = (n, now, ops) => {
    // 종료부
    if (N === n) {
      // 최소보다 작으면 최소를 변경
      if (min > now) {
        min = now;
      }

      // 최대보다 크면 최대를 변경
      if (max < now) {
        max = now;
      }

      return;
    }

    //실행부

    if (ops[0] > 0) {
      const newOp = ops.slice();
      newOp[0] -= 1;
      recurse(n + 1, now + A[n], newOp);
    }
    if (ops[1] > 0) {
      const newOp = ops.slice();
      newOp[1] -= 1;
      recurse(n + 1, now - A[n], newOp);
    }
    if (ops[2] > 0) {
      const newOp = ops.slice();
      newOp[2] -= 1;
      recurse(n + 1, now * A[n], newOp);
    }
    if (ops[3] > 0) {
      const newOp = ops.slice();
      newOp[3] -= 1;
      recurse(n + 1, Math.trunc(now / A[n]), newOp);
    }
  };

  recurse(1, A[0], op);

  console.log(max === 0 ? 0 : max);
  console.log(min === 0 ? 0 : min);