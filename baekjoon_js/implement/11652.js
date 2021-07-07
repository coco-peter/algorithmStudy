const fs = require("fs");
const stdin = (process.platform === "linux"
  ? fs.readFileSync("/dev/stdin").toString()
  : `2
1
-1
`
).split("\n");

const input = (() => {
  let line = 0;
  return () => stdin[line++];
})();

function sortF(a, b) {
  return a - b;
}

let N = Number(input());
let numList = Array(N).fill(0);
for (let i = 0; i < N; i++) {
  numList[i] = Number(input());
}

numList.sort(sortF);

minNumber = numList[0];
tempCount = 1;
maxCount = 1;

for (let i = 0; i < N - 1; i++) {
  if (numList[i + 1] == numList[i]) {
    tempCount++;
  } else if (numList[i + 1] != numList[i]) {
    tempCount = 1;
  }

  if (maxCount < tempCount) {
    maxCount = tempCount;
    minNumber = numList[i];
  }
}

console.log(String(minNumber));
