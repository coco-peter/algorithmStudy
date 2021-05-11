("use strict");

const fs = require("fs");

const stdin = (
  process.platform === "linux"
    ? fs.readFileSync("/dev/stdin").toString()
    : `15 28 19
`
).split("\n");

const input = (() => {
  let line = 0;
  return () => stdin[line++];
})();

const [E, S, M] = input().split(" ").map(Number);

let days = 1;
let tempE = 1;
let tempS = 1;
let tempM = 1;
// console.log(tempE, tempS, tempM);
while (true) {
  if (tempE === E && tempS === S && tempM == M) break;
  days++;
  if (tempE + 1 < 16) tempE++;
  else tempE = 1;
  if (tempS + 1 < 29) tempS++;
  else tempS = 1;
  if (tempM + 1 < 20) tempM++;
  else tempM = 1;
}

console.log(days);
