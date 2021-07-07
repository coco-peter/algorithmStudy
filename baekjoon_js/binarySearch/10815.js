("use strict");

const fs = require("fs");
const stdin = (process.platform === "linux"
  ? fs.readFileSync("/dev/stdin").toString()
  : `10
6 3 2 10 10 10 -10 -10 7 3
8
10 9 -5 2 3 4 5 -10
`
).split("\n");

const input = (() => {
  let line = 0;
  return () => stdin[line++];
})();

const N = Number(input());
let cardList = input()
  .split(" ")
  .map(Number)
  .sort((a, b) => {
    return a - b;
  });
const M = Number(input());
let result = "";
let targetList = input()
  .split(" ")
  .map((event) => {
    result += `${binarySearch(0, cardList.length - 1, Number(event))} `;
  });

function binarySearch(start, end, target) {
  if (start > end) return 0;

  let mid = parseInt((start + end) / 2);

  if (cardList[mid] === target) return 1;
  else if (cardList[mid] > target) return binarySearch(start, mid - 1, target);
  else if (cardList[mid] < target) return binarySearch(mid + 1, end, target);
}

// let result = "";
// for (let i = 0; i < M; i++) {
//   result += `${binarySearch(0, cardList.length - 1, targetList[i])} `;
// }
console.log(result);
