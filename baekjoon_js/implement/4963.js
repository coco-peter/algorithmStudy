const fs = require("fs");

const stdin = (
  process.platform === "linux"
    ? fs.readFileSync("/dev/stdin").toString()
    : `1 1
0
2 2
0 1
1 0
3 2
1 1 1
1 1 1
5 4
1 0 1 0 0
1 0 0 0 0
1 0 1 0 1
1 0 0 1 0
5 4
1 1 1 0 1
1 0 1 0 1
1 0 1 0 1
1 0 1 1 1
5 5
1 0 1 0 1
0 0 0 0 0
1 0 1 0 1
0 0 0 0 0
1 0 1 0 1
0 0
`
).split("\n");

const input = (() => {
  let line = 0;
  return () => stdin[line++];
})();

let dx = [1, -1, 0, 0, -1, 1, -1, 1];
let dy = [0, 0, -1, 1, -1, -1, 1, 1];
let graph, isVisited;
let islandCnt = 0;
while (true) {
  const [w, h] = input().split(" ").map(Number);
  if (w === 0 && h === 0) break;

  graph = Array(h)
    .fill(0)
    .map(() => Array(w).fill(0));
  isVisited = Array(h)
    .fill(false)
    .map(() => Array(w).fill(false));
  for (let y = 0; y < h; y++) {
    let inputList = input().split(" ").map(Number);
    // console.log(inputList, graph);
    for (let x = 0; x < w; x++) {
      graph[y][x] = inputList[x];
    }
  }

  for (let y = 0; y < h; y++) {
    for (let x = 0; x < w; x++) {
      if (isVisited[y][x] === false && graph[y][x] === 1) {
        dfs(x, y, w, h);
        islandCnt++;
      }
    }
  }
  console.log(islandCnt);
  islandCnt = 0;
}

function dfs(x, y, w, h) {
  if (isVisited[y][x] === true) return;

  isVisited[y][x] = true;
  for (let i = 0; i < 8; i++) {
    let [nx, ny] = [x + dx[i], y + dy[i]];
    if (nx >= 0 && nx < w && ny >= 0 && ny < h) {
      if (graph[ny][nx] === 1 && isVisited[ny][nx] === false) {
        dfs(nx, ny, w, h);
      }
    }
  }
}

function bfs(x, y, w, h) {
  q = [];
  q.push([x, y]);

  while (q.length > 0) {
    let [nowX, nowY] = q.shift();
    isVisited[nowY][nowX] = true;

    for (let i = 0; i < 8; i++) {
      let [nx, ny] = [nowX + dx[i], nowY + dy[i]];
      if (nx >= 0 && nx < w && ny >= 0 && ny < h) {
        if (graph[ny][nx] === 1 && isVisited[ny][nx] === false) {
          q.push([nx, ny]);
        }
      }
    }
  }
}
