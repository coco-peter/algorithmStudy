("use strict");

const fs = require("fs");
const stdin = (process.platform === "linux"
  ? fs.readFileSync("/dev/stdin").toString()
  : `11
1 4
3 5
0 6
5 7
3 8
5 9
8 11
7 11
8 12
2 13
12 14
`
).split("\n");

const input = (() => {
  let line = 0;
  return () => stdin[line++];
})();

const N = Number(input());

let timeTable = [];

for (let i = 0; i < N; i++) {
  const [start, end] = input().split(" ").map(Number);
  timeTable.push([start, end]);
}

timeTable.sort((a, b) => a[1] - b[1] || a[0] - b[0]);
// timeTable.sort((a, b) => a[1] - b[1]);
// timeTable.sort((a, b) => a[0] - b[0]);
console.log(timeTable);

let start = timeTable[0][0];
let end = timeTable[0][1];
let cnt = 1;
for (let i = 1; i < N; i++) {
  if (timeTable[i][0] < end) continue;
  else {
    //console.log(start, end);
    start = timeTable[i][0];
    end = timeTable[i][1];
    cnt++;
  }
}

console.log(cnt);
