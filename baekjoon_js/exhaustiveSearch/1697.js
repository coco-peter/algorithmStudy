("use strict");

const fs = require("fs");
const stdin = (process.platform === "linux"
  ? fs.readFileSync("/dev/stdin").toString()
  : `5 17
`
).split("\n");

const input = (() => {
  let line = 0;
  return () => stdin[line++];
})();

const [N, K] = input().split(" ").map(Number);

let isVistied = Array(100001).fill(false);

console.log(BFS(N));

function BFS(start) {
  q = [];
  q.push([start, 0]);

  while (q.length > 0) {
    let [nowPos, nowCnt] = q.shift();
    // console.log(nowPos, nowPos + 1, nowPos - 1, nowPos * 2, nowCnt);
    if (nowPos === K) return nowCnt;

    nowCnt++;
    if (nowPos + 1 < 100001 && isVistied[nowPos + 1] === false) {
      q.push([nowPos + 1, nowCnt]);
      isVistied[nowPos + 1] = true;
    }

    if (nowPos - 1 > -1 && isVistied[nowPos - 1] === false) {
      q.push([nowPos - 1, nowCnt]);
      isVistied[nowPos - 1] = true;
    }

    if (nowPos * 2 < 100001 && isVistied[nowPos * 2] === false) {
      q.push([nowPos * 2, nowCnt]);
      isVistied[nowPos * 2] = true;
    }
  }
}
