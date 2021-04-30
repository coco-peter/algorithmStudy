("use strict");

const fs = require("fs");
const stdin = (process.platform === "linux"
  ? fs.readFileSync("/dev/stdin").toString()
  : `3 15
`
).split("\n");

const input = (() => {
  let line = 0;
  return () => stdin[line++];
})();

const [M, N] = input().split(" ").map(Number);
let primeList = Array(1000001).fill(Number(0));

primeList[1] = primeList[0] = 1;

for (let i = 2; i < parseInt(primeList.length / 2); i++) {
  for (let j = i + i; j < primeList.length; j += i) {
    if (primeList[j] === 0) primeList[j] = 1;
  }
}
// setPrimeNumber();

for (let i = M; i <= N; i++) {
  if (primeList[i] === 0) console.log(i);
}

// function setPrimeNumber() {
//   for (let i = 4; i <= N; i += 2) {
//     if (primeList[i] === 0) primeList[i] = 1;
//   }
//   for (let i = 6; i <= N; i += 3) {
//     if (primeList[i] === 0) primeList[i] = 1;
//   }
// }
