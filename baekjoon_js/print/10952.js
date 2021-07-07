("use strict");

const fs = require("fs");
const stdin = (process.platform === "linux"
  ? fs.readFileSync("/dev/stdin").toString()
  : `1 1
2 3
3 4
9 8
5 2
0 0
`
).split("\n");

const input = (() => {
  let line = 0;
  return () => stdin[line++];
})();

// let t = input();
while (true) {
  const [a, b] = input().split(" ").map(Number);
  if (a === 0 && b === 0) break;
  console.log(a + b);
}
