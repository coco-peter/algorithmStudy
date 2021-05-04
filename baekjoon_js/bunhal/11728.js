("use strict");

const fs = require("fs");
const stdin = (process.platform === "linux"
  ? fs.readFileSync("/dev/stdin").toString()
  : `4 3
2 3 5 9
1 4 7
`
).split("\n");

const input = (() => {
  let line = 0;
  return () => stdin[line++];
})();

const [M, N] = input().split(" ").map(Number);
let firstArray = input().split(" ").map(Number);
let secondArray = input().split(" ").map(Number);

let [firstArrIndex, secondArrIndex] = [0, 0];
let [firstArrLength, secondArrLength] = [firstArray.length, secondArray.length];
let emergeArray = "";

while (true) {
  if (firstArray[firstArrIndex] < secondArray[secondArrIndex]) {
    // emergeArray.push(firstArray[firstArrIndex]);
    emergeArray += `${firstArray[firstArrIndex]} `;
    firstArrIndex++;
  } else {
    // emergeArray.push(secondArray[secondArrIndex]);
    emergeArray += `${secondArray[secondArrIndex]} `;
    secondArrIndex++;
  }

  if (firstArrIndex === firstArrLength) {
    for (let i = secondArrIndex; i < secondArrLength; i++) {
      emergeArray += `${secondArray[i]} `;
      // emergeArray.push(secondArray[i]);
    }
    break;
  } else if (secondArrIndex === secondArrLength) {
    for (let i = firstArrIndex; i < firstArrLength; i++) {
      emergeArray += `${firstArray[i]} `;
      //   emergeArray.push(firstArray[i]);
    }
    break;
  }
}

console.log(emergeArray);
