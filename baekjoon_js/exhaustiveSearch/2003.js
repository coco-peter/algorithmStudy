("use strict");

const fs = require("fs");

const stdin = (process.platform === "linux"
  ? fs.readFileSync("/dev/stdin").toString()
  : `10 5
1 2 3 4 2 5 3 1 1 2
`
).split("\n");

const input = (() => {
  let line = 0;
  return () => stdin[line++];
})();

const [N, S] = input().split(" ").map(Number);
const inputlist = input().split(" ").map(Number);
let isVisited = Array(N).fill(false);
let resultCnt = 0;

for (let i = 0; i < inputlist.length; i++) {
  let tempSum = 0;
  for (let j = i; j < inputlist.length; j++) {
    //   process.stdout.write(`${inputlist[k]} `);

    tempSum += inputlist[j];
    // DFS(0, j, i, inputlist);
    // console.log(tempSum, S);
    if (tempSum === S) {
      resultCnt++;
      break;
    } else if (tempSum > S) {
      break;
    }
  }
}
console.log(resultCnt);

function DFS(idx, start, targetLength, inputlist) {
  if (start === targetLength) {
    let cnt = 0;
    for (let i = 0; i < inputlist.length; i++)
      if (isVisited[i] === true) {
        process.stdout.write(`${inputlist[i]} `);
        cnt += inputlist[i];
      }
    console.log(cnt, S);
    if (cnt === S) resultCnt++;
  }

  for (let i = idx; i < inputlist.length; i++) {
    if (isVisited[i] === false) {
      isVisited[i] = true;
      DFS(i, start + 1, targetLength, inputlist);
      isVisited[i] = false;
    }
  }
}
