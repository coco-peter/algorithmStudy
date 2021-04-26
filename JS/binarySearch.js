const fs = require("fs");
const stdin = (process.platform === "linux"
  ? fs.readFileSync("/dev/stdin").toString()
  : `5
8 3 7 9 2
3
5 7 9`
).split("\n");

const input = (() => {
  let line = 0;
  return () => stdin[line++];
})();

let N = parseInt(input());
let numList = input().split(" ").map(Number);

numList.sort();
console.log(numList);
let M = parseInt(input());
let targetList = input().split(" ").map(Number);
console.log(targetList);

function binarySearch(start, end, target) {
  if (start > end) {
    return 0;
  }

  mid = parseInt((start + end) / 2);

  if (numList[mid] === target) {
    return 1;
  } else if (numList[mid] > target) {
    return binarySearch(start, mid - 1, target);
  } else {
    return binarySearch(mid + 1, end, target);
  }
}
for (let i = 0; i < targetList.length; i++) {
  //   console.log(targetList[i]);
  res = binarySearch(0, numList.length - 1, targetList[i]);
  if (res) console.log("Yes");
  else console.log("NO");
}
