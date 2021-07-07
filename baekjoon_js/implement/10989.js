const fs = require("fs");
const stdin = (process.platform === "linux"
  ? fs.readFileSync("/dev/stdin").toString()
  : `10
5
2
3
1
4
2
3
5
1
7
`
).split("\n");

const input = (() => {
  let line = 0;
  return () => stdin[line++];
})();

let N = Number(input());
let numList = Array(10001).fill(Number(0));

for (let i = 0; i < N; i++) {
  numList[Number(input())]++;
}

for (let i = 1; i < 10001; i++) {
  if (numList[i] === 0) continue;
  for (let j = 0; j < numList[i]; j++) {
    console.log(i);
  }
}
