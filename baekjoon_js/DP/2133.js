("use strict");

const fs = require("fs");
const stdin = (process.platform === "linux"
  ? fs.readFileSync("/dev/stdin").toString()
  : `4
`
).split("\n");

const input = (() => {
  let line = 0;
  return () => stdin[line++];
})();

let N = Number(input());

let dp = Array(31).fill(Number(0));

dp[2] = 3;

for (let i = 4; i < 31; i += 2) {
  dp[i] = dp[i - 2] * 3 + 2;
}

console.log(dp[N]);
