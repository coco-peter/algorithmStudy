("use strict");

const fs = require("fs");
const stdin = (process.platform === "linux"
  ? fs.readFileSync("/dev/stdin").toString()
  : `6
10
20
15
25
10
20
`
).split("\n");

const input = (() => {
  let line = 0;
  return () => stdin[line++];
})();

let N = Number(input());

let stepList = Array(N + 1).fill(Number(0));
let dp = Array(N + 1).fill(Number(0));
for (let i = 0; i < N; i++) {
  let stepValue = Number(input());
  stepList[i + 1] = stepValue;
}

for (let i = 1; i < N + 1; i++) {
  //   console.log(dp);
  if (i === 1) {
    dp[i] = stepList[i];
  } else if (i === 2) {
    dp[i] = stepList[i] + stepList[i - 1];
  } else {
    dp[i] = Math.max(
      stepList[i] + stepList[i - 1] + dp[i - 3],
      dp[i - 2] + stepList[i]
    );
  }
}

// console.log(dp);
console.log(String(dp[N]));
