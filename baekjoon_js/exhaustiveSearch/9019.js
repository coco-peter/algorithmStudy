("use strict");

const fs = require("fs");

const stdin = (process.platform === "linux"
  ? fs.readFileSync("/dev/stdin").toString()
  : `3
1234 3412
1000 1
1 16
`
).split("\n");

const input = (() => {
  let line = 0;
  return () => stdin[line++];
})();

let T = Number(input());
let num, target;
let isVisited;
while (T--) {
  [num, target] = input().split(" ").map(Number);
  isVisited = Array(10001).fill(false);
  console.log(BFS(num));
}

// let a = [];
// a = a + "hi";
// console.log(a);

function BFS(start) {
  q = [];
  q.push([start, []]);

  while (q.length > 0) {
    let [nowNum, history] = q.shift();
    isVisited[nowNum] = true;
    // console.log(nowNum, history);
    if (nowNum === target) return history;

    let commandD = nowNum * 2;
    if (commandD > 9999) commandD = commandD % 10000;
    if (isVisited[commandD] === false) {
      q.push([commandD, history + "D"]);
      //   isVisited[commandD] = true;
    }

    let commandS = nowNum - 1;
    if (commandS === 0) commandS = 9999;
    if (isVisited[commandS] === false) {
      q.push([commandS, history + "S"]);
      //   isVisited[commandS] = true;
    }

    // let commandL = "";
    // commandL += String(nowNum)[1];
    // commandL += String(nowNum)[2];
    // commandL += String(nowNum)[3];
    // commandL += String(nowNum)[0];

    let commandL = Number(
      String((nowNum % 1000) * 10 + parseInt(nowNum / 1000))
    );
    // console.log(nowNum, commandL);
    if (isVisited[commandL] === false) {
      q.push([commandL, history + "L"]);
      //   isVisited[Number(commandL)] = true;
    }
    // let commandR = "";
    // commandR += String(nowNum)[3];
    // commandR += String(nowNum)[0];
    // commandR += String(nowNum)[1];
    // commandR += String(nowNum)[2];

    let commandR = Number(String((nowNum % 10) * 1000 + parseInt(nowNum / 10)));
    if (isVisited[commandR] === false) {
      q.push([commandR, history + "R"]);
      //   isVisited[Number(commandR)] = true;
    }
  }
}
