("use strict");

const fs = require("fs");
const stdin = (process.platform === "linux"
  ? fs.readFileSync("/dev/stdin").toString()
  : `10
1 5 2 1 4 3 4 5 2 1
`
).split("\n");

const input = (() => {
  let line = 0;
  return () => stdin[line++];
})();

let N = Number(input());

let numList = input().split(" ").map(Number);
let dpFront = Array(N).fill(Number(1));
let dpBack = Array(N).fill(Number(1));
let maxDp = Array(N).fill(Number(0));

// console.log(dpFront);

for (let i = 1; i < N; i++) {
  for (let j = 0; j < i; j++) {
    if (numList[i] > numList[j])
      dpFront[i] = Math.max(dpFront[i], dpFront[j] + 1);
  }
}

for (let i = N - 1; i > -1; i--) {
  for (let j = N - 1; j > i; j--) {
    if (numList[i] > numList[j]) dpBack[i] = Math.max(dpBack[i], dpBack[j] + 1);
  }

  maxDp[i] = dpFront[i] + dpBack[i] - 1;
}
// console.log(dpFront, dpBack);

let maxLength = 0;
for (let i = 0; i < N; i++) {
  maxLength = Math.max(maxLength, maxDp[i]);
}

console.log(String(maxLength));
