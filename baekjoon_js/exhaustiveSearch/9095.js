("use strict");

const fs = require("fs");

const stdin = (
  process.platform === "linux"
    ? fs.readFileSync("/dev/stdin").toString()
    : `3
4
7
10
`
).split("\n");

const input = (() => {
  let line = 0;
  return () => stdin[line++];
})();

let T = Number(input());
let dp = Array(11).fill(Number(0));
dp[0] = 1;
dp[1] = 2;
dp[2] = 4;
for (let i = 3; i < 11; i++) dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3];
while (T--) {
  let n = Number(input());
  console.log(dp[n - 1]);
}
