// 3/10 study dfs & bfs javascript_1260

const fs = require("fs");
const stdin = (process.platform === "linux"
  ? fs.readFileSync("/dev/stdin").toString()
  : `1000 1 1000
999 1000
`
).split("\n");

const input = (() => {
  let line = 0;
  return () => stdin[line++];
})();

let [N, M, V] = input().split(" ").map(Number);

let graph = Array(N + 1)
  .fill(null)
  .map(() => Array());

for (i = 0; i < M; i++) {
  const [startNode, endNode] = input().split(" ").map(Number);
  graph[startNode].push(endNode);
  graph[endNode].push(startNode);
}

for (i = 1; i < M + 1; i++) {
  graph[i].sort();
}

function bfs(arr, node) {
  b = [];
  b.push(node);
  isVisited[node] = true;

  while (b.length > 0) {
    nowNode = b.shift();
    process.stdout.write(String(nowNode));
    process.stdout.write(" ");
    for (let i of arr[nowNode]) {
      if (isVisited[i] == false) {
        b.push(i);
        isVisited[i] = true;
      }
    }
  }
}

function dfs(arr, node) {
  isVisited[node] = true;

  process.stdout.write(String(node));
  process.stdout.write(" ");
  for (let i of arr[node]) {
    if (isVisited[i] == false) {
      dfs(arr, i);
    }
  }
}

let isVisited = Array.from({ length: N + 1 }, () => false);
dfs(graph, V);
console.log();

isVisited = Array.from({ length: N + 1 }, () => false);
bfs(graph, V);
