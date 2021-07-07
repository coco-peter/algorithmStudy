("use strict");

const fs = require("fs");
const stdin = (process.platform === "linux"
  ? fs.readFileSync("/dev/stdin").toString()
  : `5
1 3 2 -1
2 4 4 -1
3 1 2 4 3 -1
4 2 4 3 3 5 6 -1
5 4 6 -1
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

for (let i = 0; i < N; i++) {
  let nodeList = input().split(" ").map(Number);
  let startNode = nodeList[0];
  let j = 1;
  while (nodeList[j] != -1) {
    graph[startNode].push([nodeList[j], nodeList[j + 1]]);
    j += 2;
  }
}

// console.log(graph);

function bfs(start) {
  q = [];
  q.push([start, 0]);

  while (q.length > 0) {
    [node, value] = q.shift();
    isVisited[node] = true;
    // console.log(node, value);
    for ([nextNode, nextValue] of graph[node]) {
      //   console.log(nextNode, nextValue);
      if (isVisited[nextNode] === false) {
        q.push([nextNode, value + nextValue]);
        if (maxValue < value + nextValue) {
          //   console.log(maxNode, maxValue);
          maxValue = value + nextValue;
          maxNode = nextNode;
        }
      }
    }
  }
}

let [maxValue, maxNode] = [0, 0];
let isVisited = Array(N + 1).fill(false);
bfs(1);

maxValue = 0;
isVisited = Array(N + 1).fill(false);
bfs(maxNode);

console.log(maxValue);
