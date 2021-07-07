const fs = require("fs");

const stdin = (
  process.platform === "linux"
    ? fs.readFileSync("/dev/stdin").toString()
    : `10
1 1 1 0 0 0 0 1 1 1
1 1 1 1 0 0 0 0 1 1
1 0 1 1 0 0 0 0 1 1
0 0 1 1 1 0 0 0 0 1
0 0 0 1 0 0 0 0 0 1
0 0 0 0 0 0 0 0 0 1
0 0 0 0 0 0 0 0 0 0
0 0 0 0 1 1 0 0 0 0
0 0 0 0 1 1 1 0 0 0
0 0 0 0 0 0 0 0 0 0
`
).split("\n");

const input = (() => {
  let line = 0;
  return () => stdin[line++];
})();

const N = Number(input());

let graph = Array(N)
  .fill(0)
  .map(() => Array(N).fill(0));

let isVisited = Array(N)
  .fill(false)
  .map(() => Array(N).fill(false));

let color = Array(N)
  .fill(-1)
  .map(() => Array(N).fill(-1));

let minValue = Number.MAX_SAFE_INTEGER;
let colorIdx = 0;

let dx = [1, -1, 0, 0];
let dy = [0, 0, -1, 1];

for (let y = 0; y < N; y++) {
  let column = input().split(" ").map(Number);
  for (let x = 0; x < N; x++) {
    graph[y][x] = column[x];
    // if (graph[y][x] === 1) q.push([x, y]);
  }
}

for (let y = 0; y < N; y++) {
  for (let x = 0; x < N; x++) {
    if (isVisited[y][x] === false && graph[y][x] === 1) {
      BFS(x, y);
      colorIdx++;
    }
  }
}

isVisited = Array(N)
  .fill(false)
  .map(() => Array(N).fill(false));

colorIdx = 0;
for (let y = 0; y < N; y++) {
  for (let x = 0; x < N; x++) {
    if (color[y][x] === colorIdx) {
      calLength(x, y);
      colorIdx++;
    }
  }
}

console.log(minValue);

function calLength(x, y) {
  let q = [];
  q.push([x, y]);
  let nowColor = color[y][x];
  while (q.length > 0) {
    let [nowX, nowY] = q.shift();
    isVisited[nowY][nowX] = true;

    console.log(nowX, nowY, nowColor);
    for (let i = 0; i < 4; i++) {
      let [nx, ny] = [nowX + dx[i], nowY + dy[i]];
      if (nx >= 0 && nx < N && ny >= 0 && ny < N) {
        if (color[ny][nx] === -1) {
          q.push([nx, ny]);
          graph[ny][nx] == Math.min(graph[ny][nx], graph[nowY][nowX] + 1);
        } else if (color[ny][nx] !== -1 && color[ny][nx] !== nowColor) {
          minValue = Math.min(minValue, graph[nowY][nowX]);
        }
      }
    }
  }
}

function BFS(x, y) {
  let q = [];
  q.push([x, y]);
  color[y][x] = colorIdx;

  while (q.length > 0) {
    let [nowX, nowY] = q.shift();
    isVisited[nowY][nowX] = true;

    for (let i = 0; i < 4; i++) {
      let [nx, ny] = [nowX + dx[i], nowY + dy[i]];
      if (nx >= 0 && nx < N && ny >= 0 && ny < N) {
        if (graph[ny][nx] === 1 && isVisited[ny][nx] == false) {
          q.push([nx, ny]);
          color[ny][nx] = colorIdx;
        }
      }
    }
  }
}
