("use strict");

const fs = require("fs");

const stdin = (
  process.platform === "linux"
    ? fs.readFileSync("/dev/stdin").toString()
    : `4
0 10 15 20
5 0 9 10
6 13 0 12
8 8 9 0
`
).split("\n");

const input = (() => {
  let line = 0;
  return () => stdin[line++];
})();

let N = Number(input());
let graph = Array(N)
  .fill(Number(0))
  .map(() => Array(N).fill(Number(0)));
let isVisited = Array(N).fill(false);
let q = [];
let minValue = Number.MAX_SAFE_INTEGER;
for (let i = 0; i < N; i++) {
  let numList = input().split(" ").map(Number);
  for (let j = 0; j < N; j++) graph[i][j] = numList[j];
}

DFS(0);
console.log(minValue);

function DFS(start) {
  if (start === N) {
    let temp = 0;
    let isPossible = true;
    // console.log(q);
    for (let j = 0; j < N - 1; j++) {
      //   console.log(graph[q[j - 1]][q[j]]);
      if (graph[q[j]][q[j + 1]] === 0) {
        isPossible = false;
        break;
      }
      temp += graph[q[j]][q[j + 1]];
    }
    if (isPossible && graph[q[N - 1]][q[0]] != 0) {
      temp += graph[q[N - 1]][q[0]];
      minValue = Math.min(minValue, temp);
    }
  }

  for (let i = 0; i < N; i++) {
    if (isVisited[i] === true) continue;
    isVisited[i] = true;
    q.push(i);
    DFS(start + 1);
    q.pop();
    isVisited[i] = false;
  }
}
