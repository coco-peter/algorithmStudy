("use strict");

const fs = require("fs");
const stdin = (process.platform === "linux"
  ? fs.readFileSync("/dev/stdin").toString()
  : `57 2
`
).split("\n");

const input = (() => {
  let line = 0;
  return () => stdin[line++];
})();

let [A, P] = input().split(" ").map(Number);

let numList = [A];
let nextA = 0;
while (true) {
  for (let j = 0; j < String(A).length; j++) {
    number = Math.pow(String(A)[j], P);
    nextA += number;
  }
  //   console.log(nextA);
  if (numList.find((e) => e === nextA) === undefined) numList.push(nextA);
  else {
    console.log(numList.findIndex((e) => e === nextA));
    break;
  }
  A = nextA;
  nextA = 0;
}
