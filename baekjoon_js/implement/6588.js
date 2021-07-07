("use strict");

const fs = require("fs");
const stdin = (process.platform === "linux"
  ? fs.readFileSync("/dev/stdin").toString()
  : `8
  6
20
42
0
`
).split("\n");

const input = (() => {
  let line = 0;
  return () => stdin[line++];
})();

let primeList = Array(1000001).fill(Number(0));

primeList[1] = primeList[0] = 1;

for (let i = 2; i < parseInt(primeList.length / 2); i++) {
  for (let j = i + i; j < primeList.length; j += i) {
    if (primeList[j] === 0) primeList[j] = 1;
  }
}

while (true) {
  const N = Number(input());
  if (N === 0) break;

  // setPrimeNumber();

  let firstNum = 3;
  let secondNum = N - 1;
  let isPossible = false;

  while (firstNum <= secondNum) {
    if (firstNum + secondNum === N) {
      if (primeList[firstNum] === 0 && primeList[secondNum] === 0) {
        console.log(`${N} = ${firstNum} + ${secondNum}`);
        isPossible = true;
        break;
      }
      if (primeList[firstNum] === 1) {
        while (primeList[firstNum]) {
          firstNum += 2;
        }
      }
      if (primeList[secondNum] === 1) {
        while (primeList[secondNum]) {
          secondNum -= 2;
        }
      }
    } else if (firstNum + secondNum > N) {
      secondNum -= 2;
    } else if (firstNum + secondNum < N) {
      firstNum += 2;
    }
  }

  if (!isPossible) console.log("Goldbach's conjecture is wrong.");
}
//   function combinationFunc() {
//     for (let i = 3; i <= N; i += 2) {
//       if (primeList[i] === 0) {
//         firstNum = i;
//         for (let j = N - 1; j >= i; j -= 2) {
//           if (primeList[j] === 0 && firstNum + j === N) {
//             secondNum = j;
//             //   combination.push({ firstNum, secondNum });

//             if (maxDiff <= secondNum - firstNum) {
//               minNum = firstNum;
//               maxNum = secondNum;
//               maxDiff = secondNum - firstNum;
//               console.log(`${N} = ${minNum} + ${maxNum}`);
//               return;
//             }
//           }
//         }
//       }
//     }
//   }

//   if (minNum > 1 && maxNum > 1) console.log(`${N} = ${minNum} + ${maxNum}`);
//   else console.log("Goldbach's conjecture is wrong.");

//   let minNum = 0;
//   let maxNum = 0;
//   let maxDiff = 0;

//   if (combination) {
//     combination.forEach((element) => {
//       let diff = element.secondNum - element.firstNum;

//       if (maxDiff <= diff) {
//         minNum = element.firstNum;
//         maxNum = element.secondNum;
//         maxDiff = diff;
//       }
//       // console.log(maxDiff, minNum, maxNum);
//     });
//     console.log(`${N} = ${minNum} + ${maxNum}`);
//   } else {
//     console.log("Goldbach's conjecture is wrong.");
//   }
//   // console.log(combination);
