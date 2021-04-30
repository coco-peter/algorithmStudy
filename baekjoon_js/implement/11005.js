("use strict");

const fs = require("fs");
const stdin = (process.platform === "linux"
  ? fs.readFileSync("/dev/stdin").toString()
  : `8 8
`
).split("\n");

const input = (() => {
  let line = 0;
  return () => stdin[line++];
})();

let binary = [
  "0",
  "1",
  "2",
  "3",
  "4",
  "5",
  "6",
  "7",
  "8",
  "9",
  "A",
  "B",
  "C",
  "D",
  "E",
  "F",
  "G",
  "H",
  "I",
  "J",
  "K",
  "L",
  "M",
  "N",
  "O",
  "P",
  "Q",
  "R",
  "S",
  "T",
  "U",
  "V",
  "W",
  "X",
  "Y",
  "Z",
];

const [number, binaryNumber] = input().split(" ").map(Number);

console.log(NtoB(number, binaryNumber, "").split("").reverse().join(""));

function NtoB(N, B, res) {
  if (N < B) return binary[N];
  //   const NLength = String(N).length;
  let C = parseInt(N / B);
  let D = binary[N % B];
  res += D;

  //   console.log(N, B, res);

  return res + NtoB(C, B, "");
}
