const fs = require("fs");
const stdin = (process.platform === "linux"
  ? fs.readFileSync("/dev/stdin").toString()
  : `4 7
1 2 4
1 4 6
2 1 3
2 3 7
3 1 5
3 4 4
4 3 2
`
).split("\n");

const input = (() => {
  let line = 0;
  return () => stdin[line++];
})();

let [N, M] = input().split(" ").map(Number);
const INF = Number.MAX_SAFE_INTEGER;
let graph = Array(N + 1)
  .fill(INF)
  .map(() => Array(N + 1).fill(INF));

// console.log(graph);
for (let i = 0; i < M; i++) {
  const [startNode, endNode, value] = input().split(" ").map(Number);
  graph[startNode][endNode] = value;
}

// console.log(graph);

for (let y = 1; y < N + 1; y++) {
  for (let x = 1; x < N + 1; x++) {
    if (x === y) {
      graph[y][x] = 0;
    }
  }
}

for (let i = 1; i < N + 1; i++) {
  for (let j = 1; j < N + 1; j++) {
    for (let k = 1; k < N + 1; k++) {
      graph[j][k] = Math.min(graph[j][k], graph[j][i] + graph[i][k]);
    }
  }
}

for (let y = 1; y < N + 1; y++) {
  for (let x = 1; x < N + 1; x++) {
    process.stdout.write(String(graph[y][x]));
    process.stdout.write(" ");
  }
  console.log("");
}
// console.log(graph);
