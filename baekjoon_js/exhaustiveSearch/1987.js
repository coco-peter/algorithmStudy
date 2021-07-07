("use strict");

const fs = require("fs");

const stdin = (process.platform === "linux"
  ? fs.readFileSync("/dev/stdin").toString()
  : `2 4
CAAB
ADCB
`
).split("\n");

const input = (() => {
  let line = 0;
  return () => stdin[line++];
})();

const [R, C] = input().split(" ").map(Number);
let graph = Array(R)
  .fill("")
  .map(() => Array(C).fill(""));

let dx = [1, -1, 0, 0];
let dy = [0, 0, -1, 1];

for (let i = 0; i < R; i++) {
  let word = input();
  for (let j = 0; j < C; j++) {
    graph[i][j] = word[j];
  }
}

let maxCnt = 0;
// DFS(0, 0, [graph[0][0]]);
console.log(maxCnt);

// let a = [0, 0];
// let b = a.slice();
// b.push(1);
// console.log(a, b);

let a = [0, 0];
let b = a.slice() + [2];
console.log(a, b);

function DFS(x, y, history) {
  let isPossible = 0;

  for (let i = 0; i < 4; i++) {
    [nx, ny] = [x + dx[i], y + dy[i]];
    // console.log(x, y, nx, ny, history);
    if (
      nx > -1 &&
      nx < C &&
      ny > -1 &&
      ny < R &&
      history.find((e) => e === graph[ny][nx]) === undefined
    ) {
      temphitory = history.slice();
      temphitory.push(graph[ny][nx]);
      DFS(nx, ny, temphitory);
    } else {
      isPossible += 1;
    }
  }

  if (isPossible == 4) {
    maxCnt = Math.max(maxCnt, history.length);
    // console.log("HI");
    return;
  }
}

// function BFS(x, y) {
//   q = [];
//   q.push([x, y, 1, [graph[y][x]]]);
//   let maxCnt = 0;
//   while (q.length > 0) {
//     let [nowX, nowY, nowCnt, history] = q.shift();

//     let nx, ny, temphitory;
//     nowCnt++;
//     for (let i = 0; i < 4; i++) {
//       [nx, ny] = [nowX + dx[i], nowY + dy[i]];
//       //   console.log(nowX, nowY, nx, ny, history);
//       if (nx > -1 && nx < C && ny > -1 && ny < R)
//         if (history.find((e) => e === graph[ny][nx]) === undefined) {
//           temphitory = history.slice();
//           temphitory.push(graph[ny][nx]);
//           q.push([nx, ny, nowCnt, temphitory]);
//           maxCnt = Math.max(maxCnt, nowCnt);
//         }
//     }

//     // if(history.find((e) => e === graph[nowY][nowX]))
//   }

//   return maxCnt;
// }
