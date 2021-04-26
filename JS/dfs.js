// const fs = require("fs");
// const { BADFLAGS } = require('node:dns');
// const stdin = (process.platform === "linux"
//   ? fs.readFileSync("/dev/stdin").toString()
//   : `1 2 7 6 8 3 4 5`
// ).split("\n");

// const input = (() => {
//   let line = 0;
//   return () => stdin[line++];
// })();

let graph = [
  [],
  [2, 3, 8],
  [1, 7],
  [1, 4, 5],
  [3, 5],
  [3, 4],
  [7],
  [2, 6, 8],
  [1, 7],
];
let isVisited = Array.from({ length: 9 }, () => false);

console.log(graph);
console.log(isVisited);

function dfs(arr, node) {
  if (isVisited[node] == true) return;

  //   console.log(node);
  process.stdout.write(String(node));
  process.stdout.write(" ");
  isVisited[node] = true;

  for (let i of arr[node]) {
    // console.log(arr[node], i);
    dfs(arr, i);
  }
}

dfs(graph, 1);
