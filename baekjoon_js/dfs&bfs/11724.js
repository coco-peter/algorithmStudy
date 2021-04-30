("use strict");

const fs = require("fs");
const stdin = (process.platform === "linux"
  ? fs.readFileSync("/dev/stdin").toString()
  : `6 8
1 2
2 5
5 1
3 4
4 6
5 4
2 4
2 3
`
).split("\n");

const input = (() => {
  let line = 0;
  return () => stdin[line++];
})();

const [N, M] = input().split(" ").map(Number);
let graph = Array(N + 1)
  .fill(null)
  .map(() => Array());

let isVisited = Array(N + 1).fill(false);

for (let i = 0; i < M; i++) {
  const [startNum, endNum] = input().split(" ").map(Number);
  graph[startNum].push(endNum);
  graph[endNum].push(startNum);
}

cnt = 0;
for (let i = 1; i < N; i++) {
  if (!isVisited[i]) {
    dfs(i);
    cnt += 1;
  }
}

console.log(cnt);

function dfs(start) {
  isVisited[start] = true;
  for (const nextNode of graph[start]) {
    if (!isVisited[nextNode]) {
      dfs(start);
    }
  }
}

function bfs(start) {
  q = [];
  q.push(start);

  while (q.length > 0) {
    node = q.shift();
    isVisited[node] = true;

    for (const nextNode of graph[node]) {
      //   console.log(nextNode);
      if (!isVisited[nextNode]) {
        q.push(nextNode);
      }
    }
  }
}
