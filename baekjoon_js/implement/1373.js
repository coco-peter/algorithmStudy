("use strict");

const fs = require("fs");
const stdin = (process.platform === "linux"
  ? fs.readFileSync("/dev/stdin").toString()
  : `11001100
`
).split("\n");

const input = (() => {
  let line = 0;
  return () => stdin[line++];
})();

let binary = [1, 2, 3, 4, 5, 6, 7, 8];
const inputBinary = Number(input());
console.log(parseInt(inputBinary, 2).toString(8));

// console.log(
//   NtoB(BtoN(String(inputBinary), 2, 0), 8, "")
//     .split("")
//     .reverse()
//     .join("")
// );

// function BtoN(B, N, res) {
//   index = 0;
//   for (let i = String(B).length - 1; i > -1; i--) {
//     let a = Number(B[i]) * Math.pow(N, index);

//     index++;
//     res += a;
//   }
//   return res;
// }

// function NtoB(N, B, res) {
//   if (N < B) {
//     return N;
//   }

//   let C = parseInt(N / B);
//   let D = N % B;
//   res += String(D);

//   return res + NtoB(C, B, "");
// }
