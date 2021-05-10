("use strict");

const fs = require("fs");

const stdin = (process.platform === "linux"
  ? fs.readFileSync("/dev/stdin").toString()
  : `6
20 1 15 8 4 10
`
).split("\n");

const input = (() => {
  let line = 0;
  return () => stdin[line++];
})();

const N = Number(input());
let numList = input().split(" ").map(Number);
let isVisited = Array(numList.length).fill(false);
let q = [];
let maxValue = 0;

function setPrint() {
  for (let i = 0; i < q.length; i++) process.stdout.write(`${String(q[i])} `);
  console.log(" ");
}

function setMaxValue() {
  let ans = 0;
  for (let i = 0; i < q.length - 1; i++) {
    ans += Math.abs(q[i] - q[i + 1]);
  }
  maxValue = Math.max(maxValue, ans);
}

// 순열
function DFS(start) {
  if (start === numList.length) {
    setMaxValue();
    return;
  }

  for (let i = 0; i < numList.length; i++) {
    if (isVisited[i] === false) {
      isVisited[i] = true;
      q.push(numList[i]);
      DFS(start + 1);
      q.pop();
      isVisited[i] = false;
    }
  }
}

DFS(0);
console.log(maxValue);
// console.log(ans);
