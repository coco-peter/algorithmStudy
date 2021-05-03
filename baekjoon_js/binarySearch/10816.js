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
let cardList = input().split(" ").map(Number);
const M = Number(input());
let targetList = input().split(" ").map(Number);

function sortFunc(a, b) {
  return a - b;
}

function binarySearchFirst(start, end, target) {
  if (start > end) {
    return -1;
  }

  let mid = parseInt((start + end) / 2);

  if (cardList[mid] === target) {
    if (mid === 0) return mid;
    else {
      if (cardList[mid] > cardList[mid - 1]) return mid;
      else return binarySearchFirst(start, mid - 1, target);
    }
  } else if (cardList[mid] > target) {
    return binarySearchFirst(start, mid - 1, target);
  } else if (cardList[mid] < target) {
    return binarySearchFirst(mid + 1, end, target);
  }
}

function binarySearchEnd(start, end, target) {
  if (start > end) {
    return -1;
  }

  let mid = parseInt((start + end) / 2);

  if (cardList[mid] === target) {
    if (mid === cardList.length - 1) return mid;
    else {
      if (cardList[mid] < cardList[mid + 1]) return mid;
      else return binarySearchEnd(mid + 1, end, target);
    }
  } else if (cardList[mid] > target) {
    return binarySearchEnd(start, mid - 1, target);
  } else if (cardList[mid] < target) {
    return binarySearchEnd(mid + 1, end, target);
  }
}

cardList.sort(sortFunc);

// console.log(cardList);
let result = "";
for (let i = 0; i < M; i++) {
  let first = binarySearchFirst(0, cardList.length - 1, targetList[i]);
  if (first === -1) result += "0 ";
  else {
    let last = binarySearchEnd(0, cardList.length - 1, targetList[i]);
    result += `${last - first + 1} `;
  }
}

console.log(result);
// targetList.forEach((e) => {
//   let first = binarySearchFirst(0, cardList.length - 1, e);
//   if (first === -1) process.stdout.write(`0 `);
//   else {
//     let last = binarySearchEnd(0, cardList.length - 1, e);
//     process.stdout.write(`${last - first + 1} `);
//   }
// });
