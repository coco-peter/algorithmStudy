("use strict");

const fs = require("fs");
const stdin = (process.platform === "linux"
  ? fs.readFileSync("/dev/stdin").toString()
  : `10 1 10 2 1
`
).split("\n");

const input = (() => {
  let line = 0;
  return () => stdin[line++];
})();

const [F, S, G, U, D] = input().split(" ").map(Number);

let isVisited = Array(F + 1).fill(false);
let upDownBtn = [U, -D];
let isPossible = false;

console.log(BFS(S));

function BFS(start) {
  q = [];
  q.push([start, 0]);

  while (q.length > 0) {
    let [nowStair, nowCnt] = q.shift();

    if (nowStair === G) return nowCnt;
    nowCnt++;
    for (let i = 0; i < 2; i++) {
      if (
        nowStair + upDownBtn[i] > 0 &&
        nowStair + upDownBtn[i] < F + 1 &&
        isVisited[nowStair + upDownBtn[i]] === false
      ) {
        q.push([nowStair + upDownBtn[i], nowCnt]);
        isVisited[nowStair + upDownBtn[i]] = true;
      }
      //   console.log(nowStair, q, nowStair + upDownBtn[i]);
    }
  }

  return "use the stairs";
}
