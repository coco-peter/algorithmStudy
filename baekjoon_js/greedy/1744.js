("use strict");

const fs = require("fs");
const stdin = (process.platform === "linux"
  ? fs.readFileSync("/dev/stdin").toString()
  : `7
0
1
3
3
4
5
6
`
).split("\n");

const input = (() => {
  let line = 0;
  return () => stdin[line++];
})();

const N = Number(input());
let plusArr = [];
let minusArr = [];
for (let i = 0; i < N; i++) {
  let num = Number(input());
  if (num > 0) plusArr.push(num);
  else minusArr.push(num);
}

plusArr.sort((a, b) => b - a);
minusArr.sort((a, b) => a - b);

let result = 0;
for (let i = 0; i < plusArr.length; i += 2) {
  if (i == plusArr.length - 1) result += plusArr[i];
  else {
    // console.log(plusArr[i], plusArr[i + 1]);
    if (plusArr[i + 1] === 1) result += plusArr[i] + plusArr[i + 1];
    else result += plusArr[i] * plusArr[i + 1];
  }
  //   console.log(result);
}

for (let i = 0; i < minusArr.length; i += 2) {
  if (i == minusArr.length - 1) result += minusArr[i];
  else {
    result += minusArr[i] * minusArr[i + 1];
  }
  //   console.log(result);
}

console.log(result);
