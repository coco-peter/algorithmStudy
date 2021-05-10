("use strict");

const fs = require("fs");

const stdin = (process.platform === "linux"
  ? fs.readFileSync("/dev/stdin").toString()
  : `7 1 2 3 4 5 6 7
8 1 2 3 5 8 13 21 34
0
`
).split("\n");

const input = (() => {
  let line = 0;
  return () => stdin[line++];
})();

let q;
const pickCnt = 6;
let isVisited;

// function printQ(inputlist) {
//   for (let i = 0; i < ; i++) {
//     // process.stdout.write(`${q[i]} `);
//     process.stdout.write(`${inputlist[i]} `);
//     if (isVisited[i] === true) process.stdout.write(`${inputlist[i]} `);
//   }
//   console.log("");
// }

// Combination
function DFS(idx, start, inputlist) {
  if (start === pickCnt) {
    for (let i = 1; i < inputlist.length + 1; i++) {
      // process.stdout.write(`${q[i]} `);
      // process.stdout.write(`${inputlist[i]} `);
      if (isVisited[i - 1] === true) process.stdout.write(`${inputlist[i]} `);
    }
    console.log("");
  }

  for (let i = idx; i < inputlist.length; i++) {
    if (isVisited[i] === false) {
      isVisited[i] = true;
      //   q.push(inputlist[i]);
      DFS(i, start + 1, inputlist);
      //   q.pop();
      isVisited[i] = false;
    }
  }
}

while (true) {
  const inputlist = input().split(" ").map(Number);
  if (inputlist[0] === 0) break;
  let numList = Array(inputlist[0]).fill(0);
  q = [];
  isVisited = Array(inputlist[0]).fill(false);
  for (let i = 0; i < inputlist[0]; i++) numList[i] = inputlist[i + 1];

  DFS(0, 0, inputlist);
  console.log("");
}
