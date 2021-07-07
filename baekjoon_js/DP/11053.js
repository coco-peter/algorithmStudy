("use strict");

const fs = require("fs");
const stdin = (process.platform === "linux"
  ? fs.readFileSync("/dev/stdin").toString()
  : `6
10 20 10 30 20 50
`
).split("\n");

const input = (() => {
  let line = 0;
  return () => stdin[line++];
})();

let N = Number(input());

let numList = input().split(" ").map(Number);
let dp = Array(N).fill(Number(1));

for (let i = 0; i < N; i++) {
  for (let j = 0; j < i; j++) {
    if (numList[i] > numList[j]) dp[i] = Math.max(dp[i], dp[j] + 1);
  }
}

// console.log(dp);

// 배열안에 있는것들중 최대값을 찾을때는? ...
console.log(Math.max(...dp));
