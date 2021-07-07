("use strict");

const fs = require("fs");
const stdin = (process.platform === "linux"
  ? fs.readFileSync("/dev/stdin").toString()
  : `3
`
).split("\n");

const input = (() => {
  let line = 0;
  return () => stdin[line++];
})();

const [A, B] = input().split(" ").map(Number);
const N = Number(input());
const numList = input().split(" ").map(Number);

let binaryList = [
  0,
  1,
  2,
  3,
  4,
  5,
  6,
  7,
  8,
  9,
  10,
  11,
  12,
  13,
  14,
  15,
  16,
  17,
  18,
  19,
  20,
  21,
  22,
  23,
  24,
  25,
  26,
  27,
  28,
  29,
];

for (let i = 0; i < N; i++) {
  console.log(parseInt(num, 8).toString(2));
}
