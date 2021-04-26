const fs = require("fs");
const stdin = (process.platform === "linux"
  ? fs.readFileSync("/dev/stdin").toString()
  : `7 8
1 2
1 5
2 3
2 6
3 4
4 7
5 6
6 4
`
).split("\n");

const input = (() => {
  let line = 0;
  return () => stdin[line++];
})();

let [N, M] = input().split(" ").map(Number);

let graph = Array(N + 1)
  .fill(null)
  .map(() => Array());

let indegree = Array(N + 1).fill(0);

for (let i = 0; i < M; i++) {
  const [startNode, endNode] = input().split(" ").map(Number);
  graph[startNode].push(endNode);
  indegree[endNode]++;
}
function topologySort() {
  q = [];
  result = [];

  for (let i = 1; i < N + 1; i++) {
    if (indegree[i] === 0) q.push(i);
  }

  while (q.length > 0) {
    nowNode = q.shift();
    result.push(nowNode);

    for (let i of graph[nowNode]) {
      indegree[i]--;
      if (indegree[i] === 0) {
        q.push(i);
      }
    }
  }

  console.log(result);
}

topologySort();
