("use strict");

const fs = require("fs");

const stdin = (process.platform === "linux"
  ? fs.readFileSync("/dev/stdin").toString()
  : `5 0
-7 -3 -2 5 8
`
).split("\n");

const input = (() => {
  let line = 0;
  return () => stdin[line++];
})();

const [N, S] = input().split(" ").map(Number);
const inputlist = input().split(" ").map(Number);
let q = [];
let isVisited = Array(N).fill(false);
let resultCnt = 0;

for (let i = 1; i < inputlist.length + 1; i++) DFS(0, 0, i, inputlist);
console.log(resultCnt);

function DFS(idx, start, targetLength, inputlist) {
  if (start === targetLength) {
    let cnt = 0;
    for (let i = 0; i < inputlist.length; i++)
      if (isVisited[i] === true) {
        // process.stdout.write(`${inputlist[i]} `);
        cnt += inputlist[i];
      }
    // console.log(cnt, S);
    if (cnt === S) resultCnt++;
  }

  for (let i = idx; i < inputlist.length; i++) {
    if (isVisited[i] === false) {
      isVisited[i] = true;
      //   q.push(inputlist[i]);
      DFS(i, start + 1, targetLength, inputlist);
      //   q.pop();
      isVisited[i] = false;
    }
  }
}
