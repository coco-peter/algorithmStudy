("use strict");

const fs = require("fs");
const stdin = (process.platform === "linux"
  ? fs.readFileSync("/dev/stdin").toString()
  : `3
`
).split("\n");

const input = (() => {
  let line = 0;
  return () => stdin[line++];
})();

const N = Number(input());

let history = [];
let cnt = 0;

function hanoi(start, mid, end, N) {
  if (N === 1) {
    history.push([start, end]);
  } else {
    hanoi(start, end, mid, N - 1);
    history.push([start, end]);
    hanoi(mid, start, end, N - 1);
  }
  cnt++;
}

hanoi(1, 2, 3, N);

console.log(cnt);
for (let i = 0; i < history.length; i++)
  console.log(`${history[i][0]} ${history[i][1]}`);
