("use strict");

const fs = require("fs");
const stdin = (process.platform === "linux"
  ? fs.readFileSync("/dev/stdin").toString()
  : `12
1 2 3
1 3 2
2 4 5
3 5 11
3 6 9
4 7 1
4 8 7
5 9 15
5 10 4
6 11 6
6 12 10
`
).split("\n");

const input = (() => {
  let line = 0;
  return () => stdin[line++];
})();

const N = Number(input());

let graph = Array(N + 1)
  .fill(null)
  .map(() => Array());

for (let i = 0; i < N - 1; i++) {
  const [startNode, endNode, value] = input().split(" ").map(Number);
  graph[startNode].push([endNode, value]);
  graph[endNode].push([startNode, value]);
}

function bfs(start) {
  q = [];
  q.push([start, 0]);
  while (q.length > 0) {
    [node, value] = q.shift();

    isVisited[node] = true;
    for ([nextNode, nextValue] of graph[node]) {
      if (isVisited[nextNode] != true) {
        q.push([nextNode, value + nextValue]);
        if (maxValue < value + nextValue) {
          maxValue = value + nextValue;
          maxNode = nextNode;
        }
      }
    }
  }
}

let [maxValue, maxNode] = [0, 0];
let isVisited = Array(N).fill(false);
bfs(1);

maxValue = 0;
isVisited = Array(N).fill(false);
bfs(maxNode);

console.log(maxValue);
