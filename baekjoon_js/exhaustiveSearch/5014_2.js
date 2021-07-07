("use strict");

const fs = require("fs");

const stdin = (
  process.platform === "linux"
    ? fs.readFileSync("/dev/stdin").toString()
    : `100 2 1 1 0
`
).split("\n");

const input = (() => {
  let line = 0;
  return () => stdin[line++];
})();

const [F, S, G, U, D] = input().split(" ").map(Number);

// BFS
let isVisited = Array(F + 1).fill(false);
let elevatorBtn = [U, -D];
let isPossible = false;
let q = [];
q.push([S, 0]);
isVisited[S] = true;

while (q.length > 0) {
  let [nowNode, nowCnt] = q.shift();
  //   console.log(nowNode, nowCnt);
  if (nowNode === G) {
    isPossible = true;
    console.log(nowCnt);
    break;
  }
  for (let i = 0; i < 2; i++) {
    let nextNode = nowNode + elevatorBtn[i];
    if (isVisited[nextNode] === false && nextNode > 0 && nextNode < F + 1) {
      q.push([nextNode, nowCnt + 1]);
      isVisited[nextNode] = true;
    }
  }
}

if (!isPossible) console.log("use the stairs");
