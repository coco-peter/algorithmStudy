("use strict");

const fs = require("fs");
const stdin = (process.platform === "linux"
  ? fs.readFileSync("/dev/stdin").toString()
  : `100
`
).split("\n");

const input = (() => {
  let line = 0;
  return () => stdin[line++];
})();

let t = input();
let graph = Array(101)
  .fill(BigInt(0))
  .map(() => Array(10).fill(BigInt(0)));

for (let x = 1; x < 10; x++) graph[1][x] = BigInt(1);

for (let y = 2; y < 101; y++) {
  for (let x = 0; x < 10; x++) {
    graph[y][x] = BigInt(0);
    if (x > 0) graph[y][x] += graph[y - 1][x - 1];
    if (x < 9) graph[y][x] += graph[y - 1][x + 1];
  }
}
// console.log(graph);
let sum = BigInt(0);
// console.log(graph[t]);
for (let i = 0; i < 10; i++) {
  sum += BigInt(graph[t][i]);
}
console.log(String(sum % BigInt(1000000000)));
