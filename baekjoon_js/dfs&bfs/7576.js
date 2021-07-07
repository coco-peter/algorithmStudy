("use strict");

const fs = require("fs");
const stdin = (process.platform === "linux"
  ? fs.readFileSync("/dev/stdin").toString()
  : `2 2
1 -1
-1 1
`
).split("\n");

const input = (() => {
  let line = 0;
  return () => stdin[line++];
})();

// console.log(cnt);
const [M, N] = input().split(" ").map(Number);

let graph = Array(N)
  .fill(Number(0))
  .map(() => Array(M).fill(Number(0)));

let q = [];

let dx = [1, -1, 0, 0];
let dy = [0, 0, 1, -1];

for (let y = 0; y < N; y++) {
  numList = input().split(" ").map(Number);
  for (let x = 0; x < M; x++) {
    graph[y][x] = numList[x];
    // console.log(numList[x]);
    if (numList[x] === 1) {
      q.push([x, y]);
    }
  }
}

while (q.length > 0) {
  let [x, y] = q.shift();

  for (let i = 0; i < 4; i++) {
    let [nx, ny] = [x + dx[i], y + dy[i]];

    if (nx >= 0 && nx < M && ny >= 0 && ny < N) {
      // console.log(nx, ny, graph[ny][nx], isVisited[ny][nx]);
      if (graph[ny][nx] === 0) {
        graph[ny][nx] = graph[y][x] + 1;
        q.push([nx, ny]);
      }
    }
  }
  // console.log(graph);
}

let maxValue = 0;
let isPossible = true;
graph.forEach((element) => {
  element.forEach((e) => {
    maxValue = Math.max(maxValue, e);
    if (e === 0) isPossible = false;
  });
});

if (isPossible) console.log(maxValue - 1);
else console.log(-1);
