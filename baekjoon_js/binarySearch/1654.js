("use strict");

const fs = require("fs");
const stdin = (process.platform === "linux"
  ? fs.readFileSync("/dev/stdin").toString()
  : `4 11
802
743
457
539
`
).split("\n");

const input = (() => {
  let line = 0;
  return () => stdin[line++];
})();

const [K, N] = input().split(" ").map(Number);
let lineList = [];

for (let i = 0; i < K; i++) lineList.push(Number(input()));

let [left, right] = [1, Math.max(...lineList)];

let maxValue = 1;

while (left <= right) {
  let mid = parseInt((left + right) / 2);

  let cutLine = 0;
  for (line of lineList) {
    cutLine += parseInt(line / mid);
  }

  //   console.log(mid);
  if (cutLine >= N) {
    left = mid + 1;
    if (maxValue < mid) maxValue = mid;
  } else {
    right = mid - 1;
  }
}
console.log(maxValue);
