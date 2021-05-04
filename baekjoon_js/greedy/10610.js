("use strict");

const fs = require("fs");
const stdin = (process.platform === "linux"
  ? fs.readFileSync("/dev/stdin").toString()
  : `31
`
).split("\n");

const input = (() => {
  let line = 0;
  return () => stdin[line++];
})();

const N = input();

let isthereZero = false;
let numArr = [];
let sumN = 0;

// if (N.find((e) => e === 0) === undefined) console.log("HI");

for (let i = 0; i < N.length; i++) {
  if (Number(N[i]) === 0) isthereZero = true;
  sumN += Number(N[i]);
  numArr.push(Number(N[i]));
}

// console.log(N[i], sumN, isthereZero);
if (sumN % 3 !== 0) console.log("-1");
else if (!isthereZero) console.log("-1");
else {
  numArr.sort((a, b) => b - a);
  console.log(numArr.join(""));
}
