("use strict");

const fs = require("fs");

const stdin = (process.platform === "linux"
  ? fs.readFileSync("/dev/stdin").toString()
  : `3
1033 8179
1373 8017
1033 1033
`
).split("\n");

const input = (() => {
  let line = 0;
  return () => stdin[line++];
})();

let T = Number(input());
let primeNumList = Array(10001).fill(false);

primeNumList[0] = primeNumList[1] = true;

for (let i = 2; i < 5001; i++) {
  for (let j = i + i; j < 10001; j += i) {
    if (primeNumList[j] === false) primeNumList[j] = true;
  }
}

while (T--) {
  let [num, target] = input().split(" ").map(Number);
  let isVisited = Array(10001).fill(false);
  console.log(BFS(num, target, isVisited));
}

// let i = "1923";
// console.log(i.slice(0, 2) + i.slice(2, 4));
// let j = String(i);
// j = j.replace(j[0], "2");

// console.log(j);

function BFS(start, target, isVisited) {
  q = [];
  q.push([start, 0]);

  let nextNum;
  while (q.length > 0) {
    let [nowNum, nowCnt] = q.shift();
    if (nowNum === target) return nowCnt;
    nowCnt++;

    strNum = String(nowNum);
    for (let j = 0; j < 4; j++) {
      for (let i = 0; i < 10; i++) {
        if (j == 0 && i == 0) continue;
        // nextNum = String(nowNum);
        // nextNum = nextNum.replace(nextNum[j], String(i));

        nextNum = Number(
          strNum.slice(0, j) + String(i) + strNum.slice(j + 1, 4)
        );
        // console.log(nextNum);
        if (isVisited[nextNum] === false && primeNumList[nextNum] === false) {
          isVisited[nextNum] = true;
          q.push([nextNum, nowCnt]);
        }
      }
    }
  }
  return "Impossible";
}
