("use strict");

const fs = require("fs");
const stdin = (process.platform === "linux"
  ? fs.readFileSync("/dev/stdin").toString()
  : `4 7
20 15 10 17
`
).split("\n");

const input = (() => {
  let line = 0;
  return () => stdin[line++];
})();

const [N, M] = input().split(" ").map(Number);
let woodList = input().split(" ").map(Number);

// Math.max.apply(null, woodList);
let left = 0;
let right = Math.max(...woodList);
let maxValue = 0;

while (left <= right) {
  let mid = parseInt((left + right) / 2);
  let cuttedwood = 0;
  //   woodList.forEach((e) => {
  //     if (e - mid > 0) {
  //       cuttedwood += e - mid;
  //     } else cuttedwood += 0;
  //   });
  for (wood of woodList) {
    if (wood - mid > 0) cuttedwood += wood - mid;
  }

  if (cuttedwood >= M) {
    left = mid + 1;
    if (maxValue < mid) maxValue = mid;
  } else {
    right = mid - 1;
  }
}

console.log(maxValue);
