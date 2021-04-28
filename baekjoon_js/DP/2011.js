("use strict");

const fs = require("fs");
const stdin = (process.platform === "linux"
  ? fs.readFileSync("/dev/stdin").toString()
  : `25114
`
).split("\n");

const input = (() => {
  let line = 0;
  return () => stdin[line++];
})();

let N = Number(input());
let length = String(N).length;
let maxValue = 0;

divideNum(N);

function divideNum(N) {
  for (let i = 1; i < length; i++) {
    let head = parseInt(N / Math.pow(10, i));
    let tail = N % Math.pow(10, i);
    // console.log(head, tail);
    if (head < 27 && head > 0 && tail < 27 && tail > 0) {
      divideNum(tail);
      maxValue += 1;
    } else if (head < 27 && head > 0 && tail > 26) {
      divideNum(tail);
    }
  }
}

console.log(maxValue % 1000000);
