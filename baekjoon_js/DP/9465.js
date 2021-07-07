("use strict");

const fs = require("fs");
const stdin = (process.platform === "linux"
  ? fs.readFileSync("/dev/stdin").toString()
  : `2
5
50 10 100 20 40
30 50 70 10 60
7
10 30 10 50 100 20 40
20 40 30 50 60 20 80
`
).split("\n");

const input = (() => {
  let line = 0;
  return () => stdin[line++];
})();

let t = Number(input());
while (t) {
  let N = Number(input());

  let graph = Array(2)
    .fill(0)
    .map(() => Array(N).fill(0));

  for (let i = 0; i < 2; i++) {
    let numList = input().split(" ").map(Number);

    for (let j = 0; j < N; j++) {
      graph[i][j] = numList[j];
    }
  }

  for (let x = 1; x < N; x++) {
    if (x === 1) {
      graph[0][x] += graph[1][x - 1];
      graph[1][x] += graph[0][x - 1];
      continue;
    }
    for (let y = 0; y < 2; y++) {
      if (y === 1) {
        graph[y][x] = Math.max(
          graph[y][x] + graph[y - 1][x - 1],
          graph[y][x] + graph[y - 1][x - 2]
        );
      }
      if (y === 0) {
        graph[y][x] = Math.max(
          graph[y][x] + graph[y + 1][x - 1],
          graph[y][x] + graph[y + 1][x - 2]
        );
      }
    }
  }

  console.log(String(Math.max(graph[0][N - 1], graph[1][N - 1])));

  t--;
}
